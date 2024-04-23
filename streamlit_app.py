import streamlit as st
import datetime
from pandas import DataFrame
from streamlit_tree_select import tree_select
from nodes import NODES
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)


st.set_page_config(page_title="Detailed Report", layout="wide", initial_sidebar_state="expanded", page_icon="icon.png")
conn = st.connection("postgresql", type="sql")


@st.cache_data(ttl=3600)
def generate_detailed_report():
    # cp_raw = get_data('custom_profile.sql')
    # cp_df = pivot_custom_profile(cp_raw)
    df_raw = get_data('detailed_report.sql')
    dtype_dict = {
        'Document Version (Current Version)': 'int',
        'Document Version (Latest Version)': 'int',
        'Document Issue Date (Current Version)': 'datetime64[ns]',
        'Document Expiry Date (Current Version)': 'datetime64[ns]',
        'Staff Member Signed Up Date': 'datetime64[ns]',
    }
    for col in df_raw:
        if col.startswith('Is ') or col.startswith('Haven') or col.startswith('Completed '):
            dtype_dict[col] = 'object'
    df_raw = df_raw.astype(dtype_dict, errors='ignore')
    # df_merged = df_raw.merge(
    #     cp_df, 
    #     on=['employee_id', 'organisation_id'], 
    #     how='left'
    # )
    return df_raw


@st.cache_data(ttl=3600)
def generate_custom_profile():
    cp_raw = get_data('custom_profile.sql')
    return cp_raw


def get_data(file_path, **kwargs) -> DataFrame:
    with open(file_path, 'r') as sql_file:
        sql = sql_file.read()
    sql = sql.format(**kwargs)
    return conn.query(sql)


@st.cache_data(ttl=3600)
def pivot_and_merge(df, cp) -> DataFrame:
    cp_pivoted = cp.fillna('', inplace=False).pivot_table(
        index=['employee_id', 'organisation_id'],
        columns="field_name", 
        values="field_value", 
        aggfunc=lambda x: ' '.join(x),
        dropna=False
    )
    return df.merge(cp_pivoted, on=['employee_id', 'organisation_id'], how='left')


@st.cache_data(ttl=3600)
def get_tuple_element(my_tuple, index, default=None):
    try:
        return my_tuple[index]
    except IndexError:
        return default


def refresh_report() -> None:
    df = st.session_state.df
    for key, values in st.session_state.items():
        if key in df:
            if values: 
                if is_datetime64_any_dtype(df[key]):
                    df = df.loc[
                        (df[key].dt.date.between(
                            get_tuple_element(values, 0, datetime.date(1900, 1, 1)),
                            get_tuple_element(values, 1, datetime.date(2099, 12, 31)),
                        ))
                    ]
                elif is_numeric_dtype(df[key]):
                    df = df.loc[(df[key].between(*values)) | (df[key].isnull())]
                else:
                    df = df.loc[df[key].isin(values)]
    st.session_state.df_filtered = df


@st.cache_data
def update_nodes(cp) -> list:
    for section in cp['section_name'].unique().tolist():
        NODES[0]["children"].append({"label": section, "value": section, "children": []})
        for field in cp[cp['section_name'] == section]['field_name'].unique().tolist():
            NODES[0]["children"][-1]["children"].append({"label": field, "value": field}) 
    return NODES


def adjust_sidebar_padding():
    st.markdown(
        """
        <style>
        div[data-testid="stSidebarUserContent"]{padding-top: 48px;}
        </style>
        """,
        unsafe_allow_html=True
    )


def put_logo(img_file):
    st.image(img_file)
    st.markdown(
        '''
        <style>
        button[title="View fullscreen"]{visibility: hidden;}
        </style>
        ''', 
        unsafe_allow_html=True
    )


df = generate_detailed_report()
cp = generate_custom_profile()


if 'job_position_id' in st.query_params:
    org_id = get_data('rls.sql', job_position_id=st.query_params.job_position_id)['organisation_id'][0]
    df = df[df['organisation_id'] == org_id]
    cp_filtered = cp[cp['organisation_id'] == org_id]
    df = pivot_and_merge(df, cp_filtered)
else:
    cp_filtered = DataFrame(columns=cp.columns)
nodes = update_nodes(cp_filtered)


st.session_state.df = df
if 'df_filtered' not in st.session_state:
    st.session_state.df_filtered = st.session_state.df
all_cols = [column['value'] for node in nodes for section in node.get('children') for column in section.get('children')]


col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
with col1:
    put_logo('logo.svg')
with col2:
    st.metric('Total Users', value=st.session_state.df_filtered['Email'].nunique(), help='Number of unique emails')
with col3:
    st.metric('Total Records', value=len(st.session_state.df_filtered), help='Number of records')
with col4:  
    with st.popover(
        'Select Columns', 
        help='Select the columns you want to be part of the report', 
        disabled=False, 
        use_container_width=False
    ):
        if 'selected_cols' in st.session_state and st.session_state.selected_cols:
            checked = st.session_state.selected_cols['checked']
        else:
            checked = all_cols
        selected_cols = tree_select(
            nodes, 
            show_expand_all=True,
            check_model='leaf',
            expanded=[node['value'] for node in nodes],
            checked=checked,
            key='selected_cols'
        )

st.markdown("#")
if not st.session_state.df_filtered.empty and selected_cols['checked']:
    cols_to_show = ['Email'] + selected_cols['checked']
    st.dataframe(
        st.session_state.df_filtered[cols_to_show].set_index('Email'), 
        hide_index=False,
        use_container_width=True, 
    )
else:
    st.markdown(
        '''
        <div style="text-align: center; color: #758586; margin-top: 30px;">
            <p style="font-size: 20px;">Nothing to show 😟</p>
        </div>
        ''', 
        unsafe_allow_html=True
    )

# {k:v for k, v in st.session_state.items() if 'df' not in k}

with st.sidebar:
    adjust_sidebar_padding()
    filter_search = st.text_input('Search Filters', value="", placeholder='Search Filters', label_visibility='collapsed')
    for node in nodes:
        all = node.get('children')
        for section in all:
            section_name = section['value']
            with st.expander(section_name, expanded=True):
                for column in section.get('children'):
                    col = column['value']
                    if not filter_search or (filter_search and filter_search.lower() in col.lower()):
                        options = st.session_state.df[col].unique().tolist()
                        if None in options: options.remove(None)
                        if is_datetime64_any_dtype(st.session_state.df[col]):
                            # min_value = st.session_state.df[col].dt.date.min()
                            # max_value = st.session_state.df[col].dt.date.max()
                            st.date_input(col, 
                                key=col,
                                value=tuple(),      
                                # value=(min_value, max_value),
                                on_change=refresh_report,
                                format='YYYY/MM/DD',
                            )
                        elif is_numeric_dtype(st.session_state.df[col]):
                            _min = int(st.session_state.df[col].min())
                            _max = int(st.session_state.df[col].max())
                            st.slider(col,
                                key=col,
                                value=(_min, _max),
                                min_value=_min,
                                max_value=_max,
                                step=1,
                                on_change=refresh_report
                            )
                        else:
                            st.multiselect(col, 
                                key=col,
                                default=None,
                                options=options, 
                                format_func=lambda x: '(Blank)' if x is None else x,
                                on_change=refresh_report
                            )

# for row in st.session_state.df.itertuples():
    # st.write(f"{row.first_name} has email {row.email}:")