sample_list = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]


def counterClockwise(input_list):
    temp_list = []
    x = 0
    for i, j in enumerate(input_list):
        for k in range(len(input_list[x])):
            temp_list.append(input_list[k][x])
        x += 1

    main_list = []
    x = 0
    y = len(input_list[0])

    for i in range(len(input_list[0])):
        main_list.append(temp_list[x:y])
        x += len(input_list[0])
        y += len(input_list[0])

    main_list = main_list[::-1]
    return main_list


print(counterClockwise(sample_list))

# Output
# [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
