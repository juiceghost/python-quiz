'''Challenge: Model a Farm'''

class Animal:
    mood = 0
    food = 0

    def __init__(self, name: str, color: str) -> None:
        self.name: str = name
        self.color: str = color


    def feed(self) -> str:
        if self.food < 3:
            self.food += 1
            self.mood += 1
            return f"{self.name} is eating"
        else:
            return f"{self.name} is full already" and self.dump()
    

    def dump(self) -> str:
        if self.food > 2:
            self.mood += 1
            self.food = 0
            return f"Wow! {self.name} took a huge dump!"
        elif self.food == 2:
            return f"Yuck! {self.name} farted!"
        else:
            self.mood -= 1
            return f"Go shit yourself! {self.name} is hungry!"


    def speak(self, sound: str) -> str:
        return f'{self.name} says "{sound}"'
    

    def status(self) -> str:
        if self.mood > 2:
            return f"{self.name} is happy!"
        elif 1 <= self.mood <= 2:
            return f"{self.name} is ok. But don't mess around..."
        else:
            return f"{self.name} is grumpy. Serve some food or keep away!"


class Cow(Animal):

    def speak(self) -> str:
        if self.mood < 2:
            sound = "MOOO! MOOOOOOO!"
        elif 2 <= self.mood < 4:
            sound = "Mooooo"
        else:
            sound = "Moo!"
        return super().speak(sound)


class Farmer(Animal):

    def speak(self) -> str:
        if self.mood < 2:
            sound = r"@!#AAAAARGH!"
        elif 2 <= self.mood < 4:
            sound = "No time to talk. Need to do important stuff."
        else:
            sound = "Helloooo beautiful!"
        return super().speak(sound)


class Duck(Animal):

    def speak(self) -> str:
        if self.mood < 2:
            sound = "Quackin' fuck!"
        elif 2 <= self.mood < 4:
            sound = "Quack! QUACK!"
        else:
            sound = "Quackeliquack!"
        return super().speak(sound)


'''
Create three instances:
A brown cow called Rosa
A dirty farmer who's name is John Deere
A white duck called Donald
'''
cow = Cow("Rosa", "brown")
farmer = Farmer("John Deere", "dirty")
duck = Duck("Donald", "white")


'''
Try out to interact with the three instances.
See how their mood changes with how much the've
eaten and if they've took a dump.
'''
print(f"My cow's name is {cow.name} and she's {cow.color}")
print(f"My name is {farmer.name} and I'm {farmer.color}")
print(f"My duck's name is {duck.name} and he's {duck.color}")

print("\n---------cow--------\n")
print(f"Hi {cow.name}!")
print(cow.speak())
print(cow.status())

print("\n--------farmer------\n")
print(f"Hi {farmer.name}!")
print(farmer.speak())
print(farmer.status())

print("\n---------duck-------\n")
print(f"Hi {duck.name}!")
print(duck.speak())
print(duck.status())

print("\n---------cow--------\n")
print(cow.feed())
print(cow.speak())
print(cow.dump())
print(cow.feed())
print(cow.speak())
print(cow.dump())
print(cow.feed())
print(cow.speak())
print(cow.dump())
print(cow.speak())
print(cow.dump())

print("\n--------farmer------\n")
print(farmer.feed())
print(farmer.speak())
print(farmer.dump())
print(farmer.feed())
print(farmer.speak())
print(farmer.dump())
print(farmer.feed())
print(farmer.speak())
print(farmer.dump())
print(farmer.speak())
print(farmer.dump())

print("\n---------duck-------\n")
print(duck.feed())
print(duck.speak())
print(duck.dump())
print(duck.feed())
print(duck.speak())
print(duck.dump())
print(duck.feed())
print(duck.speak())
print(duck.dump())
print(duck.speak())
print(duck.dump())



'''
def speak_to_leet(trans_str: str) -> str:
    char = "abelost"
    leet = "4831057"
    char_to_leet = trans_str.maketrans(char, leet)
    return trans_str.translate(char_to_leet)


def leet_to_speak(trans_str: str) -> str:
    char = "abelost"
    leet = "4831057"
    leet_to_char = trans_str.maketrans(leet, char)
    return trans_str.translate(leet_to_char)


def translate():
    input_str = input("Enter some text: ")
    print(speak_to_leet(input_str))
    input_str = input("3n73r 50m3 73x7: ")
    print(leet_to_speak(input_str))
'''