#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()


def greet(name):
    print(f"Hello, {name}!")
greet("Naasiro")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()


def add(num1, num2):
    return(num1 + num2)
add(5, 9)


def halve(number):
    return(number / 2)
halve(6)