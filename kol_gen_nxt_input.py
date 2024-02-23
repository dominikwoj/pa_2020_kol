import csv

def main():
    can_count, operation_count = list(map(int, input().split()))
    can_set = [[0] for i in range(can_count)]
    for i in range(operation_count):
        c_start, c_stop, color = list(map(int, input().split()))
        [can_set[c].append(color) for c in range(c_start - 1, c_stop)]

    out = (i for i in can_set if list(dict.fromkeys(i)) == [0, 1, 2])
    print(sum(1 for _ in out))


if __name__ == '__main__':
    main()
