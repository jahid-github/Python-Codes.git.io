# -*- coding: utf-8 -*-
"""Part add and Sample output will be
First line and Second part
First line and Second part
"""
def print_twice(text):
    print(text)
    print(text)

def cat_twice(part1, part2):
    cat=part1+part2
    print_twice(cat)

line1='First line'
line2=' and Second part'
cat_twice(line1, line2)

"""Triangle
Write a function called triangle that takes a string and an integer and draws a triangle with the given height, made up of copies of the string. Here’s an example of a triangle with five levels using the string 'L':
triangle('L', 5)
L
LL
LLL
LLLL
LLLLL
"""
def triangle(char, height):
    for a in range(height):
        print(char * (a+1))
triangle('L', 5)

"""Rectangle
Write a function called rectangle that takes a string and two integers and draws a rectangle with the given width and height, made up of copies of the string. Here’s an example of a rectangle with width 5 and height 4, using the string 'H':

rectangle('H', 5, 4)
HHHHH
HHHHH
HHHHH
HHHHH
"""
def rectangle(char, width, height):
  for _ in range(height):
    print(char*width)
rectangle('H', 5, 4)

"""Square with turtle
Using the module turtle, write a function called square that draws a square with given side length.
If you are using VSCode, the screen opens and closes. Then for closing the screen only after clicking:
import turtle as t
#def your function:
#   your code
square(150)
t.done() # in VSCode, waits for click in close window 
"""
import turtle as t
def square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
square(200)

"""Rectangle with turtle
Write a function called rectangle that draws a rectangle with given side lengths.
import turtle as t
"""
def rectangle(width, height):
  for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
rectangle(100, 50)
t.done()

"""
Calculate average
"""
def calculate_average(scores):
    if not scores:  # Check if the list is empty
        return "The scores list is empty. Cannot calculate average."
    total = 0
    for score in scores:
        total += score
    return total / len(scores)
student_scores = []
print(calculate_average(student_scores))

"""
Process
"""
def process(x, y=10):
    return x + y
print(process(5))
print(process(5, 20))

"""
Polygon
"""
def polygon(n, length):
   angle = 360 / n
   for i in range(n):
       forward(length)
       left(angle)

"""
"""
