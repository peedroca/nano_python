with open("fist_file.txt", "a") as file:
    file.write("Hello World\n")

with open("fist_file.txt", "r") as file:
    for line in file.readlines():
        print(line)
