alphabet = 'abcdefghijklmnopqrstuvwxyz'

def enc_cesar_cypher(plain_text: str, key:int) -> str:
    enc_str = ''
    for c in plain_text:
        enc_str += alphabet[(alphabet.find(c) + key) % len(alphabet)]
    return enc_str

def dec_cesar_cypher(plain_text: str, key:int) -> str:
    enc_str = ''
    for c in plain_text:
        enc_str += alphabet[(alphabet.find(c) - key) % len(alphabet)]
    return enc_str

print(enc_cesar_cypher('abc', 3))
print(dec_cesar_cypher(enc_cesar_cypher('abc', 3), 3))