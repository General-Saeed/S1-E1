from datetime import datetime, timedelta

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self._price = price
        self.__quantity = quantity

    def calculate_value(self):
        return self._price * self.__quantity

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__product_id

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return f"ID: {self.__product_id} | Name: {self.__name} | Val: {self.calculate_value():.2f}"


class PerishableProduct(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date, storage_temperature):
        super().__init__(product_id, name, price, quantity)
        self.__expiry_date = expiry_date
        self.__storage_temperature = storage_temperature

    def calculate_value(self):
        base_value = self._price * self.get_quantity()
        days_remaining = (self.__expiry_date - datetime.now()).days
        
        if days_remaining < 3:
            return base_value * 0.80
        return base_value


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, quantity, warranty_period, power_consumption):
        super().__init__(product_id, name, price, quantity)
        self.__warranty_period = warranty_period
        self.__power_consumption = power_consumption

    def calculate_value(self):
        base_value = self._price * self.get_quantity()
        tax_rate = 0.09
        return base_value * (1 + tax_rate)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.get_name()}' added to inventory.")

    def get_total_inventory_value(self):
        total = 0
        for p in self.products:
            total += p.calculate_value()
        return total

    def find_product_by_name(self, name):
        found_items = [p for p in self.products if name.lower() in p.get_name().lower()]
        return found_items

    def show_inventory(self):
        print("\n--- Inventory List ---")
        for p in self.products:
            print(p)


if __name__ == "__main__":
    inventory = Inventory()

    p1 = Product(101, "Simple Notebook", 50000, 10)

    expiry_soon = datetime.now() + timedelta(days=1)
    p2 = PerishableProduct(201, "Fresh Milk", 20000, 50, expiry_soon, 4)

    p3 = ElectronicProduct(301, "Gaming Laptop", 35000000, 2, "2 Years", "250W")

    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)

    inventory.show_inventory()

    total_value = inventory.get_total_inventory_value()
    print(f"\nTotal inventory value: {total_value:,.0f} Toman")

    print("\nSearch results for 'Laptop':")
    results = inventory.find_product_by_name("Laptop")
    for item in results:
        print(item)
