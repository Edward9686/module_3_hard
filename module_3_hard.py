def calculate_structure_sum(*args):
    result = 0
    if isinstance(args[0], int | float):
        result += args[0]
    elif isinstance(args[0], str):
        result += len(args[0])
    elif isinstance(args[0], list | set | tuple):
        for i in args[0]:
            result += calculate_structure_sum(i)
    elif isinstance(args[0], dict):
        for key, value in args[0].items():
            result += calculate_structure_sum(key)
            result += calculate_structure_sum(value)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
