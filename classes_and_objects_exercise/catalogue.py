class Catalogue:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        filtered_list = []
        for product in self.products:
            if product[0].lower() == first_letter.lower():
                filtered_list.append(product)
        return filtered_list

    def __repr__(self):
        sorted_products = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{sorted_products}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)