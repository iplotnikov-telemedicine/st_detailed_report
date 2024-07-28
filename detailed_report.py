import streamlit as st
from streamlit_tree_select import tree_select


def display_detailed_report(nodes, all_cols):
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    with col1:
        st.image('logo.svg')
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