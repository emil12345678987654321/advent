import re

if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/5/data.txt') as f:
        contents = f.read()
        inventory, moves = contents.split('\n\n')
        inventory_row = inventory.split('\n')
        for idx, line in enumerate(inventory_row):
            location = ([line[i:i+4] for i in range(0, len(line), 4)])

