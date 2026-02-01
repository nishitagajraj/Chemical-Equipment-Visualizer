from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import EquipmentUpload
from .serializers import EquipmentUploadSerializer
import pandas as pd
import os

class EquipmentAnalysisView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # 1. Receive and Save the File
        file_serializer = EquipmentUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            
            # 2. Open the file with Pandas
            # We get the file path from the database instance we just saved
            file_path = file_instance.file.path
            
            try:
                # Read the CSV
                df = pd.read_csv(file_path)

                # 3. Perform Analytics (The Math)
                # Total equipment count
                total_count = len(df)
                
                # Average values (Flowrate, Pressure, Temperature)
                # We use .mean() and round to 2 decimal places
                avg_flowrate = round(df['Flowrate'].mean(), 2) if 'Flowrate' in df else 0
                avg_pressure = round(df['Pressure'].mean(), 2) if 'Pressure' in df else 0
                avg_temperature = round(df['Temperature'].mean(), 2) if 'Temperature' in df else 0

                # Equipment Type Distribution (Pie Chart data)
                # This counts how many of each 'Type' exist
                type_counts = df['Type'].value_counts().to_dict()

                # 4. Prepare the final answer
                response_data = {
                    "filename": os.path.basename(file_path),
                    "total_count": total_count,
                    "averages": {
                        "flowrate": avg_flowrate,
                        "pressure": avg_pressure,
                        "temperature": avg_temperature
                    },
                    "type_distribution": type_counts,
                    # We also send the raw data back so the table can show it
                    "data": df.head(50).to_dict(orient='records') 
                }

                return Response(response_data, status=200)

            except Exception as e:
                return Response({"error": str(e)}, status=400)
        
        return Response(file_serializer.errors, status=400)