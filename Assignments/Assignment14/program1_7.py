 
Divisible_5 = lambda Value :(Value % 5 == 0)


def main():
    no1 = int(input("Enter Number :"))

    Ret =(Divisible_5(no1))
    print(Ret)

if __name__ == "__main__":
    main()
