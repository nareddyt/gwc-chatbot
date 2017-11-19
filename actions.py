import datetime


def choose_action(action, params):
    text = "Looking for action..."

    if action == "hello":
        person_name = params.get("given-name")
        text = hello(person_name)
    elif action == "hello-foreign-language":
        language = params.get("language")
        text = hello_language(language)
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


def hello_language(language):
    """
    Says "Hello" in foreign languages
    """
    print('hello foreign language action')

    text = None
    
    if language == "Spanish":
        text = "¡Hola!"
    elif language == "French":
        text = "Bonjour!"
    elif language == "German":
        text = "Guten Tag!"
    elif language == "Russian":
        text = "Salve!"
    else:
        text = "No language detected"
    
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
