#!/usr/bin/python3
""" HBNB cmd class """
from models.base_model import BaseModel
from models import storage
import cmd

blueprint = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """airBNB main command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of line command to exit the program"""
        return True

    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_create(self, arg):
        '''creates new instance of class'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        else:
            new_b = blueprint[args[0]]()
            storage.save()
            print(new_b.id)

    def help_create(self):
        """Documentation for how create works"""
        print("Creates a new instance of the specified class Class,")
        print("saves it to the JSON file and prints the id.")
        print("Usage: Create <className>\n")

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def help_show(self):
        """Documentation for how show is executed"""
        print("Prints the string representation of instance")
        print("based on the class name and id.")
        print("Usage: show <className> <id>\n")

    def do_destroy(self, arg):
        '''Deletes an instance using class name and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """Documentation for how destroy is executed"""
        print("Deletes an instance based on the class name and id,")
        print("(saves the change into the JSON file).")
        print("Usage: destroy <className> <id>\n")

    def do_all(self, arg):
        '''Prints __str__ of all instances'''
        args = arg.split()
        obj_dict = storage.all()
        string = []
        if len(args) != 0:
            if args[0] not in blueprint:
                print("** class doesn't exist **")
                return
            else:
                for key in obj_dict:
                    if obj_dict[key].__class__.__name__ == args[0]:
                        string.append(str(obj_dict[key]))
        else:
            for key in obj_dict:
                string.append(str(obj_dict[key]))
        print(string)

    def help_all(self):
        '''Documentation for how all is executed'''
        print("Prints all string representation of all instances")
        print("based or not on the class name.")
        print("Usage: all <className> OR all\n")

    def do_update(self, arg):
        '''updates an instance using user input'''
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in blueprint:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in obj_dict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance = obj_dict[f"{args[0]}.{args[1]}"]
            args[3] = args[3].strip("\"\'")
            if args[2] in instance.__dict__:
                args[3] = type(instance.__dict__[args[2]])(args[3])
            instance.__dict__[args[2]] = args[3]
            instance.save()
            storage.save()

    def help_update(self):
        '''Documentation for how update is executed'''
        print("Updates an instance based on the class name and id")
        print("adding or updating attribute (saves changes to JSON file)")
        print("Usage: update <class name> <id> <att name> \"<att value>\"\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

