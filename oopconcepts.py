"""Learning to Program PT2 OOP Concepts."""


class Classroom:
    """Class room class."""

    def __init__(self):
        """Initialization."""
        self._people = []

    def add_person(self, person):
        """Add a person."""
        self._people.append(person)

    def remove_person(self, person):
        """Remove a person."""
        self._people.remove(person)

    def greet(self):
        """All people say hello."""
        for person in self._people:
            person.say_hello()


class Person:
    """Person Class."""

    def __init__(self, name):
        """Initialization."""
        self.name = name

    def say_hello(self):
        """A person says hello."""
        print(id(self))
        print("Hello, ", self.name)


room = Classroom()
room.add_person(Person("Scott"))
room.add_person(Person("Poonam"))
room.add_person(Person("Paul"))
room.greet()
