alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict = []
with open('lab1_criptografia_simetrica/dict.txt', 'r') as file:
    for line in file:
        dict.append(line.strip().lower())

def enc_cesar_cypher(plain_text: str, key:int) -> str:
    enc_str = ''
    for c in plain_text:
        enc_str += alphabet[(alphabet.find(c) + key) % len(alphabet)]
    return enc_str

def cesar_cypher(plain_text: str) -> str:
    plain_text = plain_text.replace(' ', '').lower()
    results = []
    for i in range(len(alphabet)):
        result = [enc_cesar_cypher(plain_text, i), 0]
        print(result[0])

        for w in dict:
            if w in result[0]:
                result[1] += 1

        results.append(result)
    
    m = 0
    ans = ''
    for enc in results:
        if enc[1] > m:
            m = enc[1]
            ans = enc[0]
    return ans

print(cesar_cypher('pdackkzpdaxwzwjzpdaqchu'))
