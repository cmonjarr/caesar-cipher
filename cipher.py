# add your code here
letters = "abcdefghijklmnopqrstuvwxyz"

encryption = {}
for i in range(26):
    j = (i + 5) % 26
    encryption[letters[i]] = letters[j]

#print(encryption)
#for letter in letters:
#    print(letter, encryption[letter])

user_sentence = input("Please enter a sentence:")
print(user_sentence)
user_sentece = user_sentence.lower()
print("Plain sentence:", user_sentence)

encrypted_text = ""
for letter in user_sentece:
    if letter in encryption:
        encrypted_text += encryption[letter]
    else:
        encrypted_text += letter
print("The encrypted sentence is:",  encrypted_text)