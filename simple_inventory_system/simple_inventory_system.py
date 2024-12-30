# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        """
        Initializes a new product with a name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        """
        Displays the product's information (name, price, and quantity).
        """
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print("---------------------------")

    def update_quantity(self, new_quantity):
        """
        Updates the product's quantity.
        """
        self.quantity = new_quantity
        print(f"Quantity of {self.name} updated to {self.quantity}.")

    def total_value(self):
        """
        Calculates and returns the total value of the product in the inventory (price * quantity).
        """
        return self.price * self.quantity

# Define the Inventory class
class Inventory:
    def __init__(self):
        """
        Initializes the inventory as an empty list to hold products.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the inventory.
        """
        self.products.append(product)

    def display_inventory(self):
        """
        Displays information about all the products in the inventory.
        """
        if not self.products:
            print("The inventory is empty.")
        for product in self.products:
            product.display_product_info()

    def calculate_total_inventory_value(self):
        """
        Calculates the total value of all products in the inventory.
        """
        total_value = sum(product.total_value() for product in self.products)
        print(f"Total value of inventory: ${total_value:.2f}")

# Main program
def main():
    # Create an inventory system
    store_inventory = Inventory()

    # Add products to the inventory
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 20)
    product3 = Product("Headphones", 89.99, 50)

    store_inventory.add_product(product1)
    store_inventory.add_product(product2)
    store_inventory.add_product(product3)

    # Display all products in the inventory
    print("Inventory Information:")
    store_inventory.display_inventory()

    # Update quantity of a product
    product2.update_quantity(15)

    # Calculate and display the total value of the inventory
    store_inventory.calculate_total_inventory_value()

# Call the main function to run the program
if __name__ == "__main__":
    main()
