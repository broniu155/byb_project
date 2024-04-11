
inbox = ["1","2","3"]
# --- Functions --- #
# Build out the required functions for your program.

def read_email(index):
    
    # Create a function which displays a selected email.
    if 0 < enumerate(index) < len(inbox):
      #  index = inbox[index]
        for i in index:
            print(i)
            
read_email(inbox)            