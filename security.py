from user import User

def authenticate (username, password):
    
    print("DEBUG: before finding the username")
    user = User.find_by_username (username)
    print("DEBUG: after finding the username")

    if user and user.password == password:
        return user
    return None

def identity (payload):
    user_id = payload['identity']
    return User.find_by_id (user_id)
