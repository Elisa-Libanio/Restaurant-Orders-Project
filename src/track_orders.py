from src.analyze_log import (most_frequent_order, never_ordered, days_not)
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return most_frequent_order(self.orders, customer)

    def get_never_ordered_per_customer(self, customer):
        return never_ordered(self.orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return days_not(self.orders, customer)

    def get_busiest_day(self):
        days = [item[2] for item in self.orders]
        busiest_day = Counter(days).most_common()[0][0]
        return busiest_day

    def get_least_busy_day(self):
        days = [item[2] for item in self.orders]
        least_day = Counter(days).most_common()[-1][0]
        return least_day

 