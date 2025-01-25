import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
from datetime import datetime

def display_trace_timeline(trace_data):
    """Display trace timeline visualization"""
    st.subheader("Request Traces")

    if trace_data.empty:
        st.info("No trace data available at the moment.")
        return

    # Convert Start and Finish to datetime and calculate duration
    trace_data = trace_data.copy()
    trace_data['Start'] = pd.to_datetime(trace_data['Start'])
    trace_data['Finish'] = pd.to_datetime(trace_data['Finish'])
    trace_data['Duration'] = (trace_data['Finish'] - trace_data['Start']).dt.total_seconds()

    # Create color mapping for unique tasks
    colors = {'API Request': '#FF4B4B', 'Database Query': '#1F77B4', 'Cache Operation': '#2CA02C'}

    # Create Gantt chart for traces
    if len(trace_data) > 0:
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

        # Trace details with formatted duration
        with st.expander("Trace Details"):
            display_df = trace_data.copy()
            display_df['Duration'] = display_df['Duration'].apply(lambda x: f"{x:.2f}s")
            st.dataframe(
                display_df[['Task', 'Start', 'Finish', 'Resource', 'Duration']],
                use_container_width=True
            )