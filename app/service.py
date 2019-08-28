from tinydb import TinyDB, Query
import datetime

__author__ = "Mehdi Ben Taarit"

def program(command):
    """ process the command written in the CLI and determine which functino to call !"""
    args = (command.lower()).split()
    if len(args) == 1 :
        profile_user(args)
    else:
        if args[1] == 'follows':
            follow_user(args)
        elif args[1] == 'add':
            add_user(args)
        elif args[1] == 'wall' :
            wall_user(args)
        elif args[1] == '->' :
            args = command.split('->')
            post_user(args)
        else:
            print ('\tMake sure your input is correct, type "help options" for more info ')  

def add_user(inputs):
    """ Add function of new user """
    #Missing verification condition for duplicity !
    if '_' in name:
        raise
    else:    
        name = inputs[0]
        created = datetime.datetime.now()
        users_table = TinyDB('users.json')
        users_table.insert({'name': name, 'created': datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')})
        print('user added !')
        
def follow_user(inputs):
    """ Subscribe function to other users. """
    #Missing verification of duplicated entry and non exiting users
    user = inputs[0]
    follow = inputs[2]
    users_relation_table = TinyDB('users_follow.json')
    users_relation_table.insert({'user': user, 'follow': follow})
    print('subscribed with success !')
    
def profile_user(inputs):
    """ Function to display user posts. """
    posts = get_posts(inputs[0])
    posts.sort(key=order_by_time)
    for post in posts:
        print(post['user']+'>>\t'+post['post']+ '  ('+str(post['time'])+' min. ago)')

def wall_user(inputs):
    """ Function to display user posts and follwed posts. """
    feeds = get_posts(inputs[0])
    subscribers = get_subscribers(inputs[0])
    for subscriber in subscribers:
        feeds.extend(get_posts(subscriber['follow']))
    feeds.sort(key=order_by_time)
    for post in feeds:
        print(post['user']+' - '+post['post']+ '  ('+str(post['time'])+' min. ago)')

def post_user(inputs):
    """ Function to post message on user wall. """
    user = inputs[0]
    post = inputs[1]
    posts_table = TinyDB('users_posts.json')
    posts_table.insert({'user': user[:-1], 'post': post[1:], 'published':datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')})
    return

def get_subscribers(user):
    """  Function that fetche all subcribers of a user """
    subscribers = Query()
    db = TinyDB('users_follow.json')
    res = db.search(subscribers.user == user)
    return res
    
def get_posts(user):
    """ Function to fetch all post for a user """
    Posts = Query()
    db = TinyDB('users_posts.json')
    res = db.search(Posts.user == user)
    return res

def order_by_time(elem):
    """ Sort values according to the time of posting """
    t1 = datetime.datetime.strptime(elem['published'], '%Y%m%d %H:%M:%S')
    t2 = datetime.datetime.now()
    diff = (t2 - t1).total_seconds() / 60
    elem['time'] = int(round(diff))
    return diff
