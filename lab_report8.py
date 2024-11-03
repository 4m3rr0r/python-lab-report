def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

filename = 'lottery_data.txt'
data = 'Lottery Numbers:\n123456\n654321\n112233\n223344\n334455'

write_to_file(filename, data)
lottery_data = read_from_file(filename)

print(f"Data written to {filename}:\n{lottery_data}")
