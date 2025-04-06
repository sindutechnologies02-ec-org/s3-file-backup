# 🔐 Secure File Backup System using AWS S3 + Python + Windows Task Scheduler

This project is a **Secure File Backup System** that automatically uploads files from a local folder to an AWS S3 bucket using Python and Windows Task Scheduler.

## 🚀 Features

- Uploads files to S3 using `boto3`
- Scheduled backups with Task Scheduler
- Handles `.txt`, `.jpg`, `.png`, and other files
- Logs uploaded files
- Optional: IAM role setup, encryption & versioning

## 🛠️ Technologies
- Python
- AWS S3
- IAM
- Windows Task Scheduler
- Git Bash

## 📁 Folder Structure


## 📌 How It Works

1. ✅ Copy files to the `project-backups/` folder
2. 🕒 Windows Task Scheduler runs the script daily
3. ☁️ Files are uploaded to S3 bucket
4. ✅ Message is printed: `Backup script completed successfully.`

## 📸 Screenshots
<img width="493" alt="image" src="https://github.com/user-attachments/assets/fb1c01fc-f8ed-4766-af96-0ae5e4f6d5ee" />


<img width="960" alt="image" src="https://github.com/user-attachments/assets/6cb1198d-e0a5-4c44-aab6-56ba8d783bc2" />


---

## 📦 To Run Manually

```bash
python backup_to_s3.py
## License

This project is licensed under the [MIT License](LICENSE).

