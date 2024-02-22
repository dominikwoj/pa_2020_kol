#from more_itertools import ilen
import csv
from memory_profiler import profile


class Can:
    def __init__(self):
        self.color_table = [0]  # white
        self.color_name = None


    def add_color(self, color):
        self.color_table.append(color)


    def name_color(self):
        self.color_table = list(dict.fromkeys(self.color_table))  # remove duplicates !!
        self.color_table.sort()
        green = False
        # if [0] == self.color_table:
        #     self.color_name = 'white'
        # elif [0, 1] == self.color_table:
        #     self.color_name = 'yellow'
        # elif [0, 2] == self.color_table:
        #     self.color_name = 'blue'
        # elif [0, 3] == self.color_table:
        #     self.color_name = 'red'
        # elif [0, 1, 2] == self.color_table:
        #     self.color_name = 'green'
        #     green = True
        # elif [0, 1, 3] == self.color_table:
        #     self.color_name = 'orange'
        # elif [0, 2, 3] == self.color_table:
        #     self.color_name = 'purple'
        # elif [0, 1, 2, 3] == self.color_table:
        #     self.color_name = 'brown'
        # return green
        return True if [0, 1, 2] == self.color_table else False

def name_color(color_table):
    color_table = list(dict.fromkeys(color_table))  # remove duplicates !!
    color_table.sort()
    color_name = ''
    green = False
    if [0] == color_table:
        color_name = 'white'
    elif [0, 1] == color_table:
        color_name = 'yellow'
    elif [0, 2] == color_table:
        color_name = 'blue'
    elif [0, 3] == color_table:
        color_name = 'red'
    elif [0, 1, 2] == color_table:
        color_name = 'green'
        green = True
    elif [0, 1, 3] == color_table:
        color_name = 'orange'
    elif [0, 2, 3] == color_table:
        color_name = 'purple'
    elif [0, 1, 2, 3] == color_table:
        color_name = 'brown'
    return green


#@profile()
def read_data():
    rows = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append([int(i) for i in str(row[0]).split(' ')])
    return rows


#@profile()
def main():
    data = read_data()
    #print(data)
    can_count, operation_count = data[0]
    print(f'{can_count} {operation_count}')
    can_set = [Can() for i in range(can_count)]
    for i in range(operation_count):
        c_start, c_stop, color = data[i + 1]
        #print(f'opeation: {i + 1}|can: {c_start}->{c_stop}|color={color}')
        for c in range(c_start - 1, c_stop):
            can_set[c].add_color(color)
    #print([can_set[i].name_color() for i in range(can_count)].count(True))
    # out = 0
    # for i in range(can_count):
    #     out += 1 if can_set[i].name_color() == True else 0
    # print(out)
    #print([name_color(can_set[i].color_table) for i in range(can_count)].count(True))

    # out = (can_set[i].name_color() for i in range(can_count)).count(True)
    #out = list((can_set[i].name_color() for i in range(can_count)))
    # out = (lambda True if[0, 1, 2] == i.else False for i in range(can_count))
    #print(can_set)
    [print(i.color_table) for i in can_set]
    #out = filter(lambda i: list(dict.fromkeys(i.color_table)) == [0, 1, 2], can_set)
    #out = [i for i in can_set if list(dict.fromkeys(i.color_table)) == [0, 1, 2]]
    out = (i for i in can_set if list(dict.fromkeys(i.color_table)) == [0, 1, 2])
    print(f'{len(can_set)}\n{out}\n{list(out)}\n{len(list(out))}\n{list(out).__len__}') # len(out) == 0 <- !!!
    [print(i.color_table) for i in list(out)]
    # for i in list(out):
    #     print(i.color_table)
    #print(out.count(True))
    #print(out)

    # out_table = [can_set[i].name_color() for i in range(can_count)]
    # print(out_table)

if __name__ == '__main__':
    main()