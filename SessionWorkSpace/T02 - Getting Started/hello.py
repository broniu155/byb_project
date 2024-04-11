class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
        print("Email has been read.")

    def __repr__(self):
        return f"Email from {self.email_address} with subject '{self.subject_line}'"

inbox = []

def populate_inbox():
    email_1 = Email("noreply@HyperionDev.co.uk", "Hello You!", "Welcome to your new job. It is nice to have you!")
    email_2 = Email("HR@HyperionDev.co.uk", "Setup your new account!", "Here is a gentle reminder to create the SharePoint account!")
    email_3 = Email("noreply@Heperion.Sharepoint.co.uk", "Here is your new code to access SharePoint", "Your code is 556622")
    
    inbox.extend([email_1, email_2, email_3])

def list_emails():
    print("Inbox Emails:")
    for count, email in enumerate(inbox):
        read_status = "Read" if email.has_been_read else "Unread"
        print(f"{count + 1}: {email.subject_line} ({read_status})")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"Reading email from {email.email_address}:")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email index.")

populate_inbox()

while True:
    print("\n--- Email Menu ---")
    print("1. List all emails")
    print("2. Read an email")
    print("3. Quit")
    user_choice = input("Enter selection: ")
    if user_choice == "1":
        list_emails()
    elif user_choice == "2":
        try:
            email_index = int(input("Enter the email number to read: ")) - 1
            read_email(email_index)
        except ValueError:
            print("Please enter a valid number.")
    elif user_choice == "3":
        print("Quitting email simulator.")
        break
    else:
        print("Invalid selection. Please try again.")
