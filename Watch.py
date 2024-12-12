import streamlit as st
import pandas as pd
import os   #realtive Paths for Github 

# Configure the Streamlit app page
st.set_page_config(
    page_title="Watch Investment App",  # Title displayed in the browser tab
    layout="centered",  # Centers the app layout
    menu_items={  # Customize the app menu
        'Get Help': None,  # Hides the "Get Help" option
        'Report a bug': None,  # Hides the "Report a bug" option
        'About': "This is a Watch Investment Application built with Streamlit."  # Adds a description for the app
    }
)

# Import functions for each page
from page1_questionnaire import questionnaire
from page2_recommendations import recommend_watches
from page3_watch_detail import watch_detail
from page4_investment_calculator import investment_calculator

# Initialize session state variables for app navigation and data persistence
if 'page' not in st.session_state:
    st.session_state['page'] = 'Questionnaire'  # Default page is the Questionnaire
if 'questionnaire_complete' not in st.session_state:
    st.session_state['questionnaire_complete'] = False  # Tracks if the questionnaire has been completed
if 'selected_watch' not in st.session_state:
    st.session_state['selected_watch'] = None  # Stores details of the selected watch
if 'watches_data' not in st.session_state:
    st.session_state['watches_data'] = None  # Placeholder for the loaded CSV data

# Function to load CSV data containing watch information
def load_csv_data():
    file_path_watchdata = os.path.join('watchdata5.csv')  # Path to the CSV file 
    
    try:
        # Read the CSV file and store it in the session state
        st.session_state['watches_data'] = pd.read_csv(file_path_watchdata, quotechar='"', delimiter=',')
    except FileNotFoundError:  # Handle case where the file is missing
        st.error(f"File not found: {file_path_watchdata}. Please ensure the file exists.")
        st.stop()  # Stop app execution if the file is not found

# Function to navigate between pages
def navigate_to(page_name, message=None):
    if message:  # Optional message displayed when navigation occurs
        st.info(message)
    st.session_state['page'] = page_name  # Update the current page in the session state
    st.rerun()  # Refresh the app to load the new page

# Ensure the CSV data is loaded before proceeding
if st.session_state['watches_data'] is None:
    load_csv_data()  # Load the data if it hasn't been loaded already

# Dynamically control which page is displayed based on the session state
if st.session_state['page'] == 'Questionnaire':
    questionnaire()  # Display the Questionnaire page
    if st.session_state['questionnaire_complete']:  # Check if the questionnaire was completed
        navigate_to('Recommendations', "Questionnaire complete. Proceeding to Recommendations.")  # Navigate to Recommendations

elif st.session_state['page'] == 'Recommendations':
    recommend_watches()  # Display the Recommendations page

elif st.session_state['page'] == 'Watch Details':
    if st.session_state['selected_watch']:  # Ensure a watch is selected
        watch_detail()  # Display the Watch Details page
    else:  # If no watch is selected, navigate back to Recommendations
        st.warning("No watch selected. Redirecting to Recommendations...")
        navigate_to('Recommendations')

elif st.session_state['page'] == 'Investment Calculator':
    if st.session_state['selected_watch']:  # Ensure a watch is selected
        investment_calculator()  # Display the Investment Calculator page
    else:  # If no watch is selected, navigate back to Recommendations
        st.warning("No watch selected. Redirecting to Recommendations...")
        navigate_to('Recommendations')

else:
    # Handle invalid pages by navigating to the Questionnaire page
    st.error("Page not found. Redirecting to Questionnaire...")
    navigate_to('Questionnaire')

# Add buttons for quick navigation between pages
st.write("---")  # Add a horizontal separator
col1, col2, col3, col4 = st.columns(4)  # Create a 4-column layout for navigation buttons

# Button to navigate to the Questionnaire page
with col1:
    if st.button("Questionnaire"):
        navigate_to('Questionnaire')

# Button to navigate to the Recommendations page
with col2:
    if st.button("Recommendations"):
        navigate_to('Recommendations')

# Button to navigate to the Watch Details page
with col3:
    if st.button("Watch Details"):
        if st.session_state['selected_watch']:  # Only allow navigation if a watch is selected
            navigate_to('Watch Details')
        else:
            st.warning("No watch selected.")  # Warn the user if no watch is selected

# Button to navigate to the Investment Calculator page
with col4:
    if st.button("Investment Calculator"):
        if st.session_state['selected_watch']:  # Only allow navigation if a watch is selected
            navigate_to('Investment Calculator')
        else:
            st.warning("No watch selected.")  # Warn the user if no watch is selected




# 	•	Sources:
# 	•	Streamlit Documentation: The layout, page navigation, and session state handling were largely based on examples from the Streamlit documentation: https://docs.streamlit.io/develop/api-reference/layout
# 	•	GitHub Projects: Ideas for creating multi-page apps were inspired by open-source Streamlit projects on GitHub: https://stackoverflow.com/questions/78677719/streamlit-how-to-navigate-to-a-page-directly-after-file-uploader
# 	•	ChatGPT: ChatGPT contributed by suggesting enhancements to the app’s navigation logic and identifying edge cases for better error handling.
