import tkinter as tk
from tkinter import filedialog, messagebox
from app import send_to_all, count_recipients


recipient_path = ""
window = tk.Tk()
window.title("email sender")
window.geometry("400x300")
label = tk.Label(window, text="Recipient file:")
label.pack()
attachment_path = ""

def on_click() :
    global recipient_path
    recipient_path= filedialog.askopenfilename()
    label.config(text="Recipient file: "+ recipient_path)

button=tk.Button(window, text= "Choose Recipient File", command=on_click)
button.pack()
def choose_attach():
    global attachment_path
    attachment_path = filedialog.askopenfilename()
    attachment_label.config(text="Attachment: " + attachment_path)

attachment_label = tk.Label(window, text="Attachment: (none)")
attachment_label.pack()

attachment_button = tk.Button(window, text="Choose Attachment", command=choose_attach)
attachment_button.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()

subject_box = tk.Entry(window, width=40)
subject_box.pack()

body_label = tk.Label(window, text="Message:")
body_label.pack()

body_box = tk.Text(window, width=40, height=5)
body_box.pack()

def on_send():
    if recipient_path == "":
        messagebox.showwarning("Missing file", "Please choose a recipient file.")
        return
    if not recipient_path.lower().endswith(".csv"):
        messagebox.showwarning("Wrong file type", "The recipient file must be a .csv file.")
        return
    subject = subject_box.get()
    if subject.strip() == "":
        messagebox.showwarning("Missing subject", "Please enter a subject.")
        return
    body = body_box.get("1.0", "end")
    if body.strip() == "":
        messagebox.showwarning("Missing subject", "Please enter body.")
        return
    count = count_recipients(recipient_path)
    if not messagebox.askyesno("Confirm", f"Send emails to {count} people in this file?"):
     return
    try:
        send_to_all(recipient_path, subject, body, attachment_path)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
        messagebox.showinfo("Done", f"Sent {count} emails.")
    send_to_all(recipient_path, subject, body, attachment_path)
send_button = tk.Button(window, text="Send", command=on_send)
send_button.pack()
window.mainloop()
