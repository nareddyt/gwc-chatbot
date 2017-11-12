import datetime


def choose_action(action, params):
    text = "Looking for action..."

    if action == "hello":
        person_name = params.get("given-name")
        text = hello(person_name)
    elif action == "time":
        text = get_time()
    else:
        text = "No action matched!"

    return text


def hello(person_name):
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello " + str(person_name)
    return text


def get_time():
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    text = "The time is %d:%d" % (hour, minute)
    return text
