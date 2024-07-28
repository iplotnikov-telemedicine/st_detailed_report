import streamlit as st
from streamlit_echarts import st_echarts
import plotly.graph_objects as go


def render_pie_donutradius():
    df = st.session_state.df_filtered.groupby(by="Document Status (Current Version)") \
        .agg(count_column=("Document Status (Current Version)", "count")).reset_index()
    options = {
        "title": {"show": True, "text": "Document Status (Current Version)"},
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center", "top": "bottom"},
        "series": [
            {
                "name": "Document Status (Current Version)",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 0,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {"show": False, "position": "center"},
                "labelLine": {"show": False},
            }
        ],
    }
    options["series"][0]["data"] = [{"name": row["Document Status (Current Version)"], "value": row["count_column"]} for _, row in df.iterrows()]
    my_chart = st_echarts(
        options=options, height="400px", key="eeechart"
    )


@st.cache_data
def get_plotly_donut(df):
    df = df.groupby(by="Document Status (Current Version)") \
        .agg(count_column=('Document Status (Current Version)', 'count')).reset_index()
    # fig = px.pie(
    #     data_frame=df,
    #     title="Document Status",
    #     names="Document Status (Current Version)",
    #     values="count_column",
    #     hole=0.6
    # )
    labels = df["Document Status (Current Version)"]
    values = df["count_column"]
    return go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
    # return fig


# fig = px.pie(
#     data_frame=df,
#     title="Document Status",
#     names="Document Status (Current Version)",
#     values="count_column",
#     color="Document Status (Current Version)",
#     hole=0.6
# )
# fig.update_layout(
#     # autosize=True, 
#     legend=dict(orientation="h", font=dict(size=12))
# ) 
# selected_points = plotly_events(fig, key='selected_points')
# if selected_points:
#     st.session_state["Document Status (Current Version) selected with chart"] = df["Document Status (Current Version)"].loc[selected_points[0]["pointNumber"]]