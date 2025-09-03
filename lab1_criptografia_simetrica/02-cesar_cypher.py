alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict = []
with open('lab1_criptografia_simetrica/dict.txt', 'r') as file:
    for line in file:
        dict.append(line.strip().lower())

def enc_cesar_cypher(plain_text: str, key: int) -> str:
    ans = ''
    for c in plain_text:
        if c.isalnum():
            ans += alphabet[(alphabet.find(c) + key) % len(alphabet)]
        else:
            ans += c
    return ans

def cesar_cypher(plain_text: str) -> str:
    results = []
    for i in range(len(alphabet)):
        result = [enc_cesar_cypher(plain_text, i), 0]
        print(result[0])

        for w in dict:
            if result[0].count(w):
                result[1] += result[0].count(w)

        results.append(result)
    
    m = 0
    ans = ''
    for enc in results:
        if enc[1] > m:
            m = enc[1]
            ans = enc[0]
    return ans

print(cesar_cypher('pda ckkz pda xwz wjz pda qchu'))
