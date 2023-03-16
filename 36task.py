def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        list = []
        for j in range(1, num_columns + 1):
            list.append(str(operation(i, j)))
        print(''.join(f'{x:<3}' for x in list))
print_operation_table(lambda x, y: x * y)