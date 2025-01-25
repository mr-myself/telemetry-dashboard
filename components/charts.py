import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def display_error_rate_chart(error_data):
    """Display error rate chart using Plotly"""
    fig = px.line(
        error_data,
        x='timestamp',
        y='error_rate',
        title='Error Rate Over Time'
    )
    
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Time",
        yaxis_title="Error Rate (%)",
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_performance_chart(perf_data):
    """Create performance metrics chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=perf_data['timestamp'],
        y=perf_data['response_time'],
        name='Response Time',
        line=dict(color='#FF4B4B')
    ))
    
    fig.update_layout(
        template="plotly_dark",
        title="System Performance",
        xaxis_title="Time",
        yaxis_title="Response Time (ms)",
        showlegend=True
    )
    
    return fig
