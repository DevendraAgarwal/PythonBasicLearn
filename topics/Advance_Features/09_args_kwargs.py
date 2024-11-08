#  Args and Kwargs

""" 
args : Arguments / Parameter of A Function
kwargs : Keyword Arguments / Named Parameter of A Function
"""

def args_function(*args):
    for a in args:
        print(a)
        

args_function("test", 123, [1,2,3])

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        

kwargs_function(name = "shaktiman", title = "Superhero")

def both_function(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

both_function('test', 'shaktimaan', 'power', first="test", mid="shaktimaan", last="power")