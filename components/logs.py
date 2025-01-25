import streamlit as st
import pandas as pd

def display_log_viewer(logs_data):
    """Display log viewer with search and filter capabilities"""
    # Log level filter
    log_levels = ['ALL'] + sorted(logs_data['level'].unique().tolist())
    selected_level = st.selectbox('Log Level', log_levels)
    
    # Search box
    search_term = st.text_input('Search Logs', '')
    
    # Filter logs based on selections
    filtered_logs = logs_data
    if selected_level != 'ALL':
        filtered_logs = filtered_logs[filtered_logs['level'] == selected_level]
    
    if search_term:
        filtered_logs = filtered_logs[
            filtered_logs['message'].str.contains(search_term, case=False) |
            filtered_logs['service'].str.contains(search_term, case=False)
        ]
    
    # Display logs in a scrollable container
    st.dataframe(
        filtered_logs,
        use_container_width=True,
        height=400
    )
