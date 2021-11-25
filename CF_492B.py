def main():
    max_distance = 0.0

    values = input()
    raw_string_array = input()

    values = values.split()
    values = list(map(int, values))

    raw_list_string_array = raw_string_array.split()
    set_string_array = set(raw_list_string_array)
    list_string_array = list(set_string_array)

    list_num_array = list(map(int, list_string_array))
    list_num_array.sort()

    for index in range(1, len(list_num_array)):
        if (list_num_array[index] - list_num_array[index-1] > max_distance):
            max_distance = list_num_array[index] - list_num_array[index-1]

    first_distance = list_num_array[0] - 0.0
    last_distance = values[1] - list_num_array[-1]

    max_range = float(max(first_distance, last_distance, max_distance/2))

    print(max_range)

if __name__ == "__main__":
    main()
