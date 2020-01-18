# Author: Marc Atienza
# Date: 1/18/2020
# Description: Unfortunately I ran out of time and I was not able to finish the project. I mistakenly mixed the due
# dates up in my calendar and as a result I did not give myself enough time to complete the assignment.

import re


class Product:
    # constructor for product attributes
    def __init__(self, id_code, title, description, price, quantity_available):
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):                          # gets product id
        return self._id_code

    def get_title(self):                            # gets product title
        return self._title

    def get_description(self):                      # gets product description
        return self._description

    def get_price(self):                            # gets the price of product
        return self._price

    def get_quantity_available(self):               # gets the quantity of the product
        return self._quantity_available

    def decrease_quantity(self):                    # subtracts the quantity of the product by 1
        self._quantity_available = self._quantity_available - 1
        return self._quantity_available


class Customer:
    # constructor for name and membership
    def __init__(self, name, account_ID, premium_member):
        self._name = name
        self._account_ID = account_ID
        self._premium_member = premium_member
        self.cart = []

    def get_name(self):                 # gets name of person
        return self._name

    def get_account_ID(self):           # gets the id of person
        return self._account_ID

    def is_premium_member(self):        # returns membership status
        return self._premium_member

    def add_product_to_cart(self, id_code):     # adds id_code of item to cart
        self.cart.append(id_code)

    def empty_cart(self):                       # empties the cart
        self.cart = []


class InvalidCheckoutError(BaseException):
    pass


class Store:
    # constructor for creating the inventory and membership list
    def __init__(self):
        self.inventory = []
        self.members = []

    def add_product(self, product):                 # adds item into inventory list
        self.inventory.append(product)

    def add_member(self, member):                   # adds person to member list
        self.members.append(member)

    def get_product_from_ID(self, id_code):         # grabs the product using the id_code
        for item in self.inventory:
            if id_code == item.get_id_code():
                return item
            return None

    def get_member_from_ID(self, account_ID):       # gets customer's account id
        for person in self.members:
            if person.get_account_ID == account_ID:
                return person
            return None

    def product_search(self, enter):                # searches using word entered by customer and returns id of items
        id_list = []
        for item in self.inventory:
            if re.search(enter, item.get_title(), re.IGNORECASE) or re.search(enter, item.get_description(),
                                                                              re.IGNORECASE):
                id_list.append(item.get_id_code)
            return id_list.sort()

    def add_product_to_member_cart(self, product_id, member_id):    # adds product to cart unless product id or member
        product = self.get_product_from_ID(product_id)              # id is not found or product is out of stock
        member = self.get_member_from_ID(member_id)

        if product is None:
            return "product ID not found"
        if member is None:
            return "member ID not found"
        if product.get_quantity_available() > 0:
            member.add_product_to_cart(product_id)
            return "product added to cart"
        else:
            return "product out of stock"

    def check_out_member(self, member_id):                         # checkout person and calculates total
        customer = self.get_member_from_ID(member_id)              # if customer not member invalid checkout mssg popup

        if customer is None:
            raise InvalidCheckoutError()
        else:
            total = 0.00
            for item in self.cart():
                product = self.get_product_from_ID(item)
                if product.get_quantity_available() > 0:
                    product.decrease_quantity()
                    total = product.price()
                if not customer.is_premium_member():
                    total = total + (total * 0.07)
                    return total

    if __name__ == '__main__':
        # product being sold at store with prod id number, item being sold, description, price, and stock
        p1 = Product("130", "Stephen Curry Jersey", "Play like your favorite nba pro.", 89.99, 3)
        # customer created with name, account id, and premium member status
        c1 = Customer("Marc", "MRA", False)

        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("130", "MRA")
        result = myStore.check_out_member("MRA")

        try:
            myStore.check_out_member("MRA")
        except InvalidCheckoutError:
            print("Sorry, you have to be a member in order to checkout.")
