## *Classes*
>>> *Back to [README](/README.md)*


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

The term **instance** is very often used interchangeably with the the term **object**, becuase **object** refers to a particular isntance of a **class**. It's a bit of a simplification, because the term **object** is more general than instance.

To create instances, we have to **instantiate a class**...:

```
duckling = Duck(height=10, weight=4, sex="male")
drake = Duck(height=25, weight=3, sex="male")
hen = Duck(height=20, weight=3.2, sex="female")
```

An **attribute** is a capacious term that can refer to two major kinds of class traits:

 - *variables*, containing information about the class itself or a class instance; classes and class instances can own many variables;
- *methods*, formulated as Python functions; they represent a behavior that could be applied to the object.

Each Python object has its own individual set of attributes. We can extend that set by adding new attributes to existing objects, change (reasign) them or control access to those attributes.

It is said that methods are the 'callable attributes' of Python objects. By 'callable' we should understand anything that can be called; such objects allow you to use round parentheses () and eventually pass some parameters, just like functions.

This is very important to remember... **methods are called on behalf of an object and are usually executed on object data.**

>>> Go [up](#classes)

Class attributes are most often addressed with 'dot' notation, i.e., \<class\>dot\<attribute\>. The other way to access attributes (variables) is to use `getattr` and `setattr` functions.

In our example, there are the following attributes:
 - **variables**: `self.height`, `self.weight`, `self.sex` --containing different values for each object.
 - **methods**: `__init__`, `walk`, `quack` --common to all objects so far.

 Examples:
  - To call a method, issue: `drake.quack()`;
  - To access and attribute, issue: `print(duckling.height)`.

  If you run the code, you'll get the following example:
  ```
  Quack!
  10
  ```

A **type** is one of the most fundamental and abstract terms of Python:
   - is the foremost type that any class can be inherited from;
   - as a result, if you're looking for the type of class, then *type* is returned;
   - in all other cases, it refers to the class that was used to instantiate the object; it's a general term describing the type/kind of any object;
   - it's the name of a very handy Python function that returns the class information about the objects passed as arguments to that function;
   - it returns a new type object when `type()` is called with three arguments.