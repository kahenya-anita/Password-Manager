import pyperclip
class User:
    """
    Class that generates new instances of user-info
    """

    user_list = [] 
    def __init__(self,user_name,acc_type,password,confirm_password):
        '''
        __init__method that helps us define properties for our objects.
        '''
        self.user_name = user_name
        self.acc_type = acc_type
        self.password = password
        self.confirm_password = confirm_password

    def save_user(self):
        '''
        save_user saves user objects to user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
    
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    @classmethod
    def copy_user(cls,User):
        pyperclip.copy(User)
        pyperclip.paste(User)

    def display_users(self,cls):
        '''
        method that returns the user list
        '''
        return cls.user_list