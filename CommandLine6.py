


def Addition(no1 , no2):

    iAns = 0

    iAns = no1+ no2

    return iAns    


def main():
    print("Eneter the first number : ") 
    iValue1 = int(input())

    print("Eneter the Second number : ") 
    iValue2 = int(input())
    iRet = Addition(iValue1 , iValue2)
    print("Addition of two Number is  is ",iRet)

if __name__ == "__main__":
    main()