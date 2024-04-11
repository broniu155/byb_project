### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    def __init__(self,email_address,subject_line,email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Declare the class variable, with default value, for emails.
    has_been_read = False 
    # Initialise the instance variables for emails.
    
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
        print("Email has been read ")
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    
    email_1 = Email("noreply@HyperionDev.co.uk","Hello You!",
                    "Welcome to your new job it is nice to have you!")
    email_2 = Email("HR@HyperionDev.co.uk","Setup your new account!",
                    "Here is a Gentle reminder to create the Sharepoint account!")
    email_3 = Email("noreply@Heperion.Sharepoint.co.uk",
                    "Here is your new code to access the Sharepoint",
                    "Your coude is 556622")
    
    inbox.extend([email_1,email_2,email_3])



    
def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print("List of emails: ")
    for count,email in enumerate(inbox):
        email = email.subject_line
        print(count,email)
        
   

def read_email(index):
    
    # Create a function which displays a selected email.
    if 0 <= index < len(inbox):
        email = inbox[index]
    for email in inbox:
        print(email.email_address,email.subject_line,email.email_content)
        print("Email has been read")     
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email.has_been_read = True   
# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while True:
     user_choice = int(input('''\nWould you like to:
     1. Read an email
     2. View unread emails
     3. Quit application

     Enter selection: '''))
       
     if user_choice == 1:
        # add logic here to read an email
         print("What e-mail would you like to read: ")
         list_emails()
         read_email(int(input("Enter Value: ")))       
        
     elif user_choice == 2:
         # add logic here to view unread emails
        list_emails()
        
     elif user_choice == 3:
         # add logic here to quit appplication
        print("Goodbye!")
        break
     else:
         print("Oops - incorrect input.")
