import streamlit as st
import plotly.graph_objects as go


def display_default_dashboard(df):
    pending_approvals_section = st.columns(2)
    pending_approvals_section[0].write('**Pending Approvals**')
    with pending_approvals_section[0].container(border=True):
        # print(df['Onboarding Current Step Type'].unique())
        count_approval = df[df['Onboarding Current Step Type'] == "Staff Member’s Approval"]['job_position_id'].nunique()
        onboarding = st.columns([0.4, 1.3, 0.7, 0.7])
        onboarding[0].image('onb.png')
        onboarding[1].markdown("<p style='color: black; font-size: 20px; text-align: left;'>Onboardings</p>", unsafe_allow_html=True)
        with onboarding[3]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=count_approval,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    pending_approvals_section[1].write("<p style='font-weight: bold; height: 26px;'></p>", unsafe_allow_html=True)
    with pending_approvals_section[1].container(border=True):  
        mandatory_docs = st.columns([0.4, 1.3, 0.7, 0.7])
        mandatory_docs[0].image('mand_docs.png')
        mandatory_docs[1].markdown("<p style='color: black; font-size: 18px; text-align: left;'>Mandatory Documents</p>", unsafe_allow_html=True)
        with mandatory_docs[3]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    
    users_section = st.columns([4, 3, 2])
    users_section[0].write('**Users**')
    with users_section[0].container(border=True): 
        cols = st.columns([1, 1, 2])
        cols[0].write('**Total Users**')
        with cols[1]:
            total_users_empty = st.empty()
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=9730,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
        cols = st.columns(2)
        with cols[0]:
            fig = go.Figure()
            labels = ['A', 'B', 'C', 'D']
            values = [20, 30, 40, 10]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
            fig.update_layout(title_text="User Status", title_x=0.33, height=355, legend=dict(orientation="h", font=dict(size=12)))
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
        with cols[1]:
            fig = go.Figure()
            labels = ['A', 'B', 'C', 'D']
            values = [20, 30, 40, 10]
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
            fig.update_layout(title_text="Signed Off", title_x=0.33, height=355, legend=dict(orientation="h", font=dict(size=12)))
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
        st.markdown("#")
    users_section[1].write("<p style='font-weight: bold; height: 26px;'></p>", unsafe_allow_html=True)
    with users_section[1].container(border=True): 
        st.write('**Added**')
        cols = st.columns(3)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Yesterday</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 7 Days</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 30 Days</p>", unsafe_allow_html=True)
    with users_section[1].container(border=True): 
        st.write('**Signed Up**')
        cols = st.columns(3)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Yesterday</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 7 Days</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 30 Days</p>", unsafe_allow_html=True)
    with users_section[1].container(border=True): 
        st.write('**Signed Off**')
        cols = st.columns(3)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Yesterday</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 7 Days</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=35)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 30 Days</p>", unsafe_allow_html=True)
    users_section[2].write("<p style='font-weight: bold; height: 26px;'></p>", unsafe_allow_html=True)
    with users_section[2].container(border=True):
        cols = st.columns([3, 2])
        cols[0].markdown("<p style='color: black; font-size: 16px; text-align: left;'>Invited & Not Signed Up</p>", unsafe_allow_html=True)
        # cols[0].write('**Invited & Not Signed Up**')
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            number={'font': {'size': 38, 'color': 'black'}},
            mode="number",
            value=300,
            domain={'row': 0, 'column': 1})
        )
        fig.update_layout(height=40)
        cols[1].plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    with users_section[2].container(border=True):
        cols = st.columns([3, 2])
        cols[0].markdown("<p style='color: black; font-size: 16px; text-align: left;'>Not assigned</p>", unsafe_allow_html=True)
        # cols[0].write('**Not assigned**')
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            number={'font': {'size': 38, 'color': 'black'}},
            mode="number",
            value=300,
            domain={'row': 0, 'column': 1})
        )
        fig.update_layout(height=40)
        cols[1].plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    compliance_left, compliance_right, onboarding_left, onboarding_right = st.columns(4)
    compliance_left.write('**Compliance**')
    with compliance_left.container(border=True):
        fig = go.Figure()
        labels = ['A', 'B', 'C', 'D']
        values = [20, 30, 40, 10]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
        fig.update_layout(title_text="Compliance Status", title_x=0.2, height=300, legend=dict(orientation="h", font=dict(size=12)))
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    compliance_right.write("<p style='font-weight: bold; height: 26px;'></p>", unsafe_allow_html=True)
    with compliance_right.container(border=True):
        fig = go.Figure()
        labels = ['A', 'B', 'C', 'D']
        values = [20, 30, 40, 10]
        fig = go.Figure(data=[go.Bar(y=labels, x=values, orientation='h')])
        fig.update_layout(title_text="Approaching Compliance", title_x=0.2, height=300, legend=dict(orientation="h", font=dict(size=12)))
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit") 
    onboarding_left.write('**Onboarding**')
    with onboarding_left.container(border=True):
        fig = go.Figure()
        labels = ['A', 'B', 'C', 'D']
        values = [20, 30, 40, 10]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])
        fig.update_layout(title_text="Onboarding Status", title_x=0.2, height=300, legend=dict(orientation="h", font=dict(size=12)))
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    onboarding_right.write("<p style='font-weight: bold; height: 26px;'></p>", unsafe_allow_html=True)
    with onboarding_right.container(border=True):
        fig = go.Figure()
        labels = ['A', 'B', 'C', 'D']
        values = [20, 30, 40, 10]
        fig = go.Figure(data=[go.Bar(y=labels, x=values, orientation='h')])
        fig.update_layout(title_text="Stalled Onboardings", title_x=0.2, height=300, legend=dict(orientation="h", font=dict(size=12)))
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit") 
    cols = st.columns([2, 1.1, 0.9])
    with cols[0].container(border=True):
        signed_off = st.columns([5, 3, 2])
        signed_off[0].markdown("<p style='color: black; font-size: 18px; text-align: left;'>Signed Off & Non-Compliant Users</p>", unsafe_allow_html=True)
        with signed_off[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    with cols[1].container(border=True):  
        signed_off = st.columns([5, 3])
        signed_off[0].markdown("<p style='color: black; font-size: 16px; text-align: left;'>Signed Up & Not Started Onboarding   </p>", unsafe_allow_html=True)
        with signed_off[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    with cols[2].container(border=True):  
        signed_off = st.columns([5, 3.5])
        signed_off[0].markdown("<p style='color: black; font-size: 18px; text-align: left;'>In Progress</p>", unsafe_allow_html=True)
        with signed_off[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
    compliance_section = st.columns(2)
    with compliance_section[0].container(border=True): 
        st.write('**Non-Compliant**')
        cols = st.columns(3)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Mandatory Documents</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>References</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Other</p>", unsafe_allow_html=True)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>DBS Update Service</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Professional Registration & Performance List</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; padding-top: 0p; text-align: center;'>Right To Work</p>", unsafe_allow_html=True)
    with compliance_section[1].container(border=True): 
        st.write('**Users Completed Onboarding**')
        cols = st.columns(3)
        with cols[0]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Yesterday</p>", unsafe_allow_html=True)
        with cols[1]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 7 Days</p>", unsafe_allow_html=True)
        with cols[2]:
            fig = go.Figure()
            fig.add_trace(go.Indicator(
                number={'font': {'size': 38, 'color': 'black'}},
                mode="number",
                value=300,
                domain={'row': 0, 'column': 1})
            )
            fig.update_layout(height=50)
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")
            st.write("<p style='font-size: 14px; text-align: center;'>Last 30 Days</p>", unsafe_allow_html=True)