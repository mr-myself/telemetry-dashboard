import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

def display_trace_timeline(trace_data):
    """Display trace timeline visualization"""
    st.subheader("Request Traces")

    # Create color mapping based on unique tasks
    unique_tasks = trace_data['Task'].unique()
    colors = {'API Request': '#FF4B4B', 'Database Query': '#1F77B4', 'Cache Operation': '#2CA02C'}

    # Create Gantt chart for traces
    fig = ff.create_gantt(
        trace_data,
        colors=colors,
        group_tasks=True,
        showgrid_x=True,
        showgrid_y=True,
        index_col='Task'
    )

    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # Trace details
    with st.expander("Trace Details"):
        st.dataframe(
            trace_data[['Task', 'Start', 'Finish', 'Resource', 'Duration']],
            use_container_width=True
        )