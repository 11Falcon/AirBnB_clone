#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""
    prompt = '(hbnb) '
    def do_quit(self,line):
        """exit the program"""
        return True
    def do_EOF(self, line):
        """exit the program"""
        return True
    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
