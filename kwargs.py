import random
def time_activity(*args, **kwargs):
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)

time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
