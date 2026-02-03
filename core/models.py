from django.db import models

class EquipmentUpload(models.Model):
    # This stores the actual CSV file
    file = models.FileField(upload_to='uploads/') 
    
    # This records exactly when it was uploaded (for the "Last 5" feature)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # This gives the file a readable name in the database
    def __str__(self):
        return f"File uploaded at {self.uploaded_at}"

    # This ensures we only keep the File, not the complex row data in DB 
    # (We will use Pandas for the math later, which is faster for analytics)
