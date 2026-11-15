"""
File Name: entities.py
Authors: Jonathan Walker, Briana Campbell, Isaiah McSwain
Date: 13 Nov 2026

Scope: Create the entities that belong in the dashboard.

"""


class Client:
    """Stores information about a client."""

    def __init__(self, name, email, phone, requirements):
        self.name = name
        self.email = email
        self.phone = phone
        self.requirements = requirements

    def add_requirement(self, requirement):
        """Adds a new requirement for the client."""
        self.requirements.append(requirement)

    def remove_requirement(self, requirement):
        """Removes a requirement from the client."""
        if requirement in self.requirements:
            self.requirements.remove(requirement)

    def display_info(self):
        """Displays the client's information."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("Requirements:")

        for requirement in self.requirements:
            print(f"- {requirement}")

