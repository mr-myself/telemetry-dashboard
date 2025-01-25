import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_data():
    """Generate sample telemetry data for demonstration"""
    now = datetime.now()
    timestamps = pd.date_range(end=now, periods=100, freq='1min')
    
    # Generate metrics data
    metrics = {
        'avg_response_time': 250.5,
        'response_time_change': -12.3,
        'requests_per_second': 458.2,
        'rps_change': 23.5,
        'error_rate': 1.2,
        'error_rate_change': -0.3
    }
    
    # Generate error rate data
    errors = pd.DataFrame({
        'timestamp': timestamps,
        'error_rate': np.random.normal(1.5, 0.5, len(timestamps))
    })
    
    # Generate trace data
    traces = pd.DataFrame([
        dict(Task='API Request', Start='2023-01-01 12:00:00', Finish='2023-01-01 12:00:02', Resource='Gateway'),
        dict(Task='Database Query', Start='2023-01-01 12:00:02', Finish='2023-01-01 12:00:04', Resource='Database'),
        dict(Task='Cache Operation', Start='2023-01-01 12:00:04', Finish='2023-01-01 12:00:05', Resource='Cache')
    ])
    
    # Generate logs data
    logs = pd.DataFrame({
        'timestamp': timestamps,
        'level': np.random.choice(['INFO', 'WARNING', 'ERROR'], size=len(timestamps)),
        'service': np.random.choice(['api', 'database', 'cache'], size=len(timestamps)),
        'message': [f'Sample log message {i}' for i in range(len(timestamps))]
    })
    
    return {
        'metrics': metrics,
        'errors': errors,
        'traces': traces,
        'logs': logs
    }
