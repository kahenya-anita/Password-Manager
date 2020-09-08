#!/usr/bin/env python3.6
import user
import password

password_obj=password.Password()
def sign_up():
    '''
    Function that allows a new user to sign up.
    '''
    
    username_signup=" "
    password_signup=" " 

    print(" ")
    print("-----Sign up here-----")
    username_valid=True
    while username_valid:
        username_signup=input("Username (at least 5 chars): ")
        if len(username_signup)<5:
            username_valid=True
            print("**Username too short. Try again.")
        else:
            username_valid=False 
        
    want_password_valid=True
    while want_password_valid:        
        want_sys_password=input("Want system generated password? (Y/n): ")        
        if want_sys_password=="Y":
            want_password_valid=False
            password_signup=password_obj.gen_password()            
            print("Your password: "+password_signup+" (copied to clipboard)")
            print("Signup successful!")
        elif want_sys_password=="n":
            password_signup=input("Password (at least 5 chars): ")
            password_confirm=input("Confirm password: ")
            if len(password_signup)<5:
                want_password_valid=True
                print("**Password too short. Try again.")
            elif password_confirm==password_signup:
                print("Signup successful!")                
                want_password_valid=False
            else:
                print("**Passwords did not match. Try again.")
                want_password_valid=True
        else:
            print("**Invalid choice. Choose Y/n")
            want_password_valid=True

    new_user=user.User(username_signup,password_signup)
    new_user.add_user(new_user)



def main():
    print("Hello Welcome to Password Manager. What is your name?")
    your_name = input('Your name: ')

    print(f"Hello {'your_name'}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : ca - create a new account,lg - login to your account, da - display accounts, del - delete account, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print("-----Lets create a New Account-----")
                            
                            print ("Provide Username ....")
                            user_name = input('username: ')

                            print("Account type; Fb,IG,twitter or email ...")
                            acc_type = input('acc_type: ')

                            print("Input password ...")
                            password = input('password: ')

                            print("Confirm password ...")
                            confirm_password = input('Confirm Password: ')
                            print('Congratulations your new account is set up!!')

                            (user_name,acc_type,password,confirm_password) # create and save new user account.
                            print ('\n')
                            print(f"New User {user_name} {acc_type} created")
                            print ('\n')

                    elif short_code =='lg':
                        print('---Welcome back---')
                        print('Enter credentials')
                        login_user_name = input('username: ')
                        login_acc_type = input('acc_type: ')
                        login_password = input('password: ')
                        confirm_password_login = input('confirm password: ')
                        login_valid = user.User.check_login(login_user_name,login_password,login_acc_type,confirm_password_login)
                        if login_valid:
                            print('login was successful.')
                            is_login = False
                            user_obj = user.user.return_user(login_user_name,login_acc_type,login_password,confirm_password_login)
                            main(login_user_name,user_obj)
                        else:
                                print('Login was unsuccessful.Please try again.')
                    elif short_code == 'da':

                            if display_users_():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for user in display_user():
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