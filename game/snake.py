import tkinter as tk
import turtle
import time
import random

def start_game_window():
    # Close main menu window
    root.destroy()

    # Game logic
    delay = 0.05

    # Score
    score = 0
    high_score = 0

    # Set up the screen
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

# Set the geometry of the main menu window to match the game window and center it
game_width = 600
game_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - game_width) // 2
y_coordinate = (screen_height - game_height) // 2
root.geometry(f"{game_width}x{game_height}+{x_coordinate}+{y_coordinate}")

# Change background color
root.configure(bg="#fff5e3")  

# Instructions label
instructions_label = tk.Label(root, text="Заавар\n\n\n 1.Могойг зөвхөн сум ашиглан удирдана.\n\n2.Санамсаргүй гарч ирэх хоолыг идсэнээр могой урт болно.\n\n3.Ханыг мөргөх үед тоглоом дуусна\n\n4.Өөрийнхөө биед хүрвэл тоглоом дуусна!", font=("Helvetica", 14), wraplength=game_width-40, bg="#f0f0f0")  # Match background color
instructions_label.pack(pady=20)

# Function to start the game
def start_game():
    start_game_window()

# Button to start the game
start_button = tk.Button(root, text="Play Game", font=("Helvetica", 16), command=start_game, bg="#4CAF50", fg="white")  # Green button with white text
start_button.pack(pady=10)

# Function to exit the game
def exit_game():
    root.destroy()

# Button to exit the game
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 16), command=exit_game, bg="#f44336", fg="white")  # Red button with white text
exit_button.pack(pady=10)

root.mainloop()



