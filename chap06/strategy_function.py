# -*- coding: utf-8 -*-
from chap06.promotions import best_promo
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class ListItem:

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
        self.cart = cart
        self.promotion = promotion

    @property
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total for item in self.cart)
        return self.__total

    @property
    def discount(self):
        if not hasattr(self, '__discount'):
            self.__discount = self.promotion(self)
        return self.__discount

    @property
    def due(self):
        return self.total - self.discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} discount: {:.2f} due: {:.2f}'
        return fmt.format(self.total, self.discount, self.due)


if __name__ == '__main__':
    joe = Customer('joe', 300)
    tom = Customer('tom', 10000)
    banana_cart = [ListItem('banana', 1000, 0.5), ListItem('milk', 300, 5.5)]
    adult_cart = [ListItem('durex', 30, 10), ListItem('orcodo', 10, 20)]
    order_1 = Order(joe, banana_cart, best_promo)
    order_2 = Order(tom, adult_cart, best_promo)
    print(order_1)
    print(order_2)
