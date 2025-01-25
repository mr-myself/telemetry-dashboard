# Telemetry Dashboard with Todo App Integration

A comprehensive telemetry visualization dashboard that enables real-time monitoring and analysis of system metrics and logs, integrated with a Todo application for demonstration purposes.

## 📊 Telemetry Dashboard

A real-time monitoring solution that provides insights into system performance, error rates, and application behavior.

### Key Features
- Real-time metrics visualization
- Interactive performance charts
- System log viewer with filtering capabilities
- Request trace analysis
- Customizable refresh rates
- Dark mode interface

### Screenshots
[Dashboard Screenshot Here]
*Screenshot showing the telemetry dashboard with metrics, traces, and logs sections*

## ✅ Todo Application

A sample application integrated with the telemetry system to demonstrate real-world monitoring capabilities.

### Key Features
- Create and manage todos
- Real-time telemetry data collection
- Performance monitoring
- Error tracking
- Request tracing

### Screenshots
[Todo App Screenshot Here]
*Screenshot showing the Todo application interface*

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
This will start the collector service on port 8000.

2. Start the Todo App:
```bash
python todo_app.py
```
The Todo app will be available at http://localhost:3000

3. Start the Dashboard:
```bash
streamlit run main.py
```
The dashboard will be accessible at http://localhost:5000

## 🔍 Usage

### Telemetry Dashboard
- Select time range from the sidebar
- Choose refresh rate for real-time updates
- View system metrics in the top cards
- Analyze error rates and performance in the charts
- Explore request traces in the timeline view
- Filter and search logs in the log viewer

### Todo App
- Access the Todo app interface
- Add new todos using the form
- View the list of todos
- Monitor the application's performance in the dashboard

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
