if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/6/data.txt') as f:
        contents = f.read()
        move = True
        start, stop = 0, 14
        while move:
            message = contents[start:stop]
            unique = ''.join(set(message))
            if len(unique) == 14:
                move = False
                print(stop)
            start += 1
            stop += 1
