alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frequencies = frequencias = [
    ["A", 14.63],
    ["E", 12.57],
    ["O", 10.73],
    ["S", 7.81],
    ["R", 6.53],
    ["I", 6.18],
    ["N", 5.05],
    ["D", 4.99],
    ["M", 4.74],
    ["U", 4.63],
    ["T", 4.34],
    ["C", 3.88],
    ["L", 2.78],
    ["P", 2.52],
    ["V", 1.67],
    ["G", 1.30],
    ["H", 1.28],
    ["Q", 1.20],
    ["B", 1.04],
    ["F", 1.02],
    ["Z", 0.47],
    ["J", 0.40],
    ["X", 0.21],
    ["K", 0.02],
    ["W", 0.01],
    ["Y", 0.01]
]
enc = 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ'   # "THE QUICK BROWN FOX..."
a = 'ivj ajd j wvnovioz' # NAO FOI O BASTANTE

def enc_cesar_cypher(plain_text: str, key: int) -> str:
    ans = ''
    for c in plain_text:
        if c.isalnum():
            ans += alphabet[(alphabet.find(c) + key) % len(alphabet)]
    return ans

def freq_cypher(plain_text: str) -> str:
    freq = []
    ans = ''
    for letter in alphabet:
        freq.append([letter, plain_text.count(letter) * 100 / len(plain_text)])

    return ans
