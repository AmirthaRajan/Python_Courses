class Food:
    
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind
    
    def get_name(self):
        return self.name

    def get_kind(self):
        return self.kind

    @classmethod
    def describe(cls):
        print("this is describe method")

    def __repr__(self):
        print("This food {} is of kind {}".format(self.name , self.kind))



class Meat(Food):

    def __init__(self):
        self.food = Food("noodles","chinese")

    def cook(self):
        print("cooking ... {} which is {}".format(self.food.get_name(),self.food.get_kind()))


class Fruit(Food):
    def __init__(self):
        self.food = Food("salad","italian")

    def clean(self):
        print("cleaning fruits")