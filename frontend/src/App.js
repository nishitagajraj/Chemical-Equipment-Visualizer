import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js';
import { Bar, Pie } from 'react-chartjs-2';

// Register the chart components so React can use them
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  // 1. Handle when user selects a file
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError('');
  };

  // 2. Send the file to Django (Port 8080)
  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      // Note: We use port 8080 because that's where Django is listening
      const response = await axios.post('http://127.0.0.1:800/api/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setData(response.data); // Save the answer from the brain
    } catch (err) {
      console.error(err);
      setError('Error uploading file. Make sure Django is running on port 8080!');
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Chemical Equipment Visualizer</h1>

      {/* Upload Section */}
      <div className="card p-4 shadow-sm mb-4">
        <div className="d-flex justify-content-center align-items-center gap-3">
          <input type="file" className="form-control w-50" onChange={handleFileChange} />
          <button className="btn btn-primary" onClick={handleUpload}>
            Analyze Data
          </button>
           
           <button 
  className="btn btn-danger ms-2" 
  onClick={() => window.open('http://127.0.0.1:800/api/export-pdf/', '_blank')}
>
  Download PDF Report
</button>
        </div>
        {error && <p className="text-danger text-center mt-2">{error}</p>}
      </div>

      {/* Results Section - Only shows if we have data */}
      {data && (
        <div>
          {/* Summary Cards */}
          <div className="row mb-4">
            <div className="col-md-3">
              <div className="card text-white bg-primary mb-3">
                <div className="card-header">Total Equipment</div>
                <div className="card-body">
                  <h3 className="card-title">{data.total_count}</h3>
                </div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="card text-white bg-success mb-3">
                <div className="card-header">Avg Flowrate</div>
                <div className="card-body">
                  <h3 className="card-title">{data.averages.flowrate}</h3>
                </div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="card text-white bg-warning mb-3">
                <div className="card-header">Avg Pressure</div>
                <div className="card-body">
                  <h3 className="card-title">{data.averages.pressure}</h3>
                </div>
              </div>
            </div>
            <div className="col-md-3">
              <div className="card text-white bg-danger mb-3">
                <div className="card-header">Avg Temp</div>
                <div className="card-body">
                  <h3 className="card-title">{data.averages.temperature}</h3>
                </div>
              </div>
            </div>
          </div>
{/* Charts Section */}
          <div className="row mb-4">
            {/* Pie Chart: Equipment Types */}
            <div className="col-md-6">
              <div className="card shadow-sm p-3">
                <h5 className="text-center">Equipment Type Distribution</h5>
                <div style={{ height: '300px', display: 'flex', justifyContent: 'center' }}>
                  <Pie
                    data={{
                      labels: Object.keys(data.type_distribution),
                      datasets: [
                        {
                          label: '# of Equipment',
                          data: Object.values(data.type_distribution),
                          backgroundColor: [
                            '#FF6384',
                            '#36A2EB',
                            '#FFCE56',
                            '#4BC0C0',
                            '#9966FF',
                          ],
                          borderWidth: 1,
                        },
                      ],
                    }}
                    options={{ maintainAspectRatio: false }}
                  />
                </div>
              </div>
            </div>

            {/* Bar Chart: Averages */}
            <div className="col-md-6">
              <div className="card shadow-sm p-3">
                <h5 className="text-center">Parameter Averages</h5>
                <div style={{ height: '300px' }}>
                  <Bar
                    data={{
                      labels: ['Flowrate', 'Pressure', 'Temperature'],
                      datasets: [
                        {
                          label: 'Average Values',
                          data: [
                            data.averages.flowrate,
                            data.averages.pressure,
                            data.averages.temperature,
                          ],
                          backgroundColor: ['#4BC0C0', '#FF6384', '#36A2EB'],
                        },
                      ],
                    }}
                    options={{
                      maintainAspectRatio: false,
                      responsive: true,
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
          {/* Data Table */}
          <div className="card shadow-sm">
            <div className="card-header">Data Preview (First 50 rows)</div>
            <div className="table-responsive" style={{ maxHeight: '400px' }}>
              <table className="table table-striped table-hover mb-0">
                <thead>
                  <tr>
                    <th>Equipment Name</th>
                    <th>Type</th>
                    <th>Flowrate</th>
                    <th>Pressure</th>
                    <th>Temperature</th>
                  </tr>
                </thead>
                <tbody>
                  {data.data.map((row, index) => (
                    <tr key={index}>
                      <td>{row['Equipment Name']}</td>
                      <td>{row['Type']}</td>
                      <td>{row['Flowrate']}</td>
                      <td>{row['Pressure']}</td>
                      <td>{row['Temperature']}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
