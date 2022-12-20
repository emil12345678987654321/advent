import numpy as np

if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/8/exampledata.txt') as f:

        def check_visibility(height, x, y):
            # if x == 0 or x == len(y_axis[0]) - 1 or y == 0 or y == len(y_axis) - 1:
            if x == 0 or x == 98 or y == 0 or y == 98:
                return True
            # elif height > np.array(y_axis[y+1:][x]) and height > np.array(y_axis[y-1:][x]) and height > np.array(y_axis[y][x+1:]) and height > np.array(y_axis[y][x-1:]):
            elif all(i < height for i in y_axis[y+1:][x]) \
                    and height > all(i < height for i in y_axis[y-1:][x])\
                    and height > all(i < height for i in y_axis[y][x+1:])\
                    gitand height > all(i < height for i in y_axis[y][x-1:]):
                print(y_axis[y])
                print("height", height)
                print("up", y_axis[y+1][x])
                print("down", y_axis[y-1][x])
                print("right", y_axis[y][x+1])
                print("left", y_axis[y][x-1])
                return True
            else:
                return False

        content = f.read().split('\n')
        y_axis = []
        visible_trees_counter = 0

        for line in content:
            x_axis = [line[i:i + 1] for i in range(0, len(line), 1)]
            y_axis.append(x_axis)

        for y, line in enumerate(y_axis):
            for x, height in enumerate(line):
                if check_visibility(height, x, y):
                    visible_trees_counter += 1

        print(visible_trees_counter)
