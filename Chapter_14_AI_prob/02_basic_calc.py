"""Project 2: Simple Calculator

Description: Build a command-line calculator that can perform basic arithmetic operations like
                (addition, subtraction, multiplication, and division).

Skills: Basic input/output, conditionals, arithmetic operations.

Challenge: Add an option for handling invalid inputs (e.g., divide by zero)..."""



def get_input():
    while True:
        try:
            input_str = str(input("Enter what do you want to do in (operator1 * operator2)format: "))
            input_lst = input_str.split(" ")

            op1 = int(input_lst[0])
            sym = input_lst[1]
            op2 = int(input_lst[2])

            return op1, sym, op2
        
        except Exception as e:
            print("Invalid input. Please enter the operation in the correct format.\n")
            continue

def main():

    while True:
        op1, sym, op2 = get_input()
        print("")

        match sym:
            case '+':
                print(f"{op1} + {op2} = {op1 + op2}")

            case '-':
                print(f"{op1} - {op2} = {op1 - op2}")

            case '*':
                print(f"{op1} * {op2} = {op1 * op2}")

            case '/':
                try:
                    print(f"{op1} / {op2} = {op1 / op2}")

                except ZeroDivisionError:
                    print(f"Error: Cannot divide by 0\n")
            case _:
                print("Please do a valid operation(+, -, *, /)!!!")


        exit = int(input("Enter '0' to continue, and '1' to exit:\n"))
        if exit == 1:
            print("Exiting the program!!!")
            break
        

if __name__ == "__main__":
        main()

    