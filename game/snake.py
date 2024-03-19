import tkinter as tk
from tkinter import PhotoImage
import turtle
import time
import random

def start_game_window():
    # Main menu хаах хэсэг
    root.destroy()


    delay = 0.05

    # Оноо
    score = 0
    high_score = 0

    # Дэлгэц тохируулах хэсэг 
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("#fff5e3")
    wn.setup(width=600, height=700)
    wn.tracer(0)  # Turn off screen updates

    border = turtle.Turtle()
    border.penup()
    border.goto(-300, -300)
    border.pendown()

    score_display = turtle.Turtle()
    score_display.penup()
    score_display.goto(0, 310)
    score_display.hideturtle()

    for _ in range(4):
        border.forward(600)
        border.left(90)

    border.hideturtle()

    head = turtle.Turtle()
    head.speed(10)
    head.shape("square")
    head.color("#aef0d1")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("#e84c3e")
    food.penup()
    food.goto(0, 100)

    segments = []

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)

    score_display.write("Оноо: 0  Хамгийн өндөр оноо: 0", align="center", font=("Courier", 24, "normal"))

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":   
            head.direction = "down"

    def go_left():
        if head.direction != "right":  
            head.direction = "left"

    def go_right():
        if head.direction != "left": 
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

    while True:
        wn.update()
        if (
            head.xcor() > 290
            or head.xcor() < -290
            or head.ycor() > 290
            or head.ycor() < -290
        ):
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.05

            score_display.clear()
            score_display.write("Оноо: {}  Хамгийн өндөр оноо: {}".format(score, high_score), align="center", font=("Helvetica", 24, "normal"))

        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#23b99a")
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001
            score += 10

            if score > high_score:
                high_score = score

            score_display.clear()
            score_display.write("Оноо: {}  Хамгийн өндөр оноо: {}".format(score, high_score), align="center", font=("Helvetica", 24, "normal"))

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "Stop"

                for segment in segments:
                    segment.goto(1000, 1000)

                segments.clear()

                score = 0
                delay = 0.05

                score_display.clear()
                score_display.write("Оноо: {}  Хамгийн өндөр оноо: {}".format(score, high_score), align="center", font=("Helvetica", 24, "normal"))

       
        time.sleep(delay)

def start_game():
    start_game_window()

root = tk.Tk()
root.title("Game Menu")

# Main menu хэсгийн window тохируулга урт , өргөн , дэлгэцний хаана гарч ирэх  
game_width = 600
game_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - game_width) // 2
y_coordinate = (screen_height - game_height) // 2
root.geometry(f"{game_width}x{game_height}+{x_coordinate}+{y_coordinate}")

# Арын өнгө тохируулга
root.configure(bg="#fff5e3")  


# Load the snake image using PhotoImage
try:
    image = PhotoImage(file="snake.png")  # Replace "snake.png" with your image path
except FileNotFoundError:
    print("Error: Image file 'snake.png' not found. Please check the path.")
    exit()

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label.pack(pady=20)

#  Зааврын Label
instructions_label = tk.Label(root, text="Заавар\n\n\n 1.Могойг зөвхөн сум ашиглан удирдана.\n\n2.Санамсаргүй гарч ирэх хоолыг идсэнээр могой урт болно.\n\n3.Ханыг мөргөх үед тоглоом дуусна\n\n4.Өөрийнхөө биед хүрвэл тоглоом дуусна!", font=("Helvetica", 14), wraplength=game_width-40, bg="#E5DCCC") 
instructions_label.pack(pady=20)

# Тоглоом эхлүүлэх функц
def start_game():
    start_game_window()

# Тоглоом эхлүүлэх товч
start_button = tk.Button(root, text="Тоглох", font=("Helvetica", 16), command=start_game, bg="#E5DCCC", fg="black")  
start_button.pack(pady=10)

# Тоглоомноос гарах функц
def exit_game():
    root.destroy()

# Тоглоомноос гарах товч
exit_button = tk.Button(root, text="Гарах", font=("Helvetica", 16), command=exit_game, bg="#E5DCCC", fg="black")
exit_button.pack(pady=10)

root.mainloop()



