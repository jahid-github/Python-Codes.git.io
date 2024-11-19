# -*- coding: utf-8 -*-
"""Functions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1__DkURVXw4l6bsNXY1Ia6qOtXO2YPxVO
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

def triangle(char, height):
    for a in range(height):
        print(char * (a+1))
triangle('L', 5)

def rectangle(char, width, height):
  for _ in range(height):
    print(char*width)
rectangle('H', 5, 4)

import turtle as t
def square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
square(200)

import turtle as t
def rectangle(width, height):
  for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
rectangle(100, 50)
t.done()

def calculate_average(scores):
    if not scores:  # Check if the list is empty
        return "The scores list is empty. Cannot calculate average."
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

student_scores = []
print(calculate_average(student_scores))

def process(x, y=10):
    return x + y
print(process(5))
print(process(5, 20))