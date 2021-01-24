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

uncCourse = ['ENGL 105', 'COMP 210', 'COMP 211', 'COMP 301',
             'MATH 381', 'CHEM 241', 'BIOL 202', 'CHEM 101']


if collegeDropDown == "Duke":
    course = st.sidebar.selectbox("Courses", [])
    if course == None:
        st.sidebar.write(
            'It seems like no courses have been reported. More data coming soon!')

if collegeDropDown == "North Carolina State University":
    course = st.sidebar.selectbox("Courses", [])
    if course == None:
        st.sidebar.write(
            'It seems like no courses have been reported. More data coming soon!')

if collegeDropDown == "University of North Carolina at Chapel Hill":
    course = st.sidebar.selectbox("Courses", uncCourse)

if collegeDropDown == "University of North Carolina at Charlotte":
    course = st.sidebar.selectbox("Courses", [])
    if course == None:
        st.sidebar.write(
            'It seems like no courses have been reported. More data coming soon!')

if course != None and course != "":
    courseGender = unc.gender(course)
    courseRace = unc.specific_race(course)
    GenVs = []
    for v in courseGender.values():
        GenVs.append(v)
    GenLabels = []
    for k in courseGender.keys():
        GenLabels.append(k)
    genderDF = pd.DataFrame({'Gender': GenLabels, 'Percentages': GenVs})
    figGen = px.pie(genderDF, values='Percentages', names='Gender')
    st.subheader("Gender Breakdown for " + course)
    st.plotly_chart(figGen)

    RaceVs = []
    for v in courseRace.values():
        RaceVs.append(v)
    RaceLabs = []
    for k in courseRace.keys():
        RaceLabs.append(k)
    raceDF = pd.DataFrame({'Race': RaceLabs, 'Percentages': RaceVs})
    figRace = px.pie(raceDF, values='Percentages', names='Race')
    st.subheader("Racial Breakdown for " + course)
    st.plotly_chart(figRace)

