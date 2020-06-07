def gap_insertion_sort(a_list, start, gap):
    print("start = ", start)
    print("gap = ", gap)
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


def shell_sort(a_list):
    # Divide the list by half
    sublist_count = len(a_list) // 2
    print("Sublist count:", sublist_count)
    while sublist_count > 0:
        for start_position in range(sublist_count):
            print("Start Position: ", start_position)
            gap_insertion_sort(a_list, start_position, sublist_count)

        print("After increments of size", sublist_count, "The list is",
              a_list)

        sublist_count = sublist_count // 2


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)