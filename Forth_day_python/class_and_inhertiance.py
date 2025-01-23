class Human:
    def __init__(self, age, name, legs):
        self.name = name
        self.age = age
        self.legs = legs

    def walk(self, distance):
        print(f"I walked {distance}m")
    
class Student(Human):
    def __init__(self, topics, interrests, age, name, legs):
        self.topics = topics
        self.interrests = interrests
        super().__init__(age, name, legs)

    def walk(self, distance):
        return super().walk(distance)

x = Student(["c#", "python", "Ansible"], ["Web-Developement", "Dev-Ops"], 46, "Mathias", True,)

x.walk(23)
print(x.interrests)
print(x.age)
