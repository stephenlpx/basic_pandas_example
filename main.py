import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()
print(fur_color)

gray_count = 0
red_count = 0
black_count = 0

for color in fur_color:
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1

print(gray_count)
print(red_count)
print(black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
