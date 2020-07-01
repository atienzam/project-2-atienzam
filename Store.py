# Author: Marc Atienza
# Date: 6/30/2020
# Description: This program represents an online store simulator. It's broken down into three classes: Product,
# Customer, and Store.
import re


class Product:

    def __init__(self, prod_id, title, description, price, quantity_available):
        self.__prod_id = prod_id
        self.__title = title
        self.__description = description
        self.__price = price
        self.__quantity_available = quantity_available

    def get_product_id(self):
        """gets product id"""
        return self.__prod_id

    def get_title(self):
        """gets product title"""
        return self.__title

    def get_description(self):
        """gets description of item"""
        return self.__description

    def get_price(self):
        """gets the price of the object"""
        return self.__price

    def quantity_available(self):
        """gets the quantity of the product"""
        return self.__quantity_available

    def decrease_quantity(self):
        """decreases the inventory quantity by 1"""
        return self.__quantity_available - 1


class Customer:
    def __init__(self, name, customer_id, premium_member):
        self.__name = name
        self.__customer_id = customer_id
        self.__premium_member = premium_member
        self.cart = []

    def get_name(self):
        """gets the name of user"""
        return self.__name

    def get_customer_id(self):
        """gets the id of user"""
        return self.__customer_id

    def is_premium_member(self):
        """returns the membership status"""
        return self.__premium_member

    def add_product_to_cart(self):
        """takes product ID code and adds it to the customer's cart"""
        prod_id = Product.get_product_id
        return self.cart.append(prod_id)

    def empty_cart(self):
        """empties the cart"""
        return self.cart.clear()


class InvalidCheckoutError(Exception):
    pass


class Store:

    def __init__(self):
        self.__inventory = []
        self.__membership = []

    def add_product(self, product):
        """adds product object to inventory list"""
        self.__inventory.append(product)

    def add_member(self, member):
        """adds customer object to membership list"""
        self.__membership.append(member)

    def get_product_from_id(self, prod_id):
        """returns product based on the id it received"""
        for item in self.__inventory:
            if prod_id == item.get_product_id:
                return item
            return None

    def get_member_from_id(self, account_id):
        """returns customer based on id received"""
        for person in self.__membership:
            if account_id == person.get_customer_id:
                return person
            return None

    def product_search(self, search_string):
        """searches for product through name or description entered by the user"""
        id_list = []
        for i in self.__inventory:
            if re.search(search_string, i.Product.get_title(), re.IGNORECASE) or re.search(search_string,
                                                                                           i.Product.get_description(),
                                                                                           re.IGNORECASE):
                id_list.append(i.Product.get_product_id())
                return id_list.sort()
            else:
                return id_list.clear()

    def add_product_to_member_cart(self, product_id, customer_id):
        """adds product to cart as long as product id and member id is found and product is in stock """
        product = self.get_product_from_id(product_id)
        customer = self.get_member_from_id(customer_id)

        if product is None:
            return print("product ID not found")
        elif customer is None:
            return print("member ID not found")
        else:
            if product.Product.quantity_available() > 0:
                customer.Customer.add_product_to_cart()
                return print("product added to cart")
            else:
                return print("product out of stock")

    def check_out_member(self, account_id):
        """ checks out person and calculates total, if customer is not a member invalid checkout mssg appears"""
        member = self.get_member_from_id(account_id)

        if member is None:
            raise InvalidCheckoutError()
        else:
            total = 0.00
            for item in member.Customer.add_product_to_cart():
                product = self.get_product_from_id(item)
                if product.Product.quantity_available() > 0:
                    product.Product.decrease_quantity()
                    total = product.Product.get_price()
                if not member.Customer.is_premium_member():
                    total = total + (total * 0.07)
                    return total


def main():
    p1 = Product("130", "Stephen Curry Jersey", "Play like your favorite nba pro.", 89.99, 3)
    c1 = Customer("Marc", "MRA", True)

    myStore = Store()
    myStore.add_product(p1)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("130", "MRA")

    try:
        myStore.check_out_member("MRA")
    except InvalidCheckoutError:
        print("Sorry, you have to be a member in order to checkout.")
    else:
        myStore.check_out_member("MRA")


if __name__ == '__main__':
    main()
