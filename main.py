class Alien:
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object):
        pass

def new_aliens_collection(start_positions):
    return [Alien(x, y) for x, y in start_positions]


# create an alien
alien1 = Alien(5, 10)
print(alien1.x_coordinate, alien1.y_coordinate)
print(alien1.health)

# hit the alien
alien1.hit()
alien1.hit()
alien1.hit()
print(alien1.health)

# Check if the alien is dead or alive
if alien1.is_alive():
    print("Is Alive")
else:
    print("Dead.")

# Create another alien and check the total count
alien1 = Alien(2, 1)
print(Alien.total_aliens_created)


