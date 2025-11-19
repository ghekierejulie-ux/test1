from os import times


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __eq__(self, other):
        if isinstance(other, Player):
            return other.name == self.name
        return False
    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.number < other.number
    def __str__(self):
        return (f"{self.name} ({self.number})")

p1 = Player("Julie Ghekiere", 10)
p2 = Player("Luk Ghekiere", 16)
p3 = Player("Cientia Cornille",15)

players = [p1, p2, p3]
print(p1)
print("p1 == p2?", p1==p2)
# Test eq
print("p1 == p2?", p1 == p2)

# Test lt via sorted()
sorted_players = sorted(players)

print("\nGesorteerde spelers:")
for p in sorted_players:
    print(p)

class Pass:
    def __init__(self, sender, receiver, nr_of_times):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times
    def get_weight(self):
        return self.nr_of_times
    def get_start(self):
        return self.sender
    def get_end(self):
        return self.receiver
    def __eq__(self, other):
        if isinstance(other, Pass) and self.receiver == other.receiver and self.sender == other.sender:
            return True
        return False
    def __str__(self):
        return (f"Pass from {self.sender} to {self.receiver}")
p1 = Player("Julie Ghekiere", 10)
p2 = Player("Luk Ghekiere", 16)
p3 = Player("Cientia Cornille",15)

pass1 = Pass(p1, p2, 5)
pass2 = Pass(p1, p3, 2)
pass3 = Pass(p3, p2, 7)

print(pass3)
print(pass1 == pass2)
print(pass1.get_weight())

