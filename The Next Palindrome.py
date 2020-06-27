if __name__ == '__main__':
    print("Welcome to the program\tcreated by \x1b[6;30;42m'Jatin Rathi'\x1b[0m")
    num = int(input("\nHow many number you want to enter to know their next palindrome: "))
    list = []
    for i in range(num):
        n = int(input(f"Enter {i} number: "))
        list.append(n)
    j = 0
    for number in list:
        while True:
            number += 1
            string = str(number)
            if string == string[::-1]:
                print(f"Next palindrome number of {list[j]} is {string}")
                j += 1
                break

