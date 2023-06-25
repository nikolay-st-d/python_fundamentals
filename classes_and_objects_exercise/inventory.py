class Inventory:

    items = []

    def __init__(self, __capacity):
        self.__capacity = __capacity

    def add_item(self, item: str):
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(Inventory.items)
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {left_capacity}"

# test code
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)