alphabet = 'abcdefghijklmnopqrstuvwxyz'
frequencies = {
    "a": 14.63,
    "e": 12.57,
    "o": 10.73,
    "s": 7.81,
    "r": 6.53,
    "i": 6.18,
    "n": 5.05,
    "d": 4.99,
    "m": 4.74,
    "u": 4.63,
    "t": 4.34,
    "c": 3.88,
    "l": 2.78,
    "p": 2.52,
    "v": 1.67,
    "g": 1.30,
    "h": 1.28,
    "q": 1.20,
    "b": 1.04,
    "f": 1.02,
    "z": 0.47,
    "j": 0.40,
    "x": 0.21,
    "k": 0.02,
    "w": 0.01,
    "y": 0.01
}
enc = 'ivj ajd j wvnovioz' # NAO FOI O BASTANTE

def enc_cesar_cypher(plain_text: str, key: int) -> str:
    ans = ''
    for c in plain_text:
        if c.isalnum():
            ans += alphabet[(alphabet.find(c) + key) % len(alphabet)]
        else:
            ans += c
    return ans

def calc_diff(freq_list: list) -> float:
    dist = 0
    for i in freq_list:
        dist += abs(i[1] - frequencies[i[0]])
    return dist
    
def freq_cypher(plain_text: str) -> str:
    results = []
    ans = ''
    for i in range(len(alphabet)):
        freq = []
        result = [enc_cesar_cypher(plain_text, i), 0]
    
        for letter in alphabet:
            freq.append([letter, result[0].count(letter) * 100 / len(result[0])])
        result[1] = calc_diff(freq)
        results.append(result)
    min_dist = min(results, key=lambda x: x[1])
    return min_dist[0]

print(freq_cypher('ivj ajd j wvnovioz'))
print(freq_cypher('yqe jvewi hi xiwxi kpsfs vipskms geqmwe i xyhs qemw'))