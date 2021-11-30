class Animal:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def description(self):
		if self.age == 1:
			return f"{self.name} is {self.age} year old."
		else:
			return f"{self.name} is {self.age} years old."

	def noise(self, noise):
		return f"{self.name} says {noise}"


class Pig(Animal):
	def mud_rolling(self):
		return f"{self.name} loves to roll around in the mud!"

	def noise(self, noise="Oink"):
		return f"{self.name} says {noise}."


class Sheep(Animal):
	def jump(self):
		return f"{self.name} loves to jump around!"

	def noise(self, noise="Reeeeeeeeeek"):
		return f"{self.name} says {noise}."


class Rooster(Animal):
	def cookely(self):
		return f"{self.name} wakes everybody in the morning at 7 A.M"

	def noise(self, noise="Cookely kuuu"):
		return f"{self.name} says {noise}"


frank = Sheep("Frank", 2)
print(frank.jump())