import csv
from memory_profiler import profile


#@profile()
def read_data(file_name):
    rows = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append([int(i) for i in str(row[0]).split(' ')])
    return rows


#@profile()
def main():
    data = read_data(file_name='data10k10k.csv')
    #print(data)
    can_count, operation_count = data[0]
    #print(f'{can_count} {operation_count}')
    can_set = [[0] for i in range(can_count)]
    for i in range(operation_count):
        c_start, c_stop, color = data[i + 1]
        [can_set[c].append(color) for c in range(c_start - 1, c_stop)]

    out = (i for i in can_set if list(dict.fromkeys(i)) == [0, 1, 2])
    print(sum(1 for _ in out))


if __name__ == '__main__':
    main()
