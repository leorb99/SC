alphabet = 'abcdefghijklmnopqrstuvwxyz'
vigenere_tab = []

for i in range(26):
    vigenere_tab.append(alphabet)
    alphabet = alphabet[1:] + alphabet[0]

def vigenere_cipher(plain_text: str, key: str) -> str:
    ans = ''
    for i in range(len(plain_text)):
        if(plain_text[i].isalnum()):
            idx = alphabet.find(plain_text[i])
            idx_k = alphabet.find(key[i%len(key)])
            ans += vigenere_tab[idx][idx_k]
    return ans

def decode(plain_text: str, key: str) -> str:
    ans = ''
    for i in range(len(plain_text)):
        if(plain_text[i].isalnum()):
            idx_k = alphabet.find(key[i%len(key)])
            idx = vigenere_tab[idx_k].find(plain_text[i])
            ans += alphabet[idx]
    return ans
    
print(vigenere_cipher('ATAQUEAMANHA'.lower(), 'LIMAO'.lower()))
print(vigenere_cipher('CRYPTOGRAFIA'.lower(), 'SEGREDO'.lower()))
print(vigenere_cipher('SEGURANCA'.lower(), 'CHAVE'.lower()))

print(decode('lbmqipiyabsi'.lower(), 'limao'.lower()))
print(decode('uvegxrujelze'.lower(), 'segredo'.lower()))
print(decode('ulgpvcucv'.lower(), 'chave'.lower()))
