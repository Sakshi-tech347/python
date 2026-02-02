
chkEvn = lambda val1 : (val1 % 2 == 0)


def main():
    print("Enter Data")
    Data = [int(x)for x in input().split()]
    print(f"Actual Data is {Data}")

    FData = list(filter(chkEvn,Data))
    print(f"Filtered Even data {FData}")

if __name__ == "__main__":
    main()