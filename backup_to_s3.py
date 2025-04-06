import boto3
import os
from datetime import datetime

bucket_name = 's3-file-backup-bucket-sindu'  # <-- Replace with your bucket name
backup_folder = r'C:\Users\sindu\Desktop\project-backups'
  # Folder you want to back up

s3 = boto3.client('s3')

for filename in os.listdir(backup_folder):
    file_path = os.path.join(backup_folder, filename)
    if os.path.isfile(file_path):
        s3.upload_file(file_path, bucket_name, f"{datetime.now().strftime('%Y-%m-%d')}/{filename}")
        print(f"Uploaded: {filename}")
print("Backup script completed successfully.")

