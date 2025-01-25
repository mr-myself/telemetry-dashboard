from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
import pandas as pd

app = FastAPI()

# In-memory storage for demonstration
telemetry_store = {
    'metrics': {},
    'errors': [],
    'traces': [],
    'logs': []
}

# Data models
class Metrics(BaseModel):
    avg_response_time: float
    response_time_change: float
    requests_per_second: float
    rps_change: float
    error_rate: float
    error_rate_change: float

class ErrorData(BaseModel):
    timestamp: datetime
    error_rate: float

class TraceData(BaseModel):
    Task: str
    Start: datetime
    Finish: datetime
    Resource: str

class LogEntry(BaseModel):
    timestamp: datetime
    level: str
    service: str
    message: str

# Endpoints for receiving telemetry data
@app.post("/telemetry/metrics")
async def update_metrics(metrics: Metrics):
    telemetry_store['metrics'] = metrics.dict()
    return {"status": "success"}

@app.post("/telemetry/errors")
async def add_error_data(error: ErrorData):
    telemetry_store['errors'].append(error.dict())
    # Keep only last 100 entries
    telemetry_store['errors'] = telemetry_store['errors'][-100:]
    return {"status": "success"}

@app.post("/telemetry/traces")
async def add_trace(trace: TraceData):
    telemetry_store['traces'].append(trace.dict())
    # Keep only last 100 traces
    telemetry_store['traces'] = telemetry_store['traces'][-100:]
    return {"status": "success"}

@app.post("/telemetry/logs")
async def add_log(log: LogEntry):
    telemetry_store['logs'].append(log.dict())
    # Keep only last 100 logs
    telemetry_store['logs'] = telemetry_store['logs'][-100:]
    return {"status": "success"}

# Endpoints for retrieving telemetry data
@app.get("/telemetry/all")
async def get_all_telemetry():
    return {
        'metrics': telemetry_store['metrics'],
        'errors': pd.DataFrame(telemetry_store['errors']).to_dict('records') if telemetry_store['errors'] else [],
        'traces': pd.DataFrame(telemetry_store['traces']).to_dict('records') if telemetry_store['traces'] else [],
        'logs': pd.DataFrame(telemetry_store['logs']).to_dict('records') if telemetry_store['logs'] else []
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
