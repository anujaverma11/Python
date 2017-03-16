import turtle

def draw_square():
  window = turtle.Screen()
  window.bgcolor("white")

  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("purple")
  brad.speed(2)

  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)
  brad.forward(100)
  brad.right(90)



  window.exitonclick()

draw_square()