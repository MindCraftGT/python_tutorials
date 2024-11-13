#Creating a polymorphism between Plane and cow
class Plane:
    def move(self):
        return "Fly"

class Cow:    
    def move(self):
        return "Walk"
#polymorphism in action
for type_of_movement in [ Plane(), Cow()]:
    print(type_of_movement.move())