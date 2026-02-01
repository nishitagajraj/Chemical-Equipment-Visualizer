import sys
import requests
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, 
                             QWidget, QFileDialog, QLabel, QTabWidget, QTextEdit, QMessageBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# SETTINGS
API_URL = "http://127.0.0.1:5000/api/upload/"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Analyzer (Desktop)")
        self.setGeometry(100, 100, 1000, 800) # Width, Height

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 1. Upload Button
        self.btn_upload = QPushButton("Upload CSV File")
        self.btn_upload.setStyleSheet("font-size: 16px; padding: 10px; background-color: #007bff; color: white;")
        self.btn_upload.clicked.connect(self.upload_file)
        self.layout.addWidget(self.btn_upload)

        # 2. Status Label
        self.status_label = QLabel("Please upload a file to begin.")
        self.status_label.setStyleSheet("font-size: 14px; margin: 10px;")
        self.layout.addWidget(self.status_label)

        # 3. Tabs for different views
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Tab 1: Summary Text
        self.tab_summary = QWidget()
        self.summary_layout = QVBoxLayout()
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        self.summary_layout.addWidget(self.summary_text)
        self.tab_summary.setLayout(self.summary_layout)
        self.tabs.addTab(self.tab_summary, "Summary Report")

        # Tab 2: Charts
        self.tab_charts = QWidget()
        self.charts_layout = QVBoxLayout()
        self.canvas = None # We will create the chart later
        self.tab_charts.setLayout(self.charts_layout)
        self.tabs.addTab(self.tab_charts, "Visualizations")

    def upload_file(self):
        # Open file dialog
        fname, _ = QFileDialog.getOpenFileName(self, 'Open CSV', '.', "CSV Files (*.csv)")
        
        if fname:
            self.status_label.setText(f"Uploading: {fname}...")
            
            # Prepare the file for sending
            files = {'file': open(fname, 'rb')}
            
            try:
                # TALK TO DJANGO (THE BRAIN)
                response = requests.post(API_URL, files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    self.status_label.setText("Analysis Complete!")
                    self.update_ui(data)
                else:
                    self.status_label.setText("Error: Server rejected the file.")
                    print(response.text)
            
            except Exception as e:
                self.status_label.setText("Error: Could not connect to Django.")
                QMessageBox.critical(self, "Connection Error", 
                                     "Make sure Django is running on Port 5000!\n\n" + str(e))

    def update_ui(self, data):
        # 1. Update Summary Tab
        averages = data['averages']
        summary_str = f"""
        ANALYSIS RESULT
        -----------------------------
        Filename: {data['filename']}
        Total Equipment Count: {data['total_count']}
        
        AVERAGES:
        - Flowrate: {averages['flowrate']}
        - Pressure: {averages['pressure']}
        - Temperature: {averages['temperature']}
        
        TYPE DISTRIBUTION:
        {data['type_distribution']}
        """
        self.summary_text.setText(summary_str)

        # 2. Update Charts Tab (Matplotlib)
        # Clear old chart if exists
        if self.canvas:
            self.charts_layout.removeWidget(self.canvas)
            self.canvas.deleteLater()

        # Create new Figure
        fig = Figure(figsize=(5, 4), dpi=100)
        
        # Subplot 1: Bar Chart (Averages)
        ax1 = fig.add_subplot(211) # 2 rows, 1 col, pos 1
        labels = ['Flowrate', 'Pressure', 'Temp']
        values = [averages['flowrate'], averages['pressure'], averages['temperature']]
        ax1.bar(labels, values, color=['#4BC0C0', '#FF6384', '#36A2EB'])
        ax1.set_title("Average Parameters")

        # Subplot 2: Pie Chart (Types)
        ax2 = fig.add_subplot(212)
        type_data = data['type_distribution']
        ax2.pie(type_data.values(), labels=type_data.keys(), autopct='%1.1f%%')
        ax2.set_title("Equipment Types")

        # Add to Window
        self.canvas = FigureCanvas(fig)
        self.charts_layout.addWidget(self.canvas)
        
        # Switch to Charts tab automatically
        self.tabs.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())