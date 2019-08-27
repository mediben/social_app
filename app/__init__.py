from .model import Socially
import os
import sys

__author__ = "Mehdi Ben Taarit"

def main():
    check_db()
    socli = Socially()
    socli.prompt = 'socially>>'
    socli.cmdloop(login())
    
def login():
    """ Intro text for the CLI app """
    os.system('clear')
    print("**********************************************")
    print("**          Let's play socially !           **")
    print("**********************************************")
    print("\t Type help for more info about how it works. ")

def check_db():
    """ Verify if db files are created, if not creat them """
    # DB file for subscribers
    if not os.path.isfile(os.getcwd()+'/users_follow.json'):        
        with open(os.getcwd()+'/users_follow.json', 'w'): pass
    # DB file for user posts
    if not os.path.isfile(os.getcwd()+'/users_posts.json'):        
        with open(os.getcwd()+'/users_posts.json', 'w'): pass
    # DB file for saved users
    if not os.path.isfile(os.getcwd()+'/users.json'):        
        with open(os.getcwd()+'/users.json', 'w'): pass
