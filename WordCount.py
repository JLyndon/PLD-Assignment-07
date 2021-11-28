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
    else:
        if char.isdecimal() == False:
            consonants += 1
        else:
            None

print(word_count)
print(vowels)
print(consonants)