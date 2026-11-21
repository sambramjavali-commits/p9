import sys
def product_details(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: Rs. {price}"
    )

if __name__ == "__main__":
    pid = int(sys.argv[1])
    name = input("name:")
    quantity = int(sys.argv[3])
    price = float(sys.argv[4])

    print(product_details(pid, name, quantity, price))

