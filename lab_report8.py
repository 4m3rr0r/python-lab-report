def write_sorted_data_to_file(input_data, filename):
    sorted_data = sorted(input_data)
    with open(filename, 'w') as file:
        for item in sorted_data:
            file.write(f"{item}\n")

input_data = [5, 3, 8, 1, 2]
filename = 'sorted_data.txt'
write_sorted_data_to_file(input_data, filename)
