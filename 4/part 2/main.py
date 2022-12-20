if __name__ == '__main__':
    def a_overlapping_b(range_a, range_b):
        a_start, a_end = range_a.split('-')
        b_start, b_end = range_b.split('-')
        if int(b_start) <= int(a_start) <= int(b_end):
            return True

    with open('C:/Users/Emil/PycharmProjects/advent/4/data.txt') as f:
        counter = 0
        contents = f.read().split()
        for line in contents:
            range_a, range_b = line.split(',')
            if a_overlapping_b(range_a, range_b) or a_overlapping_b(range_b, range_a):
                counter += 1
        print(counter)