class PassGraph:
    def __init__(self):
        self.players = []               # lijst van Player-objecten
        self.adj = {}                   # dict: naam → lijst met Pass-objecten

    # -----------------------
    # Basisoperaties
    # -----------------------

    def add_player(self, player):
        if not self.has_player(player):
            self.players.append(player)
            self.adj[player.name] = []  # lege lijst voor uitgaande passes

    def has_player(self, player):
        if isinstance(player, Player):
            return player in self.adj
        elif isinstance(player, str):
            return player in self.adj
        return False

    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender: Player, receiver: Player, times=1):
        if times <=0:
            raise ValueError("times must be positive")
        if not (self.has_player(sender) and self.has_player(receiver)):
            raise ValueError("sender and receiver must both be Player")

        for pas in self.adj[sender.name]:
            if pas.receiver == receiver:
                pas.nr_times += times
                return
        new_pass = Pass(sender, receiver, times)
        self.adj[sender.name].append(new_pass)

    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj:
            return None
        for pas in self.adj[sender_name]:
            if pas.receiver.name == receiver_name:
                return pas
        return None

    def neighbors(self, sender_name):
        return self.adj.get(sender_name, [])

    # -----------------------
    # Analysefuncties
    # -----------------------

    def total_weight(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        total = 0
        subset_set = set(subset)

        for sender_name in subset_set:
            for p in self.adj.get(sender_name, []):
                if p.receiver.name in subset_set:
                    total += p.nr_of_times
        return total

    def pass_intensity(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        n = len(subset)
        if n < 2:
            return 0.0

        numerator = self.total_weight(subset)
        denominator = n * (n - 1)

        return numerator / denominator

    def top_pairs(self, k=5):
        passes = []
        for player in self.players:
            for pas in self.adj[player.name]:
                passes.append((pas, pas.nr_times))
        sorted_passes = sorted(passes, key= lambda x: x[1], reverse=True)
        return sorted_passes[:k]

    def distribution_from(self, sender_name: str):
        lijst = []
        for pas in self.adj[sender_name]:
            lijst.append((pas.receiver.name, pas.nr_times))
        sorted_lijst = sorted(lijst, key= lambda x: x[1], reverse=True)
        return sorted_lijst

p1 = Player("Julie Ghekiere", 10)
p2 = Player("Luk Ghekiere", 16)
p3 = Player("Cientia Cornille", 15)
p4 = Player("Milan Vandenbossche", 9)

# PassGraph aanmaken
graph = PassGraph()

# Spelers toevoegen
graph.add_player(p1)
graph.add_player(p2)
graph.add_player(p3)
graph.add_player(p4)

# 6 passes toevoegen
graph.add_pass(p1, p2, 3)
graph.add_pass(p2, p1, 1)
graph.add_pass(p1, p3, 2)
graph.add_pass(p3, p4, 4)
graph.add_pass(p4, p1, 1)
graph.add_pass(p1, p2, 2)   # bestaande pass → wordt verhoogd

# TESTEN
print("\n--- Passes van Julie ---")
for p in graph.neighbors("Julie Ghekiere"):
    print(p, "count =", p.nr_of_times)

print("\n--- get_pass Julie -> Luk ---")
print(graph.get_pass("Julie Ghekiere", "Luk Ghekiere").nr_of_times)

print("\n--- total_weight (alle spelers) ---")
print(graph.total_weight())

print("\n--- pass_intensity (alle spelers) ---")
print(graph.pass_intensity())

print("\n--- top pairs ---")
for p in graph.top_pairs():
    print(p, "count =", p.nr_of_times)

print("\n--- distribution from Julie ---")
print(graph.distribution_from("Julie Ghekiere"))

class PassGraph:
    def __init__(self, path: str | None = None):
        self.players = []      # lijst van Player-objecten
        self.adj = {}          # dict: name → lijst van Pass-objecten

        if path is not None:
            self._load_from_txt(path)

    # --------------------------------------------------
    # DEEL 4: Opslaan & Inlezen
    # --------------------------------------------------

    def _load_from_txt(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
           	    lines = f.readlines()
        except FileNotFoundError:
            raise ValueError("Bestand niet gevonden.")

        section = None

        for line in lines:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            # Secties
            if line == "[PLAYERS]":
                section = "players"
                continue
            elif line == "[PASSES]":
                section = "passes"
                continue
            elif line.startswith("[") and line.endswith("]"):
                raise ValueError(f"Onbekende sectie: {line}")

            # Players verwerken
            if section == "players":
                if ";" not in line:
                    raise ValueError("Ongeldige speler-regel.")
                name, num = line.split(";")
                name = name.strip()
                num = num.strip()
                try:
                    num = int(num)
                except:
                    raise ValueError("Ongeldig rugnummer.")

                self.add_player(Player(name, num))

            # Passes verwerken
            elif section == "passes":
                if "->" not in line or ":" not in line:
                    raise ValueError("Ongeldige pass-regel.")

                left, nr = line.split(":")
                nr = nr.strip()
                try:
                    nr = int(nr)
                except:
                    raise ValueError("Pass-gewicht moet een getal zijn.")

                sender, receiver = left.split("->")
                sender = sender.strip()
                receiver = receiver.strip()

                s_obj = self.get_player(sender)
                r_obj = self.get_player(receiver)

                if not (s_obj and r_obj):
                    raise ValueError("Pass verwijst naar onbekende speler.")

                self.add_pass(s_obj, r_obj, nr)

            else:
                raise ValueError("Bestand zonder geldige sectie.")

    # --------------------------------------------------
    # Opslaan
    # --------------------------------------------------

    def save_to_txt(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("[PLAYERS]\n")
            for p in sorted(self.players, key=lambda x: x.name):
                f.write(f"{p.name};{p.number}\n")

            f.write("[PASSES]\n")
            for sender_name in sorted(self.adj.keys()):
                for p in self.adj[sender_name]:
                    f.write(f"{p.sender.name} -> {p.receiver.name} : {p.nr_of_times}\n")
print("=== TEST: DEEL 4 ===")

# 1. PassGraph opbouwen
g = PassGraph()

p1 = Player("Julie Ghekiere", 10)
p2 = Player("Luk Ghekiere", 16)
p3 = Player("Cientia Cornille", 15)
p4 = Player("Milan VDB", 9)

g.add_player(p1)
g.add_player(p2)
g.add_player(p3)
g.add_player(p4)

g.add_pass(p1, p2, 3)
g.add_pass(p1, p2, 2)  # zelfde pass → verhoogt
g.add_pass(p2, p3, 1)
g.add_pass(p3, p4, 4)
g.add_pass(p4, p1, 1)

# 2. Opslaan
g.save_to_txt("team.txt")
print("team.txt opgeslagen.")

# 3. Inlezen via constructor
g2 = PassGraph("team.txt")
print("team.txt opnieuw ingelezen!")

# 4. Check data
print("\nSpelers in g2:")
for p in g2.get_players():
    print(" -", p)

print("\nPasses in g2:")
for p in g2.passes():
    print(f"{p.sender.name} -> {p.receiver.name} = {p.nr_of_times}")




