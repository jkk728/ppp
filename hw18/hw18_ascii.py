def toggle_text(text:str):
    result=""
    for i in text:
        if ord(i) >= 65 and ord(i)<= 90:
            result += chr(ord(i)+32)
        elif ord(i) >= 97 and ord(i)<= 122:
            result += chr(ord(i)-32)

    return result

def main():
    print(toggle_text("Apple"))

if __name__=="__main__":
    main()