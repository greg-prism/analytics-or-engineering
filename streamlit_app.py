import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.title("Engineering or Analytics?")
st.header("""This quiz is designed to find which aspects of data you most *enjoy* to see which field your interests most closely align with""")
st.subheader("""Please answer the following questions chossing a number from 1-5 with 1 being strongly disagree with 5 being strongly agree""")

# 1 - Engineering
r1 = st.radio('I enjoy building systems and processes', [1, 2, 3, 4, 5])

# 2 - Analytics
r2 = st.radio("I enjoy spotting patterns and trends", [1, 2, 3, 4, 5])

# 3 - Engineering
r3 = st.radio("I enjoy optimisng and improving efficiency", [1, 2, 3, 4, 5])

# 4 - Analytics
r4 = st.radio("I like to use statistics and mathematics", [1, 2, 3, 4, 5])

# 5 - Analytics
r5 = st.radio("I like to look at data visually to interpret what it can tell me", [1, 2, 3, 4, 5])

# 6 - Engineering
r6 = st.radio("I enjoy problem solving and trying to find the root cause of an issue", [1, 2, 3, 4, 5])

# 7 - Analytics
r7 = st.radio("I would prefer to focus on the data itself, looking for opportunities to drive business value",
                  [1, 2, 3, 4, 5])

# 8 - Data Science
# r8 = st.radio(
#     "I would prefer to focus on what the data will say in the future, creating hypotheses and testing them",
#     [1, 2, 3, 4, 5])

# 9 - Engineering
r9 = st.radio(
    "I would prefer to focus on the collection and storage of data, thinking how the business can leverage this to drive value",
    [1, 2, 3, 4, 5])

respondent = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
analytical_score = r2+r4+r5+r7
engineering_score = r1+r3+r6+r9
# ds_score = r2+r3+r4+r6+r8

analyst_score_av = round((analytical_score/4),2)
engineer_score_av = round((engineering_score/4),2)
# ds_score_av = round((ds_score/5), 2)

fig = go.Figure(data=[go.Bar(x=['Analyst','Engineer'], y=[analyst_score_av, engineer_score_av])])
fig.update_yaxes(range=[0,5])
st.plotly_chart(fig, use_container_width=True)


skills = ['Software Engineering', 'Pipeline Orchestration', 'Testing & Monitoring', 'Data Architecture', 'Databases', 'Data Visualisation', 
           'Reporting', 'Data Storytelling', 'Statistics', 'Machine Learning', 'Automation', 'Software Engineering']

analyst = [1, 1, 1, 2, 2, 5, 5, 5, 4, 3, 2, 1]
analytics_engineer = [3, 4, 5, 4, 3, 4, 3, 2, 1, 3, 3]
data_engineer = [4, 5, 5, 5, 5, 3, 2, 2, 3, 3, 4]
data_scientist = [5, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5]

fig2 = go.Figure(data=go.Scatterpolar(
      r=analyst,
      theta=skills,
      fill='toself',
      name='Data Analyst'
))

# fig2.add_trace(go.Scatterpolar(
#       r=analytics_engineer,
#       theta=skills,
#       fill='toself',
#       name='Analytics Engineer'
# ))
fig2.add_trace(go.Scatterpolar(
      r=data_engineer,
      theta=skills,
      fill='toself',
      name='Data Engineer'
))

st.plotly_chart(fig2, use_container_width=True)

# print(f"You are {percent_analyst}% analyst, {percent_engineer}% engineer and  {percent_ds}% data scientist!")

# layout = go.Layout(
#     title = 'Overview',
#     xaxis = go.XAxis(
#         showticklabels=False),
# )

# fig = go.Figure(data=go.Scatterpolar(
#       r=respondent_scores,
#       theta=['Analytics','Engineering','Data Science'],
#       fill='toself',
#       name='Data Analyst',
# ))


# fig.update_polars(radialaxis=dict(range=[1, 5]))

# st.plotly_chart(fig, use_container_width=True)



