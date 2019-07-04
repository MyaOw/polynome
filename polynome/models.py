from django.db import models

class Model:
    def __init__(self, a=0.0,b=0.0,c=0.0,x=0.0):
        self.a = a
        self.b = b
        self.c = c
        self.x = x

    def solve(self, a,b,c,x):
        return a*x**2+(b*x)+c
