
# Social Network Graph Assignment

# Create a Person class
class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    # Add a friend to the person's friend list
    def add_friend(self, friend):
        if friend not in self.friends and friend != self:
            self.friends.append(friend)


# Create a SocialNetwork class
class SocialNetwork:
    def __init__(self):
        self.people = {}

    # Add a person to the network
    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
            return

        self.people[name] = Person(name)
        print(f"{name} was added to the network.")

    # Create a bidirectional friendship
    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        if person1 == person2:
            print("Friendship not created. A person cannot be friends with themselves!")
            return

        if person2 in person1.friends:
            print("Friendship already exists.")
            return

        person1.add_friend(person2)
        person2.add_friend(person1)

        print(f"{person1_name} and {person2_name} are now friends.")

    # Print everyone and their friends
    def print_network(self):
        print("\nSOCIAL NETWORK")
        print("-------------------------")

        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]

            if friend_names:
                print(f"{name} is friends with: {', '.join(friend_names)}")
            else:
                print(f"{name} has no friends.")


# TEST THE SOCIAL NETWORK

network = SocialNetwork()

# Add at least 6 people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate person
network.add_person("Alex")

# Create at least 8 friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test a friendship with a person who doesn't exist
network.add_friendship("Alex", "Johnny")

# Test duplicate friendship
network.add_friendship("Alex", "Jordan")

# Print the completed network
network.print_network()
