def merge_sort(a_list):
    print("Splitting ", a_list)
    # Already ordered
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Remember every recursion call has their variables scope!
        i = 0 # index for left
        j = 0 # index for right
        k = 0 # index for join

        # Ordering
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        # Union left
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        # Union right
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = i + 1
            k = k + 1

    print("mergin ", a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)

