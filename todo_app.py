from flask import Flask, request, jsonify
import requests
from datetime import datetime
import time

app = Flask(__name__)

# In-memory storage for todos
todos = []

# Collector service URL
COLLECTOR_URL = "http://localhost:8000"

def send_telemetry(log_level, message, service="todo_app"):
    """Send log data to collector"""
    try:
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "level": log_level,
            "service": service,
            "message": message
        }
        requests.post(f"{COLLECTOR_URL}/telemetry/logs", json=log_data, timeout=5)
    except Exception as e:
        print(f"Failed to send log: {e}")

def send_trace(task_name, start_time, end_time):
    """Send trace data to collector"""
    try:
        trace_data = {
            "Task": task_name,
            "Start": start_time.isoformat(),
            "Finish": end_time.isoformat(),
            "Resource": "TodoAPI"
        }
        requests.post(f"{COLLECTOR_URL}/telemetry/traces", json=trace_data, timeout=5)
    except Exception as e:
        print(f"Failed to send trace: {e}")

@app.route('/todos', methods=['GET'])
def get_todos():
    start_time = datetime.now()
    try:
        send_telemetry("INFO", "Fetching all todos")
        response = jsonify(todos)
        send_telemetry("INFO", f"Successfully fetched {len(todos)} todos")
        return response
    except Exception as e:
        send_telemetry("ERROR", f"Failed to fetch todos: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        end_time = datetime.now()
        send_trace("Get Todos", start_time, end_time)

@app.route('/todos', methods=['POST'])
def add_todo():
    start_time = datetime.now()
    try:
        todo = request.json
        if not todo or 'title' not in todo:
            send_telemetry("WARNING", "Invalid todo data received")
            return jsonify({"error": "Invalid todo data"}), 400

        todos.append(todo)
        send_telemetry("INFO", f"Added new todo: {todo['title']}")
        return jsonify(todo), 201
    except Exception as e:
        send_telemetry("ERROR", f"Failed to add todo: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        end_time = datetime.now()
        send_trace("Add Todo", start_time, end_time)

if __name__ == '__main__':
    print("Starting Todo App...")
    try:
        send_telemetry("INFO", "Todo App starting up")
        app.run(host='0.0.0.0', port=3000, debug=True)
    except Exception as e:
        print(f"Failed to start Todo App: {e}")