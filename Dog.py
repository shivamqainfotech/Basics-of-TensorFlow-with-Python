class Dog:
    """    
    Requires:
    legs - Legs so that the dog can walk.
    color - A color of the fur.
    """

    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
        
    def bark(self):
        bark = "bark " * 2
        return bark

#if __name__ == "__main__":
dog = Dog(4, "brown")
bark = dog.bark()
print(bark)