import csv
from collections import Counter


def import_data(path):
    with open(path) as file:
        reader_file = csv.reader(file)
        data = [row for row in reader_file]
    return data


def most_frequent_order(data, customer):
    count_orders = []
    for info in data:
        if info[0] == customer:
            count_orders.append(info[1])
    most_frequent_maria = Counter(count_orders).most_common()[0][0]
    return most_frequent_maria


def quantity_arnaldo_order_hamburguer(data):
    quantity_arnaldo = 0
    for a, b, c in data:
        if a == 'arnaldo' and b == 'hamburguer':
            quantity_arnaldo += 1
    print(quantity_arnaldo)
    return quantity_arnaldo


def never_ordered(data, customer):
    menu = set(['hamburguer', 'pizza', 'coxinha', 'misto-quente'])
    menu_customer = set()
    for a, b, c in data:
        if a == customer:
            menu_customer.add(b)
    return menu.difference(menu_customer)


def days_not(data, customer):
    week = set(['segunda-feira', 'terça-feira', 'sabado'])
    days_customer = set()
    for a, b, c in data:
        if a == customer:
            days_customer.add(c)
    return week.difference(days_customer)


def analyze_log(path_to_file):
    if "csv" not in path_to_file:
        raise FileNotFoundError(f'Extensão inválida {path_to_file}')

    try:
        data = import_data(path_to_file)
        with open('data/mkt_campaign.txt', 'w') as mkt_campaign:
            mkt_campaign.write(f"{most_frequent_order(data, 'maria')}\n")
            mkt_campaign.write(f"{quantity_arnaldo_order_hamburguer(data)}\n")
            mkt_campaign.write(f"{never_ordered(data, 'joao')}\n")
            mkt_campaign.write(f"{days_not(data, 'joao')}\n")
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente {path_to_file}')
