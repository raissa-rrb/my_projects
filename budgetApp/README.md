# Budget App
> This projects aims at challenging my Python, SQL and Qt skills

## The Objective
What I want is a budget application that allows me to:
- **track expenses** : each expense will possess a tag that indicates its category (shopping, bills, groceries...)
- **Budget goal** : it will be possible to create a budget goal for each category OR for each month
    - Like the user can either say "i shouldn't spend more than 200 euros on groceries each month "    
    - or "i shouldn't use more than 800 euros this month"
    - can do both : "i shouldn't use more than 800 euro this month, including 200 euro max for groceries"
- **Savings tracker** : the user can set saving goals for each month (could be the same every month or not) and the app should display (a graph would be cool) how much the user actually saved and display whether the goal has been reached (you saved 50% of your goal) 

I think that's enough for now :)

## OOP in Python
> I've done OOP in Java and C++ so I have a solid understanding of OOP mechanisms but let's have a quick review of Python for OOP

[this](https://www.youtube.com/watch?v=rLyYb7BFgQI) short video gives us a good base on how to create a class, methods and howw to call them.

```python
# self <=> this in C, it's the reference to the current instance of this class
class ClassName:

    attributeName = value # shared among all the instances of this class

    # constructor
    def __init__(self, paramName1: type, paramName2: type) -> None:
        self.paramName1 = paramName1
        self.paramName2 = paramName2

    # methods
    def methodName(self) -> returnvalue:
        if self.param1: ...
        else: ...

    # dunder methods : define operations +, *, - ...
    # example : object1 + object2
    def __add__(self, other):
        ...

    def __str__(self) -> str:
        return f'param1 : {self.paramName1} param2: {self.param2}' 
    
        
# to instanciate an object
object0 = ClassName(param1, param2)

# to use a method
object0.methodName()
print(object0) # calls __str__ otherwise returns the memory adress of the class
```
Now we need a few more things in our Python OOP toolbox like inheritance and abstract classes. The best way to learn that, in my opinion, is to implement Animals, we need an `Animal` abstract class and then actuals animals that inherit from it. 
In order to cover that let's use Geeks For Geeks [Python OOPs concepts](https://www.geeksforgeeks.org/python/python-oops-concepts/) article as I find them pretty comprehensive and simple to understand.

### Class variable vs Instance variable 
- **Class variable** : shared accross all instances of a class, in the code above that's `attributeName`
    - Can be accessed with `ClassName.variableName`, a modification will affect all the other instances
- **Instance variable** : unique to each instance of a class, it's the ones defined in the `__init__` method
    - Can be accessed with `objectName.variableName`, only objectName will be modified

### Inheritance
> Inheritance is when a class acquires properties and methods from another class : a child class inherits from a parent class
> Several types of inheritance
>    - **Single inheritance** : a child inherits from a single parent
>    - **Multiple Inheritance**: a child inherits from more than one parent class
>    - **Multilevel inheritance**: a child inherits from a parent which inherits from a parent class aswell
>    - **Hierarchical inheritance**: multiple child classes inherit from a single parent class
>    - **Hybrid inheritance**: a combination of two or more types

The syntax is the following
````python
# single inheritance 1 child 1 parent
class Child(Parent):
    ...
# multilevel 1 child inheriting from a Child 
class SecondChild(Child):
    ...
# multiple inheritance
class ThirdChild(SecondChild, OtherParent):
    ...
````

Python also supports **polymorphism**: runtime (overiding methods in children for instance) and compile time (example several add functions with different parameters)

### Encapsulation
> - **Public members** : accessible from anywhere
> - **Protected members** : accessible within the class and its subclasses
> - **Private members** : accessible *only* within the class
>   In the code the type of encapsulation is defined with undercaps
```python
class Name:
    def __init__(self, param0, param1, param2):
        self.param0 = param0 # no undecap => param0 is public
        self._param1 = param1 # one undercap => param1 is protected
        self.__param2 = param2 # two undercaps => param2 is private
``` 
### Abstraction
> And finally one very important mechanism: focus on the **what to do** rather than the **how to ?**
> - **Partial abstraction** : abstract class contains both abstract and concrete methods
> - **Full abstraction** : abstract class contains **only** abstract methods (=> interfaces)

```python
from abs import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self, name):
        self.name = name

    # concrete method
    def method0(self):
          ...

    # abstract method
    @abstractmethod
    def method1(self):
        pass

class child(AbstractClass):
    def method1(self):
        #instructions
```

### Animals
> Now we have eveyrhting we need to implement some animals.
> So an Animal is not a concrete object, a cat is. An animal is just a concept, it answers the "what is it"
> for instance, all animals have a name, they can all eat, sleep, walk and produce a sound
> however they may not do it the same way, a cat meows  and a dog barks for example, but they sleep the same way.
> So instead of making 2 classes for cat and dog with the exact same code except for the sound method we can have an abstract animal class that defines the common methods and then have a concrete class for our animals in which we'll describe the specific methods like sound in our example


```python
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name # name is public
    
    # animals can make a sound, but they dont't all make the same so it's abstract
    @abstractmethod
    def sound(self):
        pass

    # animals eat 
    def eat(self):
        print("yum i was hungry")
    
    # animals sleep
    def sleep(self):
        print("zzzz i was tired zzzz")


#children
class Cow(Animal):
    def sound(self):
        print("meuuuuh")

    def __str__(self):
        return f"hi i'm a cow my name is {self.name}"
    
class Dog(Animal):
    def sound(self):
        print("wouf wouf")

    def __str__(self):
        return f"hi i'm a dog my name is {self.name}"

class Cat(Animal):
    def sound(self):
        print("meow meow")

    def __str__(self):
        return f"hi i'm a cat my name is {self.name}"

#instanciate animals
cow0 = Cow("Dolores")
dog0 = Dog("Pluto")
cat0 = Cat("kitty")

animals = [cow0, dog0, cat0]

for i in animals:
    print(i)
    i.eat()
    i.sound() 
    print("\n")
```
This enables us to have a table containing all our animals because they're all of a parent type `animal`, we wouldn't be able to do that with only cat and dog classes.
But in the for loop, when the method is called the system first checks in the concrete class if it's defined.
Se we have:
```terminal
hi i'm a cow my name is Dolores
yum i was hungry
meuuuuh

hi i'm a dog my name is Pluto
yum i was hungry
wouf wouf

hi i'm a cat my name is kitty
yum i was hungry
meow meow
```

## Now the actual budget App
> I'm using a [youtube tutorial](https://www.youtube.com/watch?v=I8S9V8AYjtA) **only** to get some general directions, i'm not going to copy paste it.

### App design: pyQt
- QWidget : windows seen by the user
- QLabel : text on the screen
- QPishButton : buttons
- QLineEdit : input box
- QComboBox: dorpdown selection
- QTableWidget: speadsheet
- QVBoxLayout : colunms
- QHBoxLayout : rowns
- QMessageBox : popups
- QTableWidgetItem 
- QHeadrView : style the table

QTCOre 
- QDate 
- Qt : alignments 

