class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"{species} in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"{species} in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"{species} in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for _ in range(n):
    animal = input().split()
    animal_species = animal[0]
    animal_name = animal[1]
    zoo.add_animal(animal_species, animal_name)

species_name = input()
print(zoo.get_info(species_name))