import sqlite3
import tkinter as tk

DB_PATH = "db.sqlite3"


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT email FROM profiles_api_userprofile")

emails = cursor.fetchall()

conn.close()


root = tk.Tk()
root.title("User Emails")
root.geometry("400x300")

label = tk.Label(root, text="Emails in database", font=("Arial", 14))
label.pack(pady=10)


for email in emails:
    email_label = tk.Label(root, text=email[0])
    email_label.pack()


root.mainloop()
