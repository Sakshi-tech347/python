#chect charector is vowel or not
def ChckVowel(charector):
    if charector in('A','E','I','O','U','a','e','i','o','u'):
        print("it is a Vowel")
    else:
        print("it is  NOT a Vowel")

def main():
    Value = (input("Enter a charector"))
    ChckVowel(Value)

if __name__ == "__main__":
    main()
