#---------- CONTEXT --------------
#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#  Example:
#     input: Sample Text here
#     output:
#           words: 3
#           vowels: 6
#           consonants: 8

Usr_Text = input("Enter text: ").lower()

vowel_list = "a","e","i","o","u"
word_count = 1
vowels = 0
consonants = 0

for char in Usr_Text:
    if char == " ":
        word_count += 1
    elif char in vowel_list:
        vowels += 1
    elif char not in vowel_list:
        if char.isalpha() == True:
            consonants += 1
    else:
        None

print(word_count)
print(vowels)
print(consonants)