if __name__ == "__main__":
    print("=~=~=~=~=~=~=~=~=~=~=")
    print("")
    height = float(input("Input the height (cm): "))
    width = float(input("Input the width (cm): "))
    length = float(input("Input the length (cm): "))
    print("")
    print("=~=~=~=~=~=~=~=~=~=~=")

    if height > 80 or width > 80 or length > 80:
        print("Rejected, measurements exceed 80cm.")
    elif height < 80 or width < 80 or length < 80:
        print("Works")
    else:
        print("Error")
