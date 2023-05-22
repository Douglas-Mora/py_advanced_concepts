# *Why I did this?*
To collect notes taken while studying Python's advanced concepts.

**Topics**
 - Classes, instances, attributes, methods, as well as working with class and instance data
 - Shallow and deep operations
 - abstract classes, method overriding, static and class methods, special methods
 - inheritance, polymorphism, subclasses, and encapsulation
 - advanced exception handling techniques
 - metaclasses
------------------------------------------------------------- 
 
## **OOP** (*Object-Oriented Programming*)

OOP is s an evolution of good design practices that go back to the very beginning of computer programming.

It allows programmers to model...
 - Entities representing real-life objects.
 - Objects in order to solve real-life problems in an efficient, comfortable, extendable, and well-structured manner.

## **Definitions**
 - *class* -- An idea, blueprint, or recipe for an instance.
 - *instance* -- An instantiation of the class; very often used interchangeably with the term ‘object’.
 - *object* -- Python's representation of data and methods; objects could be aggregates of instances.
 - *attribute* -- Any object or class trait; could be a variable or method.
 - *method* -- A function built into a class that is executed on behalf of the class or object; some say that it's a ‘callable attribute’,
 - *type* -- refers to the class that was used to instantiate the object.
 

Why is everything in Python organized as objects?
Because an object is a very useful culmination of all these terms:
 - It is an independent instance of class, and it contains and aggregates some specific and valuable data in attributes relevant to individual objects.
 - It owns and shares methods used to perform actions.

-------------------------------------------------------------
*Topics to be covered next...*

 - Creation and use of decorators
 - Implementation of core syntax
 - Class and static methods
 - Abstract methods
 - Comparison of inheritance and composition
 - Attribute encapsulation
 - Exception chaining
 - Object persistence
 - Metaprograming

## *Classes*
Click [here](/class.md#classes)


A *class* expresses an idea; it's a blueprint or recipe for an instance. *Classes* describe attributes and functionalities together to represent and idea as accurately as possible.

A *class* can be built from scratch, or even more interesting and useful, employ *inheritance* to get a more specialized class based on another class.
Also, my classes could be used as superclasses for newly derived classes (subclasses).

```
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack!')
````
An **instance** is one particular physical instantiation of a *class* that occupies memory and has data elements. This is what 'self' refers to when we deal with class instances.

An **object** is everything in Python that you can operate on, like a class, instance, list, or dictionary.





