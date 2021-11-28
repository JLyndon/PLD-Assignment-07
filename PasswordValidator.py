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

Criteria_01 = False
Criteria_02 = False
Criteria_03 = False
Criteria_04 = False

spcl_Char = "'[@_!#$%^&*()<>?/\|}{~:]`+=-.,:;~"

Usr_Pass = input("Password: ")

for PWChar in Usr_Pass: # Iterate every char in PWString then evaluate.
    if Usr_Pass.rindex(PWChar) >= 16:
        Criteria_01 = True
    if PWChar.isalpha() == True: 
        if PWChar == PWChar.upper():
            Criteria_02 = True
    elif PWChar.isdecimal() == True:
        Criteria_03 = True
    elif PWChar in spcl_Char:
        Criteria_04 = True
    
print(Criteria_01)
print(Criteria_02)
print(Criteria_03)
print(Criteria_04)