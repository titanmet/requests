def write_to_file(filename: str, data: list):
    with open(filename, "w") as file:
        file.writelines(data)


def read_file_data(filename):
    with open(filename, "r") as file:
        data = file.read()
        return data


# write_to_file("test.txt", ["Hi\n", "This is a test\n",
#               "The second test\n", "And one more test\n"])
# print(read_file_data("test.txt"))