Chemical Equipment Analyzer (Hybrid System)
Overview
This project is a hybrid data analysis tool designed to process chemical equipment datasets. It features a Django-based central API that serves two different frontends:

Web Dashboard: Built with React for easy access and data visualization.

Desktop Client: Built with PyQt5 (Python) for a dedicated, high-performance desktop experience.

The core goal of the project is to provide engineers with a unified platform to upload CSV data, visualize trends, and export professional PDF reports—regardless of which device they are using.

Key Features
Unified Backend: A single Django REST API handles all logic, ensuring data consistency across Web and Desktop.

PDF Generation: Automated report generation using ReportLab, allowing users to download analysis summaries instantly.

Cross-Platform UI:

React for a responsive, modern web experience.

PyQt5 for a robust desktop interface with native file-handling capabilities.

CSV Processing: Backend logic to parse and analyze equipment data from uploaded files.

Tech Stack
Backend: Django, Django REST Framework, ReportLab (PDF generation).

Web Frontend: React.js, Axios, Bootstrap.

Desktop Frontend: Python, PyQt5, Requests.

Database: SQLite (default Django DB).

Setup & Installation
1. Backend (Django)
Bash
# Navigate to the project root
pip install django django-cors-headers reportlab requests
python manage.py migrate
python manage.py runserver 8000
2. Web Frontend (React)
Bash
cd frontend
npm install
npm start
3. Desktop App (PyQt5)
Bash
# From the project root
python desktop/main.py
System Architecture
The system follows a Producer-Consumer pattern. The Django backend acts as the "Source of Truth." Both the React application and the PyQt5 desktop app consume the same API endpoints, such as /api/upload/ and /api/export-pdf/. This ensures that if the logic is updated once in the backend, all users benefit immediately.

Note on Local Environment
During the final build, some environments may experience port-binding restrictions (e.g., Errno 11001 or Permission Denied on certain local ports). The application is designed to be port-agnostic and can be run on any available port (e.g., 8000, 8080) by updating the base URL in the frontend configuration files.

Author
Developed by Nishita Gajraj as part of the FOSSEE/Internship Technical Assessment.
