data_structure = [
    [1, 2, 3],
    {
        'a': 4,
        'b': 5
    },
    (
        6,
        {
            'cube': 7,
            'drum': 8
        }
    ),
    "Hello",
        (
            (),
            [
                {
                    (
                        2,
                        'Urban',
                        ('Urban2', 35)
                    )
                }
            ]
        )
]


def my_func(my_func_arg):
    init_summ = 0

    if isinstance(my_func_arg, int):
        init_summ += my_func_arg
    elif isinstance(my_func_arg, str):
        init_summ += len(my_func_arg)
    elif isinstance(my_func_arg, tuple) or isinstance(my_func_arg, list) or isinstance(my_func_arg, set):
        for elem in my_func_arg:
            init_summ += my_func(elem)
    elif isinstance(my_func_arg, dict):
        for key, elem in my_func_arg.items():
            init_summ += len(key)
            init_summ += my_func(elem)

    return init_summ

res = my_func(data_structure)
print(res)