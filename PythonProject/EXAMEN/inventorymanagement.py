import random

class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def __str__(self):
        return f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})"


class Product:
    def __init__(self, product_name, holding_cost, stockout_penalty):
        self.product_name = product_name
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty
        self.batches = []   # <-- BELANGRIJK


    def add_batch(self, quantity, cost_per_unit):
        batch = Batch(quantity, cost_per_unit)
        self.batches.append(batch)

    def fulfill_demand(self, demand):
        while demand > 0 and len(self.batches) > 0:
            top_batch = self.batches[-1]

            if top_batch.quantity > demand:
                top_batch.quantity -= demand
                return 0
            else:
                demand -= top_batch.quantity
                self.batches.pop()

        if demand > 0:
            return demand * self.stockout_penalty
        return 0

    def calculate_holding_cost(self):
        total = 0
        for batch in self.batches:
            total += batch.cost_per_unit * self.holding_cost
        return total

    def __str__(self):
        result = f"Product {self.product_name}:\n"
        for batch in reversed(self.batches):
            result += str(batch) + "\n"
        return result.strip()


class Inventory_manager:
    def __init__(self):
        self.inventory = {}  # dictionary: {product_name: Product}

    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.inventory:
            print(f"Product {product_name} already exists")
        else:
            self.inventory[product_name] = Product(product_name, holding_cost, stockout_penalty)

    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name not in self.inventory:
            print(f"Product {product_name} not found")
        else:
            self.inventory[product_name].add_batch(quantity, cost_per_unit)

    def simulate_demand(self, min_demand=0, max_demand=20):
        demand = {}
        for name in self.inventory:
            demand[name] = random.randint(min_demand, max_demand)
        return demand

    def simulate_day(self, demand_dict):
        total_penalty = 0
        total_holding = 0
        for name, demand in demand_dict.items():
            product = self.inventory[name]
            total_penalty += product.fulfill_demand(demand)
            total_holding += product.calculate_holding_cost()

        return total_penalty + total_holding

    def save_to_csv(self, filename):
        with open(filename, "w") as f:
            f.write("product_name,batch_quantity,batch_cost_per_unit\n")
            for product_name, product in self.inventory.items():
                for batch in product.batches:
                    f.write(f"{product_name},{batch.quantity},{batch.cost_per_unit}\n")

    def load_from_csv(self, filename):
        with open(filename, "r") as f:
            f.readline()  # skip header
            for line in f:
                product_name, quantity, cost_per_unit = line.strip().split(",")
                quantity = int(quantity)
                cost_per_unit = float(cost_per_unit)

                if product_name not in self.inventory:
                    self.inventory[product_name] = Product(product_name, 0, 0)

                self.inventory[product_name].add_batch(quantity, cost_per_unit)

    def print_inventory(self):
        print("Current Inventory:")
        for product in self.inventory.values():
            print(product)
            print()


# MAIN los van de klasse
def main():
    manager = Inventory_manager()
    manager.add_product("Widget", 1, 10)
    manager.add_product("Gadget", 2, 5)

    manager.restock_product("Widget", 100, 2.5)
    manager.restock_product("Widget", 50, 2.0)
    manager.restock_product("Gadget", 70, 3.0)

    demand = manager.simulate_demand()
    print(demand)

    print("Costs today:", manager.simulate_day(demand))
    manager.print_inventory()
    manager.save_to_csv("inventory.csv")


# main()






