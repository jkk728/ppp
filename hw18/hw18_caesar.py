def caesar_encode(text:str, shift:int=3):
    for i in text:
        if ord(i) >= 65 and ord(i) <= 87:
            return chr(ord(i)+shift)
        elif ord(i) >= 97 and ord(i) <=118:
            return chr(ord(i)+shift)
        elif ord(i) >= 88 and ord(i) <= 90:
            return chr(ord(i)-25+shift)
        elif ord(i) >= 119 and ord(i) <=122:
            return chr(ord(i)-25+shift)

def caesar_decode(text:str, shift:int=3):
    for i in text:
        if ord(i) >= 68 and ord(i) <= 90:
            return chr(ord(i)-shift)
        elif ord(i) >= 100 and ord(i) <=122:
            return chr(ord(i)-shift)
        elif ord(i) >= 65 and ord(i) <= 67:
            return chr(ord(i)+25-shift)
        elif ord(i) >= 97 and ord(i) <=99:
            return chr(ord(i)+25-shift)

def toggle_e(e):
    result=""
    for i in e:
        result += caesar_encode(i)
    return result

def toggle_d(d):
    result = ""
    for i in d:
        result += caesar_decode(i)
    return result

def main():
    print(toggle_e("Abc"))
    print(toggle_d("Def"))

if __name__=="__main__":
    main()