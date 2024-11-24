"""Project 3: Shopping Cart

Description: Simulate a shopping cart where users can add items with prices, 
              remove items, and view the total price.

Skills: Lists, loops, conditionals, user input.

Challenge: Implement a discount system (e.g., 10% off if the total exceeds a certain amount)..."""

class shoppint_cart:
    def __init__(self) -> None:
        self.items = []

    def add_items(self, name, price):
        self.items.append((name, price))
        print(f"Item '{name}', with price of {price} is added.\n")

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(f"Item {name} is removed from the cart.\n")
            else:
                print(f"Item {name} not found!!!\n")

    def view_cart(self):
        if not self.items:
            print("No item in the cart.\n")
        else:
            for item in self.items:
                print(f"Item: {item[0]}, Price: {item[1]}")

    def calculate_total(self):
        total = sum(price for name, price in self.items)
        return total
    
    def check_discount(self, total, base_amount = 1000):
        if total > base_amount:
            print(f"You are eligible for 10% discount!!!\n")
            disc_amount = (total/100)*10
            print(f"You are given a discount of {disc_amount}rs.")
            total -= disc_amount

        else:
            print(f"No discount applied. Spend more than {base_amount}rs to get a discount.")

        return total
    

def get_task():
    print("")
    print("========Shopping Cart========\n")
    print("0.   To exit the program.")
    print("1.   To add items with their prices in the cart.")
    print("2.   To remove items from the cart.")
    print("3.   To view total price of all items in the cart.")
    print("4.   To view the items and their prices in the cart.")
    print("5.   To check for discount on the total price.")
    print("")
   


def main():
    cart = shoppint_cart()

    while True:
        get_task()

        user_task = int(input("Enter You task to perform:"))
        
        match user_task:
            case 0:
                print("Exiting the program...")
                break

            case 1:
                name = str(input("Enter the item name:"))
                price = int(input("Enter the price of that item:"))
                cart.add_items(name, price)
            
            case 2:
                name = str(input("Enter the item name to remove it from the cart:"))
                cart.remove_item(name)

            case 3:
                total = cart.calculate_total()
                print(f"Total Price of items in cart: {total}")

            case 4:
                cart.view_cart()
            
            case 5:
                total_pay = cart.check_discount(total)
                print(f"After discount, (if applicable) You have to pay {total_pay}rs\n")

            case _:
                print("Please enter a valid input!!!")

if __name__ == "__main__":
    main()