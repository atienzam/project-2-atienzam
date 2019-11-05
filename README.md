# project-2

**[70 pts]**  You will be writing a (rather primitive) online store simulator. It will have three classes: Product, Customer and Store. All data members of each class should be marked as private and the classes should have any get or set methods that will be needed to access them. Here are descriptions of methods for the three classes:

**Product:**

A Product object represents a product with an ID code, title, description, price and quantity available.

* init method - takes as parameters five values with which to initialize the Product's id_code, title, description, price, and quantity_available.
* get methods for each of the data members, named get_id_code, get_title, get_description, get_price, and get_quantity_available
* decrease_quantity - decreases the quantity available by one

**Customer:**

A Customer object represents a customer with a name and account ID. Customers must be members of the Store to make a purchase. Premium members get free shipping.

* init method - takes as parameters three values with which to initialize the Customer's name, account_ID, and whether the customer is a premium_member. 
* you decide how to represent a Customer's cart
* get methods named get_name and get_account_ID
* is_premium_member - returns whether the customer is a premium member
* add_product_to_cart - adds the product ID code to the Customer's cart
* empty_cart - empties the Customer's cart

**Store:**

A Store object represents a store, which has some number of products in its inventory and some number of customers as members.

* **you** decide how to represent a Store's inventory and members
* init method - whatever initialization needs to be done for your Store
* add_product - adds a product to the inventory
* add_member - adds a customer to the members
* get_product_from_ID - returns the Product with the matching ID. If no matching ID is found, it returns the special value None
* get_member_from_ID - returns the Customer with the matching ID. If no matching ID is found, it returns the special value None
* product_search - return a sorted list of ID codes for every product whose title or description contains the search string. The first letter of the search string should be case-insensitive, i.e. a search for "wood" should match Products that have "Wood" in their title or description, and a search for "Wood" should match Products that have "wood" in their title or description. You may assume that the search string will consist of a single word.
* add_product_to_member_cart - If the product isn't found in the inventory, return "product ID not found". If the product was found, but the member isn't found in the members, return "member ID not found". If both are found and the product is still available, call the member's addProductToCart method to add the product and then return "product added to cart". If the product was not still available, return "product out of stock". This function does not need to check how many of that product are available - just that there is at least one. It should not change how many are available - that happens during checkout. The same product can be added multiple times if the customer wants more than one of something.
* check_out_member - If the member ID isn't found, raise an **InvalidCheckoutError** (you'll need to define this exception class). Otherwise return the charge for the member's cart. This will be the total cost of all the items in the cart, not including any items that are not in the inventory or are out of stock, plus the shipping cost. If a product is not out of stock, you should add its cost to the total and decrease the available quantity of that product by 1. Note that it is possible for an item to go out of stock during checkout. For example, if the customer has two of the same product in their cart, but the store only has one of that product left, the customer will be able to buy the one that's available, but won't be able to buy a second one, because it's now out of stock. For premium members, the shipping cost is $0. For normal members, the shipping cost is 7% of the total cost of the items in the cart. When the charge for the member's cart has been tabulated, the member's cart should be emptied, and the charge amount returned.

**[10 pts]**  You must include a main function that runs if the file is run as a script, but not if the file is imported.  The main function should try to check out a member.  If an InvalidCheckoutError is raised, an explanatory message should be printed for the user (otherwise the checkout should proceed normally).

**[20 pts]**  In addition to your file containing the code for the above classes, you must also submit a file that contains unit tests for your Store.py file.  It must have at least five unit tests and use at least three different assert functions.

**Gradescope will not test your main function or unit tests - the TAs will take care of that.**

Your files must be named: **Store.py** and **StoreTester.py**
