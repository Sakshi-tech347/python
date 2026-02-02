
square = lambda Val : Val* Val


def main():
    print("Enter data")
    Data = [int (x) for x in  input().split()]
    print(f"Actual Data is : {Data}")

    MData = list(map(square,Data))
    print(f"Data after Map : {MData}")


if __name__ == "__main__":
    main()
