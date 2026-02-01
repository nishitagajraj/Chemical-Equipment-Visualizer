# Chemical Equipment Parameter Visualizer

A hybrid application (Web + Desktop) for visualizing chemical equipment data, built for the FOSSEE Internship Screening Task.

## 🚀 Features
- **Hybrid Architecture:** Common Django backend serving both React (Web) and PyQt5 (Desktop) frontends.
- **Data Analytics:** Calculates average Flowrate, Pressure, and Temperature.
- **Visualizations:**
  - **Web:** Interactive charts using Chart.js.
  - **Desktop:** Native charts using Matplotlib.
- **History:** SQLite database stores uploaded datasets.

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework, Pandas
- **Frontend (Web):** React.js, Bootstrap, Chart.js
- **Frontend (Desktop):** PyQt5, Matplotlib, Requests

## ⚙️ Setup Instructions

### 1. Backend (Django)
```bash
cd Chemical_Project
python -m venv env
# Activate env (Windows: .\env\Scripts\activate | Mac/Linux: source env/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 5000

cd frontend
npm install
npm start
# Runs on http://localhost:3000

# Ensure Backend is running first!
python desktop/main.py