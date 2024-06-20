import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
# Load the dataset with appropriate encoding handling
try:
    sp = pd.read_csv('/Users/vankhanh/Downloads/Student_Attitude_and_Behavior.csv')
except UnicodeDecodeError:
    sp = pd.read_csv('/Users/vankhanh/Downloads/Students_Attitude_and_Behavior.csv', encoding='ISO-8859-1')

# Set page config
apptitle = 'Student Attitude and Behavior'
st.set_page_config(layout="wide", page_title=apptitle, page_icon=":👩‍🎓:")

with st.sidebar:
    st.write('**🔎 Reporting to Dr. Tan Duc Do**')
    st.write("Date: ", datetime.date(2024, 5, 29))
    st.text("Description: \n This serves as an illustration \n for an Interactive Web Application \n for Python Project 2.")

st.markdown("""
    <style>
    .stApp {
        background-color: #f3f3f3;
        color: #333333;
    }
    .sidebar .sidebar-content {
        background-color: #1e90ff;
        color:#ffffff;
    }
    .sidebar .sidebar-content h2 {
        color: #2c3e50;
    }
    .sidebar .sidebar-content .stText {
        color: #2c3e50;
    }
    # .st-bb {
    #     background-color: #ffffff;
    # }
    # .st-at {
    #     background-color: #ffffff;
    # }
    </style>
    """, unsafe_allow_html=True)


st.write('**🔎 Group 6 Business IT 2 Members:**')
st.write('Nguyen Thien Van Khanh 👩🏻')
st.write('Nguyenn Thi Tra Khoi 👩🏻')


st.title("Lorem ipsum")
st.write("***" ) 
    # st.image(r"C:\Users\XPS\Desktop\sidebar1.jpg")

with st.container():
    st.write("---")
    left_column, right_column = st.columns([3, 1])  # Adjust the ratio here
    st.link_button("Where did we find dataset? 💯", "https://www.kaggle.com/datasets/susanta21/student-attitude-and-behavior")
    
    # Toggle switch to show/hide DataFrame
    if st.toggle("Show Data Frame"):
        st.dataframe(data=sp[['Certification Course', 'Gender', 'Department', 'Height(CM)', 'Weight(KG)', '10th Mark', '12th Mark', 'college mark', 'hobbies', 'Daily studying time', 'prefer to study in', 'salary expectation', 'Do you like your degree?', 'willingness to pursue a career based on their degree  ', 'social medai & video', 'Travelling Time ']], width=1500, use_container_width=True)
        