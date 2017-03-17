import turtle

def draw_square(some_turtle):
  for i in range(1,5):
    some_turtle.right(90)
    some_turtle.forward(100)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("white")

  # draw square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("purple")
  brad.speed(2)
  for i in range(1,37):
    draw_square(brad)
    brad.right(10)


  # draw circle
  # angie = turtle.Turtle()
  # angie.shape("arrow")
  # angie.color("blue")
  # angie.circle(100)

  window.exitonclick()

draw_art()