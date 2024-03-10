def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."
    return inner
 

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def find_contact(name, contacts):
    return contacts[name]


@input_error
def show_all_contacts(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def handle_command(command, contacts):
    command = command.strip().split(' ')
    if command[0] == "add":
        if len(command) != 3:
            return "Invalid command format."
        return add_contact((command[1], command[2]), contacts)
    elif command[0] == "phone":
        if len(command) != 2:
            return "Invalid command format."
        return find_contact(command[1], contacts)
    elif command[0] == "all":
        if len(command) != 1:
            return "Invalid command format."
        return show_all_contacts(contacts)
    else:
        return "Unknown command."

contacts = {}

while True:
    command = input("Enter a command: ")
    if not command:
        break
    print(handle_command(command, contacts))
