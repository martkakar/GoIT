from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_keywords(self, keywords):
        pass

    @abstractmethod
    def display_birthday(self, birthday):
        pass

class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        print("Your contacts:")
        for contact in contacts:
            print(contact)

    def display_notes(self, notes):
        print("Your notes:")
        for note in notes:
            print(note)

    def display_keywords(self, keywords):
        print("Available commands:")
        for keyword in keywords:
            print(keyword)

class GUIInterface(UserInterface):
    def display_contacts(self, contacts):
        ...

    def display_notes(self, notes):
        ...

    def display_keywords(self, keywords):
        ...

class WebInterface(UserInterface):
    def display_contacts(self, contacts):
        ...

    def display_notes(self, notes):
        ...

    def display_keywords(self, keywords):
        ...

def create_user_interface(choice):
    if choice == "console":
        return ConsoleInterface
    elif choice == "GUI":
        return GUIInterface
    elif choice == "web":
        return WebInterface
    else:
        raise ValueError("Unknown UI selection")

# example
if __name__ == "__main__":
    user_choice = input("Choice UI (console/GUI/web): ")
    UI = create_user_interface(user_choice)

    contacts = [...]  # contacts list
    notes = [...]  # notes list
    keywords = [...]  # available commands

    UI.display_contacts(contacts)
    UI.display_notes(notes)
    UI.display_keywords(keywords)
