users = [
    {
        'id': 1,
        'name': 'bob',
        'password': 'asdf'
    }
]

username_mapping = {
    'bob': {
        'id': 1,
        'name': 'bob',
        'password': 'asdf'
    }
}

userid_mapping = {
    1: {
        'id': 1,
        'name': 'bob',
        'password': 'asdf'
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
