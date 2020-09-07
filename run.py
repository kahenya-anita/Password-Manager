from user import User
def create_user(user_name,acc_type,password,confirm_password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,acc_type,password,confirm_password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    User.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()