def shell_sort(a_list):
    # Divide the list by half
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            print("Start Position: ", start_position)
            print("range", start_position + sublist_count)
            increment_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        print("==================================")
        sublist_count = sublist_count // 2


def increment_insertion_sort(a_list, start, increment):
    for i in range(start + increment, len(a_list), increment):
        current_value = a_list[i]
        position = i
        while position >= increment and a_list[position - increment] > current_value:
            print("a_list[",position,"-",increment,"]", ">", current_value)
            print("changing position", position, ">=", increment)
            a_list[position] = a_list[position - increment]
            position = position - increment
            a_list[position] = current_value



a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)