import random
import datetime

products = {
    101: {"name": "Laptop", "price": 55000, "stock": 8},
    102: {"name": "Keyboard", "price": 1200, "stock": 20},
    103: {"name": "Mouse", "price": 700, "stock": 25},
    104: {"name": "Monitor", "price": 9500, "stock": 10},
    105: {"name": "Headphones", "price": 1800, "stock": 15},
    106: {"name": "Webcam", "price": 2500, "stock": 12},
    107: {"name": "USB Cable", "price": 400, "stock": 30},
    108: {"name": "Power Bank", "price": 2200, "stock": 18},
    109: {"name": "Speaker", "price": 3200, "stock": 14},
    110: {"name": "SSD 1TB", "price": 6500, "stock": 9}
}

customers = []
sales = []
cart = []

store_name = "TechZone Store"


def line():
    print("-" * 60)


def header(title):
    line()
    print(title.center(60))
    line()


def show_products():
    header("PRODUCT LIST")

    print(f"{'ID':<8}{'PRODUCT':<20}{'PRICE':<15}{'STOCK':<10}")

    for product_id, product in products.items():
        print(
            f"{product_id:<8}"
            f"{product['name']:<20}"
            f"₹{product['price']:<14}"
            f"{product['stock']:<10}"
        )

    line()


def add_product():
    header("ADD NEW PRODUCT")

    product_id = int(input("Enter product ID: "))

    if product_id in products:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully.")


def update_product():
    header("UPDATE PRODUCT")

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    product = products[product_id]

    print(f"Current Name: {product['name']}")
    print(f"Current Price: {product['price']}")
    print(f"Current Stock: {product['stock']}")

    name = input("Enter new name: ")
    price = int(input("Enter new price: "))
    stock = int(input("Enter new stock: "))

    product["name"] = name
    product["price"] = price
    product["stock"] = stock

    print("Product updated successfully.")


def delete_product():
    header("DELETE PRODUCT")

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    product_name = products[product_id]["name"]

    confirm = input(
        f"Delete {product_name}? (yes/no): "
    ).lower()

    if confirm == "yes":
        del products[product_id]
        print("Product deleted.")
    else:
        print("Delete cancelled.")


def search_product():
    header("SEARCH PRODUCT")

    keyword = input("Enter product name: ").lower()

    found = False

    for product_id, product in products.items():
        if keyword in product["name"].lower():
            print(
                f"{product_id} - "
                f"{product['name']} - "
                f"₹{product['price']} - "
                f"Stock: {product['stock']}"
            )
            found = True

    if not found:
        print("No product found.")


def low_stock():
    header("LOW STOCK PRODUCTS")

    found = False

    for product_id, product in products.items():
        if product["stock"] <= 5:
            print(
                f"{product_id} - "
                f"{product['name']} - "
                f"Stock: {product['stock']}"
            )
            found = True

    if not found:
        print("No low-stock products.")


def register_customer():
    header("CUSTOMER REGISTRATION")

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    customer_id = random.randint(1000, 9999)

    customer = {
        "id": customer_id,
        "name": name,
        "phone": phone,
        "email": email
    }

    customers.append(customer)

    print("Customer registered successfully.")
    print(f"Customer ID: {customer_id}")


def show_customers():
    header("CUSTOMER LIST")

    if not customers:
        print("No customers registered.")
        return

    for customer in customers:
        print(f"Customer ID: {customer['id']}")
        print(f"Name: {customer['name']}")
        print(f"Phone: {customer['phone']}")
        print(f"Email: {customer['email']}")
        line()


def find_customer():
    header("FIND CUSTOMER")

    customer_id = int(input("Enter customer ID: "))

    for customer in customers:
        if customer["id"] == customer_id:
            print(f"Name: {customer['name']}")
            print(f"Phone: {customer['phone']}")
            print(f"Email: {customer['email']}")
            return

    print("Customer not found.")


def add_to_cart():
    header("ADD TO CART")

    show_products()

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Invalid product ID.")
        return

    quantity = int(input("Enter quantity: "))

    product = products[product_id]

    if quantity <= 0:
        print("Invalid quantity.")
        return

    if quantity > product["stock"]:
        print("Not enough stock.")
        return

    item = {
        "id": product_id,
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity
    }

    cart.append(item)

    print("Product added to cart.")


def show_cart():
    header("SHOPPING CART")

    if not cart:
        print("Cart is empty.")
        return 0

    total = 0

    for item in cart:
        amount = item["price"] * item["quantity"]
        total += amount

        print(
            f"{item['name']} | "
            f"₹{item['price']} x "
            f"{item['quantity']} = ₹{amount}"
        )

    line()
    print(f"Cart Total: ₹{total}")

    return total


