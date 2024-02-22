import csv
from memory_profiler import profile


class Can:
    def __init__(self):
        self.color_table = [0]  # white
        self.color_name = None

    def add_color(self, color):
        self.color_table.append(color)


# @profile()
def read_data(file_name):
    rows = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append([int(i) for i in str(row[0]).split(' ')])
    return rows


# @profile()
def main():
    #data = read_data(file_name='data.csv')
    #data = read_data(file_name='data1h1h.csv')
    #data = read_data(file_name='data1k1k.csv')
    data = read_data(file_name='data10k10k.csv')
    # print(data)
    can_count, operation_count = data[0]
    print(f'{can_count} {operation_count}')
    can_set = [Can() for i in range(can_count)]
    for i in range(operation_count):
        c_start, c_stop, color = data[i + 1]
        # print(f'opeation: {i + 1}|can: {c_start}->{c_stop}|color={color}')
        for c in range(c_start - 1, c_stop):
            can_set[c].add_color(color)
    out = (i for i in can_set if list(dict.fromkeys(i.color_table)) == [0, 1, 2])
    print(sum(1 for _ in out))


if __name__ == '__main__':
    main()
