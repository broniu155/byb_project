#-------- Python manipulation tasks ----------#

# Assign the random user string input as variable

str_manip = input("Enter the sentance:")

# Output the lenght of the provided sentance

print(f"Lenght of the sentance is: {len(str_manip)}")

# Find the last letter in the provided sentance
# and print result replacing the last letter

last_chr = str_manip[-1:]
print(str_manip.replace(last_chr,"@"))

# Output last three characters backwards 

print(str_manip[-1:-4:-1])

# Output five letter word from main input string

first_char3 = str_manip[:3]
last_char2 = str_manip[-2:]

print(first_char3 + last_char2)
  