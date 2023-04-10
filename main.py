# Working with dataset
dataset = []
with open("iris.data", "r") as file:
    for record in file.readlines():
        dataset.append(record.split(","))

print(dataset[0])
print(dataset[1][0])
