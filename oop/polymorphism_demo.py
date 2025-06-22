#Task 2. Exploring Polymorphism and Method Overriding
'''
You are tasked with creating a Python script named polymorphism_demo.py. 
In this script, define a base class Shape with a method area() and derived classes 
Rectangle and Circle, each overriding the area() method to calculate their respective areas.
'''
import math

#Create base class called Shape
class Shape:
    def area(self):
        return f"NotImplementedError"

#Creating derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

#Creating derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2