# -*- coding: utf-8 -*-


class Average:
    def __init__(self):
        self.series = []
        self.total = 0

    def __call__(self, new_val):
        self.series.append(new_val)
        self.total += new_val
        return self.total / len(self.series)


