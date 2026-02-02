# Chemical Equipment Analyzer (Hybrid System) 🚀

### **Overview**
This project is a hybrid data analysis tool designed to process chemical equipment datasets. It features a **Django-based central API** that serves two different frontends:
* **Web Dashboard**: Built with React for easy access and data visualization.
* **Desktop Client**: Built with PyQt5 (Python) for a dedicated, high-performance desktop experience.

The core goal of the project is to provide engineers with a unified platform to upload CSV data, visualize trends, and export professional PDF reports—regardless of which device they are using.

---

### **Key Features**
* **Unified Backend**: A single Django REST API handles all logic, ensuring data consistency across Web and Desktop.
* **PDF Generation**: Automated report generation using `ReportLab`, allowing users to download analysis summaries instantly.
* **Cross-Platform UI**: 
    * **React** for a responsive, modern web experience.
    * **PyQt5** for a robust desktop interface with native file-handling capabilities.
* **CSV Processing**: Backend logic to parse and analyze equipment data from uploaded files.

---

### **Tech Stack**
* **Backend**: Django, Django REST Framework, ReportLab (PDF generation).
* **Web Frontend**: React.js, Axios, Bootstrap.
* **Desktop Frontend**: Python, PyQt5, Requests.
* **Database**: SQLite (default Django DB).

---

### **Setup & Installation**

```bash
# 1. SETUP BACKEND (Django)
# Install all required dependencies
pip install django django-cors-headers reportlab requests

# Apply database migrations
python manage.py migrate

# Start the server on Port 8000
python manage.py runserver 8000

# 2. SETUP WEB FRONTEND (React)
# Navigate to frontend folder
cd frontend
npm install
npm start

# 3. SETUP DESKTOP APP (PyQt5)
# Run from the project root in a new terminal
python desktop/main.py

---

### **System Architecture & Environment Setup**

**1. SYSTEM DESIGN:**
   The application uses a "Single Source of Truth" architecture.
   - BACKEND: Django REST API handles logic, data parsing, and PDF generation.
   - CLIENTS: Both the React Web App and PyQt5 Desktop App consume the same endpoints.
   - CONSISTENCY: Centralized processing ensures identical results across all platforms.

**2. LOCAL ENVIRONMENT NOTE:**
   If you encounter port-binding errors (e.g., Errno 11001 or Permission Denied):
   - The system is port-agnostic.
   - Change the port in 'runserver [PORT]' to 8000 or 8080.
   - Update the API_URL in the frontend code to match the new port.
   - Running the terminal as Administrator can resolve most permission issues.


**Author**
Developed by **Nishita Gajraj **as part of the FOSSEE/Internship Technical Assessment.
