import random

can_count_max = 100000
operation_count_max = 100000
can_count = random.randint(1, can_count_max)
operation_count = random.randint(1, operation_count_max)

out = f'{can_count} {operation_count}'
print(out)

for i in range(0, operation_count):
    c_start = random.randint(1, can_count)
    c_stop = random.randint(c_start, can_count)
    color = random.randint(1,3)
    out += f'\n{c_start} {c_stop} {color}'

#print(out)
with open('data100k100k.csv', 'w') as file:
    file.write(out)
