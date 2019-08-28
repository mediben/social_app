from cmd import Cmd
from .service import program

__author__ = "Mehdi Ben Taarit"

class Socially(Cmd):
    def do_options(self):
        """
        Read user posts, <user name>
        Post to the wall, <user name> -> text
        Add a new user to the system, <user name> add
        Read all followed posts by user, <user name> wall
        Follow user timeline, <user name> follows <another user> 
        """
        pass

    def do_exit(self, input):
        """ Type exit to close application and logoff """
        print('\t...loggin off, Bye !')
        return True
    
    def default(self, line):
        return program(line)
