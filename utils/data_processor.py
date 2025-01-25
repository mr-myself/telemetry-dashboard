import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def process_telemetry_data(metrics_data=None, error_data=None, trace_data=None, log_data=None):
    """
    Process external telemetry data for the dashboard.

    Parameters:
    -----------
    metrics_data : dict
        Dictionary containing current metrics:
        {
            'avg_response_time': float,
            'response_time_change': float,
            'requests_per_second': float,
            'rps_change': float,
            'error_rate': float,
            'error_rate_change': float
        }

    error_data : pandas.DataFrame
        DataFrame with columns: ['timestamp', 'error_rate']

    trace_data : pandas.DataFrame
        DataFrame with columns: ['Task', 'Start', 'Finish', 'Resource']

    log_data : pandas.DataFrame
        DataFrame with columns: ['timestamp', 'level', 'service', 'message']

    Returns:
    --------
    dict : Processed data ready for dashboard display
    """
    now = datetime.now()

    # Process metrics data
    if metrics_data is None:
        metrics_data = {
            'avg_response_time': 250.5,
            'response_time_change': -12.3,
            'requests_per_second': 458.2,
            'rps_change': 23.5,
            'error_rate': 1.2,
            'error_rate_change': -0.3
        }

    # Process error data
    if error_data is None:
        timestamps = pd.date_range(end=now, periods=100, freq='1min')
        error_data = pd.DataFrame({
            'timestamp': timestamps,
            'error_rate': np.random.normal(1.5, 0.5, len(timestamps))
        })

    # Process trace data
    if trace_data is None:
        trace_data = pd.DataFrame([
            dict(Task='API Request', Start='2023-01-01 12:00:00', Finish='2023-01-01 12:00:02', Resource='Gateway'),
            dict(Task='Database Query', Start='2023-01-01 12:00:02', Finish='2023-01-01 12:00:04', Resource='Database'),
            dict(Task='Cache Operation', Start='2023-01-01 12:00:04', Finish='2023-01-01 12:00:05', Resource='Cache')
        ])

    # Process logs data
    if log_data is None:
        timestamps = pd.date_range(end=now, periods=100, freq='1min')
        log_data = pd.DataFrame({
            'timestamp': timestamps,
            'level': np.random.choice(['INFO', 'WARNING', 'ERROR'], size=len(timestamps)),
            'service': np.random.choice(['api', 'database', 'cache'], size=len(timestamps)),
            'message': [f'Sample log message {i}' for i in range(len(timestamps))]
        })

    return {
        'metrics': metrics_data,
        'errors': error_data,
        'traces': trace_data,
        'logs': log_data
    }

# Keep the generate_sample_data function for demonstration
def generate_sample_data():
    """Generate sample telemetry data for demonstration"""
    return process_telemetry_data()