class PersonalAssistant:
    def __init__(self):
        self.contacts = {"Ann": "Marketing Coordinator", "Chelsea": "Software Developer", "Nichole": "Sales Representative"}
        self.todos = []

    def get_contact(self, name):
      if name in self.contacts:
        return self.contacts[name]
      else:
        return "No contact with that name!"

# Code to test output of the class
assistant = PersonalAssistant()
# Change name to one from your contacts
print(assistant.get_contact("Chelsea"))