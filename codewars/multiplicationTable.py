def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

print(multi_table(5))
print()
print(multi_table(1))