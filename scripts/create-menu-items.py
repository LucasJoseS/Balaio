#!/usr/bin/python

def insert(container: dict, key: str, value: dict):
    if key in container.keys():
        container[key].append(value)
    else:
        container[key] = [value]

def flat(container: dict):
    for key in container.keys():
        if len(container[key]) == 1:
            container[key] = container[key][0]

if __name__ == "__main__":
    import csv
    import json

    menu = dict()
    with open('data/menu.csv') as csv_f:
        reader = csv.DictReader(csv_f, skipinitialspace=True)

        for row in reader:
            insert(menu, row.get("GROUP"), {"name": row.get("NAME"), "cost": row.get("COST"), "desc": row.get("DESC")})

        flat(menu)
        with open('menu/src/scipts/menu-itens.json', 'w') as writer:
            json.dump(menu, writer, ensure_ascii=False, indent=True)

