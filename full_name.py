# Request users name
first_name = input("Kindly input your first name: ") # Users first name
last_name = input("Kindly input your last name: ") # Users last name

full_name = first_name + " " + last_name # Combine first and last name with a space
full_name_len = len(full_name) # Get the total number of characters

# Perform validations to ensure users name is in full
if full_name_len >= 4 and full_name_len <= 25:
    print(full_name + " " + "Thank you for entering your name!") #check if total number of characters is greater than 4 but less than 25
elif full_name_len <= 1: # Can you please explain why i get the else print statement when i input ``==0`` but the if print statement when i leave it this way
    print("You have not entered anything in. Kindly type in your fullname.") #check if total number of characters is less than 1
elif full_name_len <= 4: # check if total character is less than 4
    print("You have entered less than 4 characters. Please ensure you input your first name and your last name")
elif full_name_len >= 25: # check if total characters are more than 25
    print("You have entered more than 25 characters. Please ensure you only input your first and last name")
else:
    print("Kindly input your name correctly") 


