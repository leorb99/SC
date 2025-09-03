alphabet = 'abcdefghijklmnopqrstuvwxyz'

def enc_cesar_cypher(plain_text: str, key: int) -> str:
    ans = ''
    for c in plain_text:
        if c.isalnum():
            ans += alphabet[(alphabet.find(c) + key) % len(alphabet)]
        else:
            ans += c
    return ans

def dec_cesar_cypher(plain_text: str, key: int) -> str:
    ans = ''
    for c in plain_text:
        if c.isalnum():
            ans += alphabet[(alphabet.find(c) - key) % len(alphabet)]
        else:
            ans += c
    return ans

print(enc_cesar_cypher('abc', 3))
print(enc_cesar_cypher('the good the bad and the ugly', 3))
print(dec_cesar_cypher(enc_cesar_cypher('abc', 3), 3))