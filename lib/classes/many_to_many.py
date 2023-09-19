class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self.customers_list = []
        
    def orders(self):
        return self.orders_list
    
    def customers(self):
        return self.customers_list
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            print('Error')
        elif type(name) == str and len(name) >= 3:
            self._name = name

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders_list = []
        self.coffees_list = []
        
    def orders(self):
        return self.orders_list
    
    def coffees(self):
        return self.coffees_list
    
    def create_order(self, coffee, price):
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <=15:
            self._name = name
        else:
            print('Error')
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        self.coffee.orders_list.append(self)
        self.customer.orders_list.append(self)
        
        if not (customer in self.coffee.customers_list):
            self.coffee.customers_list.append(customer)
        
        if not (coffee in self.customer.coffees_list):
            self.customer.coffees_list.append(coffee)

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            print('Error')
        elif type(price) == float and 1.0 <= price <= 10.0:
            self._price = price
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if type(customer) == Customer:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if type(coffee) == Coffee:
            self._coffee = coffee