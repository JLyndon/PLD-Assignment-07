# ------------- CONTEXT --------------
# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# Example:
#   input: P@ssw0rd+P@ssw0rd
#   ouput: Valid

Criteria_00 = False
Criteria_02 = False
Criteria_03 = False
Criteria_04 = False

spcl_Char = "'[@_!#$%^&*()<>?/\|}{~:]`+=-.,:;~"

Usr_Pass = input("Password: ")
if len(Usr_Pass) <= 14: # Initial Requirement
    print("Password must be at least 15 characters long!")
else:
    for PWChar in Usr_Pass: # Iterate every char in PWString then evaluate.
        if PWChar.isalpha() == True: 
            if PWChar == PWChar.upper():
                Criteria_02 = True
            elif PWChar == PWChar.lower():
                Criteria_00 = True
        elif PWChar.isdecimal() == True:
            Criteria_03 = True
        elif PWChar in spcl_Char:
            Criteria_04 = False

print(Criteria_00)       
print(Criteria_02)
print(Criteria_03)
print(Criteria_04)