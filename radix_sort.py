def radix_sort(ul):
    len_ul = len(ul)
    modulus = 10
    div = 1
    while True:
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in ul:
            least_digit = value % modulus
            least_digit = least_digit // div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10
        if len(new_list[0]) == len_ul:
            return new_list[0]
        ul = []
        rd_list_append = ul.append
        for x in new_list:
            for y in x:
                rd_list_append(y)