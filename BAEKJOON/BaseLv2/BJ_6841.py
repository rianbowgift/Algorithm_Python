b = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-((": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
}

while True:
    a = input()
    if a=="TTYL":
        print("talk to you later")
        break
    else:
        c = b.get(a,a)
        print(c)
