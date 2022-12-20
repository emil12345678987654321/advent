if __name__ == '__main__':
    with open('C:/Users/Emil/PycharmProjects/advent/2/data.txt') as f:
        contents = f.read()
        game = contents.split('\n')
        score = 0
        for item in game:
            opponent = item[0]
            me = item[2]
            match opponent:
                case 'A':
                    match me:
                        case 'X':
                            score += 3
                        case 'Y':
                            score += 4
                        case 'Z':
                            score += 8
                case 'B':
                    match me:
                        case 'X':
                            score += 1
                        case 'Y':
                            score += 5
                        case 'Z':
                            score += 9
                case 'C':
                    match me:
                        case 'X':
                            score += 2
                        case 'Y':
                            score += 6
                        case 'Z':
                            score += 7
        print(score)
