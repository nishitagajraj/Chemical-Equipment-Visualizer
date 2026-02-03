# Chemical Equipment Visualizer & Analysis System

A hybrid monitoring solution featuring a **Django REST API**, a **React Web Dashboard**, and a **PyQt5 Desktop Client**. This project provides real-time data visualization and automated reporting for industrial chemical equipment.

---

## 🚀 System Architecture

The project utilizes a centralized "Single Source of Truth" architecture:
- **Backend:** Django (Python) running on **Port 800**.
- **Web Frontend:** React.js for interactive browser-based monitoring.
- **Desktop Client:** PyQt5 for native Windows/Linux/macOS access.
- **Data Engine:** Pandas for CSV processing and statistical analysis.
- **Reporting:** ReportLab for server-side PDF generation.

---

## 🛠️ Features

### 1. Data Analysis
- Automated processing of equipment CSV files.
- Statistical mean calculation for pressure, temperature, and flowrate.
- Categorical distribution of equipment health status.

### 2. Interactive Visualizations
- **Pie Chart:** Proportional breakdown of Equipment Status (Operational/Maintenance).
- **Bar Graph:** Comparative analysis of parameter averages.
- **Data Table:** High-fidelity grid showing raw sensor readings and metadata.

### 3. Cross-Platform Sync
- Simultaneous data fetching for both Web and Desktop interfaces via the Port 800 API.

### 4. Automated Reporting
- One-click PDF export containing analysis summaries and timestamps.

---

## 📥 Installation

### Prerequisites
- Python 3.10+
- Node.js & npm

### 1. Backend Setup (Django)
```bash
# Navigate to root folder
pip install django pandas reportlab django-cors-headers djangorestframework
python manage.py migrate
python manage.py runserver 800
2. Frontend Setup (React)
Bash
cd frontend
npm install
# To run on localhost specifically
$env:HOST='127.0.0.1'; npm start
3. Desktop Setup (PyQt5)
Bash
pip install PyQt5 requests
python desktop/main.py