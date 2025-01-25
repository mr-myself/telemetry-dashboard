# 📊 Telemetry Dashboard with Todo App Integration

A comprehensive telemetry visualization dashboard that enables real-time monitoring and analysis of system metrics and logs, integrated with a Todo application for demonstration purposes.

## 🎯 Overview

This project combines a powerful telemetry dashboard with a sample Todo application to showcase real-world monitoring capabilities. The system consists of three main components:

1. **Telemetry Dashboard**: A Streamlit-based dashboard providing real-time insights into system performance
2. **Collector Service**: A FastAPI service that collects and processes telemetry data
3. **Todo Application**: A sample Flask application demonstrating real-world monitoring integration

## 📸 Screenshots

### Telemetry Dashboard
[Add screenshot showing the telemetry dashboard with metrics, traces, and logs sections]
*Screenshot showing real-time metrics, performance charts, and system logs*

### Todo Application
[Add screenshot of the Todo application interface]
*Screenshot showing the Todo app with form and list interface*

## 🚀 Key Features

### Telemetry Dashboard
- Real-time performance metrics visualization
- Interactive charts using Plotly
- System log viewer with advanced filtering
- Request trace analysis with timeline view
- Customizable refresh rates (5s to 5m)
- Dark mode UI with responsive design

### Todo Application
- Create and manage todos
- Real-time performance monitoring
- Error tracking and logging
- Request tracing
- RESTful API endpoints

## 🛠 Technical Stack

### Dashboard Components
- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas
- **Styling**: Custom CSS

### Todo App
- **Framework**: Flask
- **Template Engine**: Jinja2
- **API**: RESTful endpoints

### Telemetry Collector
- **Framework**: FastAPI
- **Data Models**: Pydantic
- **API**: RESTful endpoints

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/mr-myself/telemetry-dashboard.git
cd telemetry-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Running the Applications

1. Start the Collector Service:
```bash
python collector_service.py
```
The collector service will run on http://localhost:8000

2. Start the Todo App:
```bash
python todo_app.py
```
The Todo app will be available at http://localhost:3000

3. Launch the Dashboard:
```bash
streamlit run main.py
```
The dashboard will be accessible at http://localhost:5000

## 📖 Usage Guide

### Telemetry Dashboard

1. **Time Range Selection**
   - Use the sidebar to select your preferred time range
   - Options: Last 15 Minutes, Last Hour, Last 24 Hours, Last 7 Days

2. **Refresh Rate**
   - Choose how often the dashboard updates
   - Options: 5 seconds, 30 seconds, 1 minute, 5 minutes

3. **Key Metrics**
   - View essential performance indicators
   - Monitor response times, request rates, and error rates

4. **Trace Analysis**
   - Analyze request traces with timeline visualization
   - Track request durations and dependencies

5. **Log Viewer**
   - Filter logs by level and search terms
   - Real-time log updates

### Todo Application

1. **Adding Todos**
   - Enter todo text in the input field
   - Click "Add Todo" or press Enter

2. **Viewing Todos**
   - See all todos in a clean list interface
   - Monitor performance metrics in the dashboard

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualization powered by [Plotly](https://plotly.com/)
- FastAPI for efficient API development
- Flask for the sample application