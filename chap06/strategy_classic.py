# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    @property
    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promition = promotion

    @property
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total for item in self.cart)
        return self.__total

    @property
    def discount(self):
        if not hasattr(self, '__discount'):
            if self.promition is None:
                self.__discount = 0
            else:
                self.__discount = self.promition.discount(self)
        return self.__discount

    @property
    def due(self):
        return self.total - self.discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} discount: {:.2f} due: {:.2f}'
        return fmt.format(self.total, self.discount, self.due)


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """7% discount for orders with 7 or more distinct items"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 7:
            return order.total * 0.07
        return 0


if __name__ == '__main__':
    joe = Customer(name='John Doe', fidelity=0)
    ann = Customer(name='Ann Smith', fidelity=1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermallon', 5, 5.0)]
    order_a = Order(joe, cart, FidelityPromo())
    order_b = Order(ann, cart, FidelityPromo())
    print(order_a)
    print(order_b)
