import password
import account
import pyperclip

password_obj1 = password.Password()
class Credentials:
    '''
    Class that adds user credentials to the app.
    '''

    def __init__(self):
        self.credentials_list=[]
    
    def add_credential(self):
        '''
        Method to add existing credentials to the app.
        '''
        print(" ")
        print("-----Add credential here-----")
        acc_type=input("Account type: ")
        acc_username=input("Account username: ")
        acc_password=input("Account password: ")
        acc_confirm_password=input("Confirm password: ")
        new_account=account.Account(acc_type,acc_username,acc_password,acc_confirm_password)
        self.credentials_list.append(new_account)
        print(f'{acc_type} account credentials added.')

    def create_credential(self):
        '''
        Method to create new credential and add it to the app.
        '''
        print(" ")
        print("-----Create new credential here-----")
        acc_type=input("Account type: ")
        acc_username=input("Account username: ")
        acc_password=" "

        want_password_valid=True
        while want_password_valid:        
            want_sys_password=input("Want system generated password? (Y/n): ")            
            if want_sys_password=="Y":
                want_password_valid=False
                acc_password=password_obj1.gen_password()                
                print("Your password: "+acc_password+" (copied to clipboard)")
            elif want_sys_password=="n":
                acc_password=input("Account password: ")
                password_confirm=input("Confirm password: ")                
                if acc_password==password_confirm:                                    
                    want_password_valid=False
                else:
                    print("**Passwords did not match. Try again.")
                    want_password_valid=True
            else:
                print("**Invalid choice. Choose Y/n")
                want_password_valid=True    
        
        new_account=account.Account(acc_type,acc_username,acc_password)
        self.credentials_list.append(new_account)
        print(f'{acc_type} account credentials created.')

    def view_credentials(self):
        '''
        Method to display stored credentials.
        '''
        print(" ")
        print("-----View credentials here-----")
        if len(self.credentials_list)==0:
            print("No credentials saved. Add a credential.")
        else:
            for item in self.credentials_list:
                print(f'Account: {item.acc_ty} ; Username: {item.acc_uname} ; Password: {item.acc_pass} ; Confirmpassword: {item.acc_cpass}')

    def delete_credential(self):
        '''
        Method to delete stored credentials.
        '''
        print(" ")
        print("            -Delete-")
        self.view_credentials()
        print(" ")
        if len(self.credentials_list)==0:
            pass
        else:
            delete_valid=True
            while delete_valid:
                acc_delete=input("Type account type to delete: ")
                for item in self.credentials_list:
                    if item.acc_ty==acc_delete:
                        self.credentials_list.remove(item)
                        print(f'{acc_delete} account credentials deleted.')
                        delete_valid=False
                        break
                    else:                        
                        delete_valid=True
                if delete_valid==False:
                    pass
                else:
                    print(f'**Account \'{acc_delete}\' not found. Try again.')

    def copy_credential(self):
        '''
        Method to copy credential username and password to clipboard.
        '''
        print(" ")
        print("     -Copy username & password-")
        self.view_credentials()
        print(" ")
        if len(self.credentials_list)==0:
            pass
        else:
            copy_valid=True
            while copy_valid:
                acc_copy=input("Provide account type: ")
                for item in self.credentials_list:
                    if item.acc_ty==acc_copy:
                        user_n_pass=item.acc_uname+" "+item.acc_pass
                        pyperclip.copy(user_n_pass)
                        print(f'{acc_copy} username & password copied to clipboard.')
                        copy_valid=False
                        break
                    else:                        
                        copy_valid=True
                if copy_valid==False:
                    pass
                else:
                    print(f'**Account \'{acc_copy}\' not found. Try again.')
                              
        
