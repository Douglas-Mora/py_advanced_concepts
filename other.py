class Mobile:
    def __init__(self, number):
        self.number = number
    
    def turn_on(self):
        return f"mobile phone {self.number} is turned on"
    
    def turned_off(self):
        return f"mobile phone is turned off"
    
    def call(self,number_to_call):
        return f"calling {number_to_call}"
    

mymobile = Mobile("8x1x 75x8")
hermobile = Mobile("1234 8765")
print(mymobile.turn_on())
print(hermobile.turn_on())
print(mymobile.call(hermobile.number))
print(mymobile.turned_off())
print(hermobile.turned_off())
print("Code ended!")
