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

def PWValidator(Usr_Pass):
    Criteria_01 = False
    Criteria_02 = False
    Criteria_03 = False
    Criteria_04 = False
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
    return Criteria_01, Criteria_02, Criteria_03, Criteria_04

#Main Prog
spcl_Char = "'[@_!#$%^&*()<>?/\|}{~:]`+=-.,:;~" + '"'

Input_Pass = input("\nPassword: ")
InstA, InstB, InstC, InstD = PWValidator(Input_Pass)

# Interpret Results
if InstA and InstB and InstC and InstD == True:
    print("\n\33[92mValid Password\33[0m\n")
else:
    print("\n\33[91mInvalid Password\33[0m\n")
