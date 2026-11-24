# Outlook Email Sender

A desktop app that sends emails through Outlook to a list of recipients read from a CSV file, with an optional attachment. Built with Python and tkinter.

## Features

- Choose a CSV file of recipients (`name,email` columns)
- Optional file attachment
- Sends a separate email to each recipient through Outlook
- Checks for a missing file, wrong file type, empty subject, or empty message
- Confirmation popup showing how many people will receive the email
- Error popups instead of crashes

## Requirements

- Windows
- Classic Outlook desktop app, installed, signed in, and open (the new Outlook doesn't work)
- Python 3
- The `pywin32` package: `pip install pywin32`

## Usage

1. Make a CSV file with a header row and one person per row:

   ```
   name,email
   Anna,anna@example.com
   Ben,ben@example.com
   ```

2. Open classic Outlook.
3. Run `python gui_test.py`.
4. Click **Choose Recipient File** and pick your CSV.
5. Optionally click **Choose Attachment** and pick a file.
6. Enter a subject and a message, then click **Send**.
7. Confirm the popup. The app sends one email per row.