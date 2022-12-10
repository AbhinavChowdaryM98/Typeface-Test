def soundex_generator(token):
    token = token.lower()
    s = "" + token[0]
    d = {"bfpv": "1", "cgjkqsxz": "2", "dt": "3", "l": "4", "mn": "5", "r": "6", "aeiouhwy": ".",}
    for char in token[1:]:
        for key in d.keys():
            if char in key:
                code = d[key]
                if code != '.':
                    if code != s[-1]:
                        s += code
            s = s[:7].ljust(7, "0")
    return s

s1 = input("Input1: ")
s2 = input("Iput2: ")

if soundex_generator(s1) == soundex_generator(s2):
    print("Both are phonetically Same")
else:
    print("Both are not phonetically same")