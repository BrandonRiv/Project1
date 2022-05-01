import ProjMod


'''
Initial Selection Prompt
'''
def select() -> int:
    print('----------------------')
    print('SELECT CALCULATION')
    print('----------------------')
    print('1 - Summation Calculator from 1 to your chosen number')
    print('2 - Exponent Calculator, first number being the constant, second being the power')
    print('3 - Countdown Calculator')

    calc = int(input('Calculation number: '))
    while calc < 1 or calc > 3:
        calc = int(input('Choose between (1-3): '))
    return calc


'''
Function that will use your first selection to figure out which calculation to use
'''
def main():
    while True:
        choice = select()
        if choice == 1:
            n = int(input("Choose a positive integer and I'll calculate the summation from 1 - your number : "))
            print('Summation Calculation = ', ProjMod.one(n))
        elif choice == 2:
            num = int(input("Choose a constant: "))
            pow = int(input("Choose the power: "))
            print('Exponent Calculation = ', ProjMod.two(num, pow))
        elif choice == 3:
            n3 = int(input("Choose a positive integer to count down to 1: "))
            print(ProjMod.three(n3))

        # Prompt asking if they want to continue
        cont = input("Continue (y/n): ").strip().lower()
        if cont == 'y':
            pass
        elif cont == 'n':
            print("Calculation Complete!")
            break
        else:
            cont = input("Enter y or n: ").strip().lower()
            if cont == 'n':
                print("Calculation Complete!")
                break


if __name__ == '__main__':
    main()