# Strealit and compilation of other files to create final product and design
import streamlit as st
from Colleges import duke

mainTitle = st.title("Course Demographics")
mainHooker = st.header("Curious to know the demographics of your classes?")
mainExplain = st.subheader(
    "Look at the classes offered for your colleges, and view the racial and gender breakdown of your classes.")

top = st.sidebar.header("Course Selection")

collegeDropDown = st.sidebar.selectbox('Colleges',
                                       ['Select College', 'Duke', 'North Carolina State University', 'University of North Carolina at Chapel Hill', 'University of North Carolina at Charlotte'])

course = ""

if collegeDropDown == "Duke":
    course = st.sidebar.selectbox("Courses", [])

if collegeDropDown == "North Carolina State University":
    course = st.sidebar.selectbox("Courses", [])

if collegeDropDown == "University of North Carolina at Chapel Hill":
    course = st.sidebar.selectbox("Courses", [])

if collegeDropDown == "University of North Carolina at Charlotte":
    course = st.sidebar.selectbox("Courses", [])
