def main():
    #write your code below this line
    year = int(input("Give a year: "))

    if (year % 4) == 0:
        print(f"The year {year} is a leap year!")
    else:
        print(f"The year {year} is not a leap year.")

if __name__ == '__main__':
    main()
