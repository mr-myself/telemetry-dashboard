import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
from components import charts, metrics, traces, logs
from utils.data_processor import process_telemetry_data

# Page configuration
st.set_page_config(
    page_title="Telemetry Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📊 Telemetry Dashboard")
time_range = st.sidebar.selectbox(
    "Time Range",
    ["Last 15 Minutes", "Last Hour", "Last 24 Hours", "Last 7 Days"]
)

refresh_rate = st.sidebar.selectbox(
    "Refresh Rate",
    ["5 seconds", "30 seconds", "1 minute", "5 minutes"]
)

# Example of how to send your own data
"""
# Replace this example with your actual data source
your_metrics = {
    'avg_response_time': 300.0,
    'response_time_change': 5.0,
    'requests_per_second': 500.0,
    'rps_change': 10.0,
    'error_rate': 0.5,
    'error_rate_change': -0.1
}

your_error_rates_list = [0.6, 0.5, 0.4, 0.5, 0.6, 0.7, 0.6, 0.5, 0.4, 0.3] * 10 #Example data - replace with your actual data
your_error_data = pd.DataFrame({
    'timestamp': pd.date_range(end=datetime.now(), periods=100, freq='1min'),
    'error_rate': your_error_rates_list
})

your_trace_data = pd.DataFrame([
    {'Task': 'Your Task', 'Start': '2024-01-25 12:00:00', 
     'Finish': '2024-01-25 12:00:02', 'Resource': 'Your Service'}
])

timestamps = pd.date_range(end=datetime.now(), periods=100, freq='1min')
log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG'] * 25
services = ['Service A', 'Service B', 'Service C'] * 33
messages = ['Log message 1', 'Log message 2', 'Log message 3'] * 33
your_log_data = pd.DataFrame({
    'timestamp': timestamps,
    'level': log_levels,
    'service': services,
    'message': messages
})

# Process your data
data = process_telemetry_data(
    metrics_data=your_metrics,
    error_data=your_error_data,
    trace_data=your_trace_data,
    log_data=your_log_data
)
"""

# For demonstration, using sample data
data = process_telemetry_data()

# Layout
col1, col2 = st.columns(2)

with col1:
    metrics.display_key_metrics(data['metrics'])

with col2:
    charts.display_error_rate_chart(data['errors'])

# Traces section
st.header("Trace Analysis")
traces.display_trace_timeline(data['traces'])

# Logs section
st.header("System Logs")
logs.display_log_viewer(data['logs'])

# Auto-refresh
st.empty()
st.button("Refresh Data")