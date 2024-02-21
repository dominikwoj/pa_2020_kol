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
        if [0] == self.color_table:
            self.color_name = 'white'
        elif [0, 1] == self.color_table:
            self.color_name = 'yellow'
        elif [0, 2] == self.color_table:
            self.color_name = 'blue'
        elif [0, 3] == self.color_table:
            self.color_name = 'red'
        elif [0, 1, 2] == self.color_table:
            self.color_name = 'green'
            green = True
        elif [0, 1, 3] == self.color_table:
            self.color_name = 'orange'
        elif [0, 2, 3] == self.color_table:
            self.color_name = 'purple'
        elif [0, 1, 2, 3] == self.color_table:
            self.color_name = 'brown'
        return green


# @profile()
def read_data():
    rows = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append([int(i) for i in str(row[0]).split(' ')])
    return rows


# @profile()
def main():
    data = read_data()
    # print(data)
    can_count, operation_count = data[0]
    print(f'{can_count} {operation_count}')
    can_set = [Can() for i in range(can_count)]
    for i in range(operation_count):
        c_start, c_stop, color = data[i + 1]
        # print(f'opeation: {i + 1}|can: {c_start}->{c_stop}|color={color}')
        for c in range(c_start - 1, c_stop):
            can_set[c].add_color(color)
    print([can_set[i].name_color() for i in range(can_count)].count(True))


if __name__ == '__main__':
    main()
