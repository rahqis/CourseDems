# Strealit and compilation of other files to create final product and design
import streamlit as st
import pandas as pd
import plotly.express as px
from Colleges import unc

mainTitle = st.title("Course Demographics")
mainHooker = st.header("Curious to know the demographics of your classes?")
mainExplain = st.subheader(
    "Look at the classes offered for your colleges, and view the racial and gender breakdown of your classes.")

top = st.sidebar.header("Course Selection")

collegeDropDown = st.sidebar.selectbox('Colleges',
                                       ['Select College', 'Duke', 'North Carolina State University', 'University of North Carolina at Chapel Hill', 'University of North Carolina at Charlotte'])


genderLabels = ['male', 'female', 'perfer not to say', 'other']
raceLabels = ['White/Caucasian', 'Asian/Pacific-Islander', 'Hispanic/Latinx',
              'American Indian or Pacific Islander', 'Black', 'MENA', 'Other']

course = ""

if collegeDropDown == "Duke":
    course = st.sidebar.selectbox("Courses", [])
    if course == None:
        st.sidebar.write(
            'It seems like no courses have been reported. More data coming soon!')

if collegeDropDown == "North Carolina State University":
    course = st.sidebar.selectbox("Courses", [])

if collegeDropDown == "University of North Carolina at Chapel Hill":
    course = st.sidebar.selectbox("Courses", ['ENGL105'])

if collegeDropDown == "University of North Carolina at Charlotte":
    course = st.sidebar.selectbox("Courses", [])
    if course == None:
        st.sidebar.write(
            'It seems like no courses have been reported. More data coming soon!')

if course != None and course != "":
    explode = []
    courseGender = unc.gender(course)
    GenVs = []
    for v in courseGender.values():
        GenVs.append(v)
    GenLabels = []
    for k in courseGender.keys():
        GenLabels.append(k)
    for i in range(len(GenLabels)):
        explode.append(0)
    genderDF = pd.DataFrame({'Gender': GenLabels, 'Percentages': GenVs})
    fig = px.pie(genderDF, values='Percentages', names='Gender')
    st.plotly_chart(fig)
