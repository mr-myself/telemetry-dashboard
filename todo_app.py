from flask import Flask, request, jsonify, render_template, redirect, url_for
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

@app.route('/')
def index():
    """Render the main todo page"""
    start_time = datetime.now()
    try:
        send_telemetry("INFO", "Accessing todo homepage")
        return render_template('index.html', todos=todos)
    except Exception as e:
        send_telemetry("ERROR", f"Failed to render homepage: {str(e)}")
        return "Error loading the page", 500
    finally:
        end_time = datetime.now()
        send_trace("Homepage Access", start_time, end_time)

@app.route('/todos', methods=['GET'])
def get_todos():
    """API endpoint to get todos"""
    start_time = datetime.now()
    try:
        send_telemetry("INFO", "Fetching all todos")
        return jsonify(todos)
    except Exception as e:
        send_telemetry("ERROR", f"Failed to fetch todos: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        end_time = datetime.now()
        send_trace("Get Todos", start_time, end_time)

@app.route('/todos', methods=['POST'])
def add_todo():
    """Handle both form submissions and API requests"""
    start_time = datetime.now()
    try:
        if request.is_json:
            # Handle API request
            todo = request.json
            if not todo or 'title' not in todo:
                send_telemetry("WARNING", "Invalid todo data received")
                return jsonify({"error": "Invalid todo data"}), 400
        else:
            # Handle form submission
            title = request.form.get('title')
            if not title:
                send_telemetry("WARNING", "Invalid form submission")
                return "Title is required", 400
            todo = {"title": title}

        todos.append(todo)
        send_telemetry("INFO", f"Added new todo: {todo['title']}")

        # Redirect to homepage for form submissions, return JSON for API requests
        if request.is_json:
            return jsonify(todo), 201
        return redirect(url_for('index'))

    except Exception as e:
        send_telemetry("ERROR", f"Failed to add todo: {str(e)}")
        if request.is_json:
            return jsonify({"error": str(e)}), 500
        return "Error adding todo", 500
    finally:
        end_time = datetime.now()
        send_trace("Add Todo", start_time, end_time)

if __name__ == '__main__':
    print("Starting Todo App...")
    try:
        send_telemetry("INFO", "Todo App starting up")
        app.run(host='0.0.0.0', port=3000, debug=False)  
    except Exception as e:
        print(f"Failed to start Todo App: {e}")