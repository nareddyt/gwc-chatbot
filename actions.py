def choose_action(action, data):
    text = "Looking for action..."

    if action == "hello":
        text = hello_action(data)
    elif action == "something":
        # TODO
        pass
    else:
        text = "No action matched!"

    return text


def hello_action(data):
    # Simple action that responds with hello world
    text = "Hello world"
    return text