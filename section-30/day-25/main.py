# import csv
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

answer_state = screen.textinput(title="Guess the State.", prompt="What's another state's name?").title()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while score < 49:
    if answer_state in all_states:
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
            
    answer_state = screen.textinput(title=f"{score} /50 States Correct", prompt="What's another state's name?").title()



screen.exitonclick()










# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(float(row[1]))

#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# total = 0

# for i in temp_list:
#     total += i

# average = total / len(temp_list)

# print(average)

# print(sum(temp_list) / len(temp_list))

# print(data["temp"].mean())

# max_temp = data.temp.max()

# print(temp_list)

# print(data.condition)

# print(data[data.day == "Monday"])

# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]

# faren = monday.temp * 1.8 + 32

# print(faren)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241127.csv")
# red = 0
# gray = 0
# black = 0
# for i in data["Primary Fur Color"]:
#     if i == "Cinnamon":
#         red += 1
#     elif i == "Gray":
#         gray += 1
#     elif i == "Black":
#         black += 1

# data_dict = {
#     "Fur Color": ["Gray", "Red", "Black"],
#     "Count": [gray, red, black]
# }
# data_set = pandas.DataFrame(data_dict)
# data_set.to_csv("squirrel_count.csv")