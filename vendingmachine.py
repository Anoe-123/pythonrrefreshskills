# ==== CODE ====

# Import our own Python files.
import vendingproducts
import Vendingmachinepayments

vendingproducts.show_products()

choice = int(input("\nChoose a product number:"))
amount = int(input("Enter your payment in pence:"))

product = vendingproducts.names[index]
price = vendingproducts.price[index]

if Vendingmachinepayments.enough_money(amount,price):
    change = Vendingmachinepayments.calucualte_change(amount, price)

    print("Dispensing:", product)
    print("Your change:", change, "p")


else:
    print("Not enough money.")
    print("Your payment has been returned:", amount, "p")


