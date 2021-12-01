# ---------- CONTEXT --------------
# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
#  Example:
#     input: Sample Text here
#     output:
#           words: 3
#           vowels: 6
#           consonants: 8

def EliminateSpace_(Text):
    sub_word_count = 0
    identif_word, *temp = Text.split(" ") 
    for character in identif_word:
        if (character != "") or (character != None) or (character.isspace() == False):
            sub_word_count = 1
        else:
            None
    for sub_char in temp:
        for lower_char in sub_char:
            if (lower_char != "") or (sub_char != None) or (sub_char.isspace() == False):
                sub_word_count += 1
                break
            else:
                None
    return sub_word_count


Usr_Text = input("\nEnter text: ").lower()

word_count = EliminateSpace_(Usr_Text)
vowels = 0
consonants = 0

vowel_str = "aeiou"

for char in Usr_Text:
    if char == " ":
        if (Usr_Text.isspace() == True) or ((Usr_Text == "") or (Usr_Text == None)):
            break
    elif char in vowel_str:
        vowels += 1
    elif char not in vowel_str:
        if char.isalpha() == True:
            consonants += 1
    else:
        None

print(f"\nWords: {word_count}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")