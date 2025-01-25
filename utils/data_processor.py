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
            if not metrics_data:
                metrics_data = {
                    'avg_response_time': 0.0,
                    'response_time_change': 0.0,
                    'requests_per_second': 0.0,
                    'rps_change': 0.0,
                    'error_rate': 0.0,
                    'error_rate_change': 0.0
                }

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
                log_data = log_data.sort_values('timestamp', ascending=False)

            return {
                'metrics': metrics_data,
                'errors': error_data if not error_data.empty else pd.DataFrame({'timestamp': [], 'error_rate': []}),
                'traces': trace_data if not trace_data.empty else pd.DataFrame({'Task': [], 'Start': [], 'Finish': [], 'Resource': []}),
                'logs': log_data if not log_data.empty else pd.DataFrame({'timestamp': [], 'level': [], 'service': [], 'message': []})
            }

        return None
    except requests.exceptions.RequestException:
        return None

def process_telemetry_data(metrics_data=None, error_data=None, trace_data=None, log_data=None):
    """
    Process telemetry data for the dashboard.
    This function is kept for backwards compatibility but should not be used directly.
    Use fetch_telemetry_data() instead.
    """
    return fetch_telemetry_data() or {
        'metrics': metrics_data or {},
        'errors': error_data if error_data is not None else pd.DataFrame(),
        'traces': trace_data if trace_data is not None else pd.DataFrame(),
        'logs': log_data if log_data is not None else pd.DataFrame()
    }

# Keep the generate_sample_data function for demonstration
def generate_sample_data():
    """Generate sample telemetry data for demonstration"""
    return process_telemetry_data()