import random
import csv

class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def __str__(self):
        return (f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})")

class Product:
    def __init__(self, product_name, batches, holding_cost, stockout_penalty): #batches niet meegeven, want bij start is dit leeg
        self.product_name = product_name
        self.batches = []      # dit is de STACK
        self.holding_cost = holding_cost
        self.stockout_penalty = stockout_penalty

    def add_batch(self, quantity, cost_per_unit):
        batch = Batch(quantity, cost_per_unit)
        self.batches.append(batch)   # LIFO: bovenaan stack

    def fulfill_demand(self, demand):
        remaining_demand = demand

        while remaining_demand > 0 and len(self.batches) > 0:
            top_batch = self.batches[-1]   # bovenste batch

            if top_batch.quantity > remaining_demand:
                # batch heeft genoeg voorraad
                top_batch.quantity -= remaining_demand
                return 0    # volledig geleverd → geen penalty

            else:
                # batch is onvoldoende → gebruik alles
                remaining_demand -= top_batch.quantity
                self.batches.pop()         # verwijder deze batch


        # Na loop: als er nog vraag over is → stockout
        if remaining_demand > 0:
            return remaining_demand * self.stockout_penalty

        return 0
    def calculate_holding_cost(self):
        total = 0
        for batch in self.batches:
            total += batch.quantity * self.holding_cost
        return total

    def __str__(self):
        result = f"Product [{self.product_name}]:\n"
        for batch in reversed(self.batches): #want stack dus anders krijg je ..., batch3, batch2, batch1
            result += str(batch) + "\n"
        return result.strip() #De laatste \n is ongewenst → want dat veroorzaakt een lege lijn onderaan.

class Inventory_Manager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.inventory:
            print(f"Product {product_name} already exists")

        self.inventory[product_name] = Product(product_name, holding_cost, stockout_penalty)

    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name not in self.inventory:
            print(f"Product [{product_name}] not found")
            return
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
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["product_name", "batch_quantity", "batch_cost_per_unit"])

            for name, product in self.inventory.items():
                for batch in product.batches:
                    writer.writerow([name, batch.quantity, batch.cost_per_unit])

    def load_from_csv(self, filename):
        with open(filename, newline="") as f: ##with zorgt ervoor dat het bestand automatisch wordt gesloten, f is een bestandsobject, waarmee we kunnen lezen
            reader = csv.DictReader(f) #maakt van elke rij een woordenboek
            for row in reader:
                name = row["product_name"]
                q = int(row["batch_quantity"])
                c = float(row["batch_cost_per_unit"])

                if name not in self.inventory:
                    # Default costs (unknown in CSV, so set to 0)
                    self.inventory[name] = Product(name, 0, 0)

                self.inventory[name].add_batch(q, c)

    def print_inventory(self):
        print("Current Inventory:")
        for product in self.inventory.values():
            print(product)

def main():
        manager = Inventory_Manager()
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



