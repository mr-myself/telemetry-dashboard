import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
from components import charts, metrics, traces, logs
from utils.data_processor import fetch_telemetry_data
import time #Import time module for sleep function


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

# Fetch real telemetry data
data = fetch_telemetry_data()

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

# Auto-refresh based on selected rate
refresh_seconds = {
    "5 seconds": 5,
    "30 seconds": 30,
    "1 minute": 60,
    "5 minutes": 300
}[refresh_rate]

# Add auto-refresh using Streamlit's automatic rerun
st.empty()
time.sleep(refresh_seconds)
st.experimental_rerun()