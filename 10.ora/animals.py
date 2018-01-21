#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal:

    health = None
    cutenessFactor = None
    name = None

    def __init__(self, name, health, CF):
        self.name = name
        self.health = health
        self.cutenessFactor = CF
    
    def speak(self):
        print("...")

    def info(self):
        print("My name is:", self.name, ",my health is:", self.health, ",CF:",self.cutenessFactor)

class Dog(Animal):

    def __init__(self, name, health, CF):
        super().__init__(name, health, CF)
    
    def speak(self):
        print("Vau Vau!")

class Cat(Animal):
    
    def __init(self, name, health, CF):
        super().__init__(name, health, CF)

    def speak(self):
        print("Miau Miau!")


def main():
    anAnimal = Animal("Noname",10 , 0)

    myDog = Dog("Bobby", 10, 10)
    myCat = Cat("Grumpy", 10, 1)

    anAnimal.speak()
    anAnimal.info()

    myDog.speak()
    myDog.info()

    myCat.speak()
    myCat.info()

if __name__ == '__main__':
    main()
