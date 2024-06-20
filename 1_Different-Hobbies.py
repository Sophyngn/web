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

# Bar chart tab content
col1, col2 = st.columns([0.6, 0.4], gap="medium")

# Checkbox to select all options
selected_all = st.checkbox("Select All")

# Define options for multiselect
options = col2.multiselect(
    "Choose your department:",
    ["BCA", "B.com Accounting and Finance ", "Commerce", "B.com ISM"],
)

if selected_all:
    options = ["BCA", "B.com Accounting and Finance ", "Commerce", "B.com ISM"]

# Check if at least one department is selected
with col1:
    if options:
        # Filter the data based on the selected department
        filtered_sp = filtered_sp[filtered_sp['Department'].isin(options)]
        hobbies_counts = filtered_sp['hobbies'].value_counts()
        hobbies_df = hobbies_counts.reset_index()
        hobbies_df.columns = ['Hobbies', 'Count']
    else:
        st.warning("Please select at least one department")

if options:
    fig1 = px.pie(
            hobbies_df,
            names='Hobbies',
            values='Count',
            title='Distribution of Different Hobbies',
            color='Hobbies',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
    fig1.update_layout(
            title={
                'text': 'Distribution of Different Hobbies',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'size': 30}
            },
            font=dict(
                family="Arial, monospace",
                size=14,
                color="RebeccaPurple"
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(
                title='Hobbies',  # Title for the legend
                title_font=dict(size=14),  # Font size for the legend title
                font=dict(size=14),  # Font size for legend labels
                bgcolor='rgba(255, 255, 255, 0.5)',  # Background color of the legend
                bordercolor="RebeccaPurple",  # Border color of the legend
                borderwidth=2,  # Border width of the legend
                itemclick="toggleothers",  # Allow toggling of other legend items on click
                itemdoubleclick="toggle",  # Allow toggling of current legend item on double click
                itemsizing="constant"
            )
        )
    st.plotly_chart(fig1)
