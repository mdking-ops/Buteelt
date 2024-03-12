import turtle
import time
import random

delay = 0.05

#Оноо
score = 0
high_score = 0

# Дэлгэцээ тохируулах
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # дэлгэц шинэчлэх

#Могойн толгой
head = turtle.Turtle() #
head.speed(10)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
#Могойн хоол
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()  #turtle курсороо нуух
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#Үйлдлүүд
def go_up():
        head.direction = "up"


def go_down():
        head.direction = "down"


def go_left():
         head.direction = "left"


def go_right():
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

#Keyboard ажиллагаа
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Үндсэн тоглоомын давталт
while True:
    wn.update()
    # Хүрээнд хүрсэн эсэхийг шалгах
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Оноогоо шинэчлэх
        score = 0

        # хурдаа шинэчлэх
        delay = 0.05

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("italic", 24, "normal"))

    # Хоолонд хүрсэн эсэхээ шалгах
    if head.distance(food) < 20:
        #Дурын байрлал руу шил
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Mогойг
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("brown")
        new_segment.penup()
        segments.append(new_segment)

        #Хурдсах
        delay -= 0.001

        #Оноогоо нэмэх
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Бусад давхцалыг шалгах
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Оноогоо шинэчлэх
            score = 0

            # Хурдаа шинэчлэх
            delay = 0.05

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)