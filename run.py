from user import User
import pyperclip
import random

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

def copy_user(User):
        pyperclip.copy(User)
        pyperclip.paste(User)

def main():
    print("Hello Welcome to Password Manager. What is your name?")
            your_name = input()

            print(f"Hello {'your_name'}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : ca - create a new account,lg - login to your account, da - display accounts, del - delete account, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print(" Lets create a New Account")
                            
                            print ("Provide Username ....")
                            user_name = input('username: ')

                            print("Account type; Fb,IG,twitter or email ...")
                            acc_type = input('acc_type: ')

                            print("Input password ...")
                            password = input('password: ')

                            print("Confirm password ...")
                            confirm_password = input('Confirm Password: ')
                            print('Congratulations your new account is set up!!')

                            save_users(create_user(user_name,acc_type,password,confirm_password)) # create and save new user account.
                            print ('\n')
                            print(f"New User {user_name} {acc_type} created")
                            print ('\n')

                    elif short_code =='lg':
                        print('Welcome back')
                        print('Enter credentials')
                        entered_user_name = input('username:')
                        entered_acc_type = input('acc_type: ')
                        password = input('password: ')
                        confirm_password = input('confirm password: ')
                        print('login was successful.')
                    elif short_code == 'da':

                            if display_users():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.user_name} {user.acc_type} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')

                    elif short_code == 'da':

                            print("Are you sure about deleting?")

                            print("Input old user account details first")
                            user_name = input('username: ')
                            acc_type = input('acc_type: ')
                            password = input('password: ')

                            print("Lets change get that new username and password")
                            user_name = input('username: ')
                            password = input('password: ')
                            confirm_password = input('confirm-password: ')

                            print('Yeei!, The account is finally updated!!')

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

            if __name__ == '__main__':
    
                main()