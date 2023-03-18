# Request users name
first_name = input("Kindly input your first name: ") # Users first name
last_name = input("Kindly input your last name: ") # Users last name

full_name = first_name + " " + last_name # Combine first and last name with a space
full_name_len = len(full_name) # Get the total number of characters

# Perform validations to ensure users name is in full
if full_name_len >= 4 and full_name_len <= 25:
    print(full_name + " " + "Thank you for entering your name!") #check if total number of characters is greater than 4 but less than 25
else:
    print("Kindly input your name correctly") # If not request for a new input



