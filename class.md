## *Classes*


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





