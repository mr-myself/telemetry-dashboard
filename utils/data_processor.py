import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

COLLECTOR_URL = "http://localhost:8000"

def fetch_telemetry_data():
    """
    Fetch telemetry data from the collector service
    """
    try:
        response = requests.get(f"{COLLECTOR_URL}/telemetry/all")
        if response.status_code == 200:
            data = response.json()

            # Convert data to appropriate formats
            metrics_data = data.get('metrics', {})

            error_data = pd.DataFrame(data.get('errors', []))
            if not error_data.empty:
                error_data['timestamp'] = pd.to_datetime(error_data['timestamp'])

            trace_data = pd.DataFrame(data.get('traces', []))
            if not trace_data.empty:
                trace_data['Start'] = pd.to_datetime(trace_data['Start'])
                trace_data['Finish'] = pd.to_datetime(trace_data['Finish'])

            log_data = pd.DataFrame(data.get('logs', []))
            if not log_data.empty:
                log_data['timestamp'] = pd.to_datetime(log_data['timestamp'])

            return process_telemetry_data(
                metrics_data=metrics_data,
                error_data=error_data,
                trace_data=trace_data,
                log_data=log_data
            )
    except requests.exceptions.RequestException:
        # Return sample data if collector is not available
        return process_telemetry_data()

def process_telemetry_data(metrics_data=None, error_data=None, trace_data=None, log_data=None):
    """
    Process telemetry data for the dashboard.
    """
    now = datetime.now()

    # Process metrics data
    if metrics_data is None or not metrics_data:
        metrics_data = {
            'avg_response_time': 250.5,
            'response_time_change': -12.3,
            'requests_per_second': 458.2,
            'rps_change': 23.5,
            'error_rate': 1.2,
            'error_rate_change': -0.3
        }

    # Process error data
    if error_data is None or error_data.empty:
        timestamps = pd.date_range(end=now, periods=100, freq='1min')
        error_data = pd.DataFrame({
            'timestamp': timestamps,
            'error_rate': np.random.normal(1.5, 0.5, len(timestamps))
        })

    # Process trace data
    if trace_data is None or trace_data.empty:
        trace_data = pd.DataFrame([
            dict(Task='API Request', Start='2023-01-01 12:00:00', Finish='2023-01-01 12:00:02', Resource='Gateway'),
            dict(Task='Database Query', Start='2023-01-01 12:00:02', Finish='2023-01-01 12:00:04', Resource='Database'),
            dict(Task='Cache Operation', Start='2023-01-01 12:00:04', Finish='2023-01-01 12:00:05', Resource='Cache')
        ])

    # Process logs data
    if log_data is None or log_data.empty:
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