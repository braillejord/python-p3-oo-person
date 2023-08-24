class Person:
    def __init__(self, name):
        self._name = name
        self.bank_account = 25
        self.happiness = 8
        self.hygiene = 8

    def get_name(self):
        return self._name

    name = property(fget=get_name)

    def is_clean(self):
        if self.hygiene == 6.9:
            print("Dirty boy!")

        return self.hygiene > 7

    def is_happy(self):
        return self.happiness > 7

    def get_paid(self, amount):
        self.bank_account += amount
        return "all about the benjamins BABY"

    def take_bath(self):
        self.hygiene += 4
        return "♪ Rub-a-dub just relaxing in the tub ♫"

    def work_out(self):
        self.happiness += 2
        self.hygiene -= 3
        return "♪ another one bites the dust ♫"

    def call_friend(self, friend):
        self.happiness += 3
        friend.happiness += 3
        return f"Hi {friend.name}! It's {self.name}. I'm so cool. You are too. Do you watch The Office? Sometimes you make good Jim faces."

    def start_conversation(self, friend, topic):
        if topic == "politics":
            self.happiness -= 2
            friend.happiness -= 2
            return "blah blah partisan blah lobbyist"
        elif topic == "weather":
            self.happiness += 1
            friend.happiness += 1
            return "blah blah sun blah rain"
        else:
            return "blah blah blah blah blah"


curtis = Person("Curtis")
john = Person("John")
print(curtis.call_friend(john))
print(curtis.start_conversation(john, "mac and cheese"))
