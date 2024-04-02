class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    return f"Hello I am {self.name}. I am a {self.age}yr old {self.gender}"

person1 = Person("Erick Mwangi", 20, "Male")
person1.introduce()
