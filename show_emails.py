import sqlite3
import tkinter as tk

DB_PATH = "db.sqlite3"


root = tk.Tk()
# root is the main window of the application. We set its title and size. Tk() is a function that creates the main window and
# returns a reference to it, which we store in the variable root.
# We can then use this variable to configure the window and add widgets to it.
root.title("User Emails")
root.geometry("400x300")

title = tk.Label(root, text="Emails in database", font=("Arial", 14))
title.pack(pady=10)

email_frame = tk.Frame(root)
# tk.Frame is a container widget that can hold other widgets. We create a frame to hold the email labels
# and pack it into the main window.
email_frame.pack(fill="both", expand=True)
last_record_emails_count = 0


def refresh_emails():
    global last_record_emails_count
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM profiles_api_userprofile")

    emails = cursor.fetchall()
    # emails is now a list of tuples, where each tuple contains a single email address. We can access the email address using email[0] in the loop below.

    conn.close()
    ######################################################################
    # The connection to the database is established using sqlite3.connect, and a cursor is created to execute SQL queries.
    # The query retrieves all email addresses from the profiles_api_userprofile table,
    # and the results are stored in the emails variable. Finally, the connection to the database is closed.
    # clear old labels
    if (
        len(emails) != last_record_emails_count
    ):  # Checks if the number of emails retrieved from the database is
        # different from the last recorded count. If it is different, it means that there has been a change in the database
        # (either new emails added or some emails removed), and we need to update the displayed list of emails.
        last_record_emails_count = len(emails)
        for widget in email_frame.winfo_children():
            widget.destroy()

        # add updated labels
        for email in emails:
            tk.Label(email_frame, text=email[0]).pack()

    # check again in 2 seconds
    root.after(2000, refresh_emails)


refresh_emails()
root.mainloop()
