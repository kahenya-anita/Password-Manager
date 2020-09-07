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