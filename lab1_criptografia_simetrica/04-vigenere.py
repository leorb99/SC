alphabet = 'abcdefghijklmnopqrstuvwxyz'
vigenere = []

for i in range(26):
    vigenere.append(alphabet)
    alphabet = alphabet[1:] + alphabet[0]

print(vigenere)