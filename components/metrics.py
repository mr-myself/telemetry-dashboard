import streamlit as st

def display_key_metrics(metrics_data):
    """Display key performance metrics"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Average Response Time",
            value=f"{metrics_data['avg_response_time']:.2f}ms",
            delta=f"{metrics_data['response_time_change']:.1f}ms"
        )
    
    with col2:
        st.metric(
            label="Requests/Second",
            value=f"{metrics_data['requests_per_second']:.1f}",
            delta=f"{metrics_data['rps_change']:.1f}"
        )
    
    with col3:
        st.metric(
            label="Error Rate",
            value=f"{metrics_data['error_rate']:.2f}%",
            delta=f"{metrics_data['error_rate_change']:.2f}%",
            delta_color="inverse"
        )
