import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset with appropriate encoding handling
try:
    sp = pd.read_csv('/Users/vankhanh/Downloads/Student_Attitude_and_Behavior.csv')
except UnicodeDecodeError:
    sp = pd.read_csv('/Users/vankhanh/Downloads/Students_Attitude_and_Behavior.csv', encoding='ISO-8859-1')

# Set page config
apptitle = 'Student Attitude and Behavior'
st.set_page_config(layout="wide", page_title=apptitle, page_icon="👩‍🎓")

# Sidebar Gender selection
selected_gender = st.sidebar.radio("Gender 👨/👩", ('All', *sp['Gender'].unique()), key='Gender')

# Filtering data based on selected gender
if selected_gender == 'All':
    filtered_sp = sp
else:
    filtered_sp = sp[sp['Gender'] == selected_gender]

st.header("Distribution of Marks")
col1, col2 = st.columns([0.7, 0.3], gap="medium")

    
with col1:
        # Add a selectbox to choose between 10th Mark and 12th Mark
        mark_options = ["10th Mark", "12th Mark", "College mark"]
        selected_mark = st.selectbox("Types of mark:", options=mark_options)
    
with col2:
        selected_daily = st.radio("Daily studying time", ('All', *sp['Daily studying time'].unique()), key='Daily studying time')
        if selected_daily == 'All':
            filtered_daily = sp
        else:
            filtered_daily = sp[sp['Daily studying time'] == selected_daily]
        if selected_gender == 'All' and selected_daily == 'All':
            filtered_data = sp
        elif selected_gender == 'All':
            filtered_data = sp[sp['Daily studying time'] == selected_daily]
        elif selected_daily == 'All':
            filtered_data = sp[sp['Gender'] == selected_gender]
        else:
            filtered_data = sp[(sp['Gender'] == selected_gender) & (sp['Daily studying time'] == selected_daily)]

    # Add 2 columns
col1, col2 = st.columns([0.55, 0.45])  # Adjust the ratio here

with col1:
        # Create histogram chart with marks
        fig2 = px.histogram(filtered_data, x=selected_mark, nbins=10, title=f'Distribution of {selected_mark} stress level', labels={selected_mark: selected_mark, 'count': 'Frequency'}, color_discrete_sequence=['skyblue'])
        fig2.update_layout(xaxis_title=selected_mark, yaxis_title='Frequency', bargap=0.1)
        # Update histogram font and background
        fig2.update_traces(marker=dict(color='rgba(55, 128, 191, 0.7)', line=dict(color='rgba(0,0,0,0.5)', width=0.5)))

        # Update layout background color and font
        fig2.update_layout(
            font=dict(family="Arial", size=12, color="RebeccaPurple"),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        
        st.plotly_chart(fig2)

with col2:
        # Calculate average mark based on 10th and 12th marks
        filtered_data['Average Mark'] = (filtered_data['10th Mark'] + filtered_data['12th Mark'] + filtered_data['college mark'] ) / 3

        # Create violin chart with average mark
        fig3 = px.box(filtered_data, y="Average Mark", points="all", title="Violin Plot of Average Marks", hover_data=["10th Mark", "12th Mark"])
        st.plotly_chart(fig3)
        