def remove_from_cart():
    header("REMOVE FROM CART")

    if not cart:
        print("Cart is empty.")
        return

    for index, item in enumerate(cart):
        print(
            f"{index + 1}. "
            f"{item['name']} x "
            f"{item['quantity']}"
        )

    choice = int(input("Enter item number: "))

    if choice < 1 or choice > len(cart):
        print("Invalid choice.")
        return

    removed = cart.pop(choice - 1)

    print(f"{removed['name']} removed from cart.")


def calculate_discount(total):
    if total >= 50000:
        return total * 0.15

    elif total >= 25000:
        return total * 0.10

    elif total >= 10000:
        return total * 0.05

    else:
        return 0


def checkout():
    header("CHECKOUT")

    if not cart:
        print("Cart is empty.")
        return

    total = show_cart()

    discount = calculate_discount(total)

    after_discount = total - discount

    tax = after_discount * 0.18

    final_amount = after_discount + tax

    print(f"Discount: ₹{discount:.2f}")
    print(f"Tax: ₹{tax:.2f}")
    print(f"Final Amount: ₹{final_amount:.2f}")

    payment = input(
        "Payment method (cash/card/upi): "
    ).lower()

    if payment not in ["cash", "card", "upi"]:
        print("Invalid payment method.")
        return

    print("Payment successful.")

    for item in cart:
        product_id = item["id"]
        products[product_id]["stock"] -= item["quantity"]

    sale = {
        "id": random.randint(10000, 99999),
        "date": datetime.datetime.now(),
        "total": final_amount,
        "payment": payment,
        "items": cart.copy()
    }

    sales.append(sale)

    print(f"Invoice ID: {sale['id']}")

    cart.clear()

    print("Thank you for shopping!")


def show_sales():
    header("SALES HISTORY")

    if not sales:
        print("No sales available.")
        return

    for sale in sales:
        print(f"Invoice ID: {sale['id']}")
        print(f"Date: {sale['date']}")
        print(f"Amount: ₹{sale['total']:.2f}")
        print(f"Payment: {sale['payment']}")

        for item in sale["items"]:
            print(
                f"  {item['name']} x "
                f"{item['quantity']}"
            )

        line()


def sales_report():
    header("SALES REPORT")

    if not sales:
        print("No sales recorded.")
        return

    total_sales = 0
    total_items = 0

    for sale in sales:
        total_sales += sale["total"]

        for item in sale["items"]:
            total_items += item["quantity"]

    average = total_sales / len(sales)

    print(f"Total Orders: {len(sales)}")
    print(f"Items Sold: {total_items}")
    print(f"Total Revenue: ₹{total_sales:.2f}")
    print(f"Average Order: ₹{average:.2f}")


def inventory_value():
    header("INVENTORY VALUE")

    total_value = 0

    for product in products.values():
        value = product["price"] * product["stock"]
        total_value += value

    print(f"Total Inventory Value: ₹{total_value}")


def random_product():
    header("RANDOM PRODUCT")

    product_id = random.choice(list(products.keys()))

    product = products[product_id]

    print(f"Product ID: {product_id}")
    print(f"Product: {product['name']}")
    print(f"Price: ₹{product['price']}")
    print(f"Stock: {product['stock']}")


def store_statistics():
    header("STORE STATISTICS")

    total_products = len(products)
    total_customers = len(customers)
    total_sales = len(sales)

    print(f"Products: {total_products}")
    print(f"Customers: {total_customers}")
    print(f"Orders: {total_sales}")

    if sales:
        revenue = sum(sale["total"] for sale in sales)
        print(f"Revenue: ₹{revenue:.2f}")

    else:
        print("Revenue: ₹0")


def menu():
    while True:
        header(store_name)

        print("1. Show Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Low Stock Products")
        print("7. Register Customer")
        print("8. Show Customers")
        print("9. Find Customer")
        print("10. Add To Cart")
        print("11. Show Cart")
        print("12. Remove From Cart")
        print("13. Checkout")
        print("14. Sales History")
        print("15. Sales Report")
        print("16. Inventory Value")
        print("17. Random Product")
        print("18. Store Statistics")
        print("19. Exit")

        line()

        choice = input("Enter your choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            search_product()

        elif choice == "6":
            low_stock()

        elif choice == "7":
            register_customer()

        elif choice == "8":
            show_customers()

        elif choice == "9":
            find_customer()

        elif choice == "10":
            add_to_cart()

        elif choice == "11":
            show_cart()

        elif choice == "12":
            remove_from_cart()

        elif choice == "13":
            checkout()

        elif choice == "14":
            show_sales()

        elif choice == "15":
            sales_report()

        elif choice == "16":
            inventory_value()

        elif choice == "17":
            random_product()

        elif choice == "18":
            store_statistics()

        elif choice == "19":
            print("Thank you for using TechZone Store.")
            break

        else:
            print("Invalid choice. Try again.")


menu()
