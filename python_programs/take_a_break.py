import time
import webbrowser

break1 = 1

while (break1 <=3):
  print("This program started on "+time.ctime())
  time.sleep(10)
  webbrowser.open("https://www.youtube.com/watch?v=1tVL11ULjYY")
  break1 = break1 +1

