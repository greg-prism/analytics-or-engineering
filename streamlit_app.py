import streamlit as st
import plotly.graph_objects as go


def validate(response):
    if (response in ['1', '2', '3', '4', '5']) and (response != None):
        return int(response)
    else:
        print(f"Error: Cannot accept {response} please choose a number between 1 and 5")
        response_new = input()
        validate(response_new)


st.title("Engineering or Analytics?")
st.header("""This quiz is designed to find which aspects of data you most *enjoy* to see which field your
          interests most closely align with""")
st.subheader(""""Please answer the following questions chossing a number from 1-5
                 with 1 being strongly disagree with 5 being strongly agree""")

print('Please answer the following questions chossing a number from 1-5 \nwith 1 being strongly disagree with 5 being strongly agree\n\n')

# 1 - Engineering
r1 = st.selectbox('I enjoy building systems and processes', [1, 2, 3, 4, 5])

# 2 - Analytics
r2 = st.selectbox("I enjoy spotting patterns and trends", [1, 2, 3, 4, 5])

# 3 - Engineering
r3 = st.selectbox("I enjoy optimisng and improving efficiency", [1, 2, 3, 4, 5])

# 4 - Analytics
r4 = st.selectbox("I like to use statistics and mathematics", [1, 2, 3, 4, 5])

# 5 - Analytics
r5 = st.selectbox("I like to look at data visually to interpret what it can tell me", [1, 2, 3, 4, 5])

# 6 - Engineering
r6 = st.selectbox("I enjoy problem solving and trying to find the root cause of an issue", [1, 2, 3, 4, 5])

# 7 - Analytics
r7 = st.selectbox("I would prefer to focus on the data itself, looking for opportunities to drive business value",
                  [1, 2, 3, 4, 5])

# 8 - Data Science
r8 = st.selectbox(
    "I would prefer to focus on what the data will say in the future, creating hypotheses and testing them",
    [1, 2, 3, 4, 5])

# 9 - Engineering
r9 = st.selectbox(
    "I would prefer to focus on the collection and storage of data, thinking how the business can leverage this to drive value",
    [1, 2, 3, 4, 5])

respondent = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
analytical_score = r2+r4+r5+r7
engineering_score = r1+r3+r6+r9
ds_score = r2+r3+r4+r6+r8

analyst_score_av = round((analytical_score/4))
engineer_score_av = round((engineering_score/4))
ds_score_av = round((ds_score/5), 2)

respondent_scores = [analyst_score_av,engineer_score_av,ds_score_av]

# print(f"You are {percent_analyst}% analyst, {percent_engineer}% engineer and  {percent_ds}% data scientist!")

layout = go.Layout(
    title = 'Overview',
    xaxis = go.XAxis(
        showticklabels=False),
)

fig = go.Figure(data=go.Scatterpolar(
      r=respondent_scores,
      theta=['Analytics','Engineering','Data Science'],
      fill='toself',
      name='Data Analyst',
))

fig.update_polars(radialaxis=dict(range=[1, 5]))

st.plotly_chart(fig, use_container_width=True)
