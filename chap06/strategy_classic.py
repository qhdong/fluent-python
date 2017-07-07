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
                self.__discount = self.promition(self)
        return self.__discount

    @property
    def due(self):
        return self.total - self.discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} discount: {:.2f} due: {:.2f}'
        return fmt.format(self.total, self.discount, self.due)


promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def buik_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total * 0.1
    return discount


@promotion
def large_order(order):
    """7% discount for orders with 7 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 7:
        return order.total * 0.07
    return 0


def best_promo(order):
    """select best discount available"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer(name='John Doe', fidelity=0)
    ann = Customer(name='Ann Smith', fidelity=1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermallon', 5, 5.0)]
    order_a = Order(joe, cart, best_promo)
    order_b = Order(ann, cart, best_promo)
    print(order_a)
    print(order_b)
