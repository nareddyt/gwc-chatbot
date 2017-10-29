import datetime


def choose_action(action, data):
    text = "Looking for action..."

    if action == "hello":
        text = hello(data)
    elif action == "time":
        text = get_time(data)
    else:
        text = "No action matched!"

    return text


def hello(data):
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello World"
    return text


def get_time(data):
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    text = "The time is %d:%d" % (hour, minute)
    return text
