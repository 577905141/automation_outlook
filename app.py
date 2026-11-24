import csv
import win32com.client
import os

outlook = win32com.client.Dispatch("Outlook.Application")

def send_email(to, subject, body, attachment_path=""):
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    if attachment_path != "":
        mail.Attachments.Add(attachment_path)
    mail.Send()
def send_to_all(csv_path, subject, body, attachment_path=""):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            send_email(row["email"], subject, body, attachment_path)
            print("sent to", row["email"])
def count_recipients(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return len(list(reader))