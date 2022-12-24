# import
import os

class Error(Exception):
    pass
class UserNameTypoError(Error):
    """Raised when user type wrong account number"""
    pass
class AccountNumberTypoError(Error):
    """Raised when user type wrong account number"""
    pass
class AccountExistsError(Error):
    """Raised when user already had an account"""
    pass
class NoAccountError(Error):
    """Raised when user did not had an account, wanna delete account"""
    pass

# Functions
def addAccount(n, aN, iA, B):
    """
    Store new account information
    
    n: name
    aN: accountNum
    iA: initial amount
    B: Balance
    
    """
    all_accounts = os.listdir() 
    
    if n == "" or aN == "":
        print("All fields required!")
        return "All fields required!"
 

    for name_check in all_accounts:
        
        try: 
            if n == name_check:
                raise AccountExistsError
        except:
            print("AccountExistsError")
            print("Account Already Exists!")
            return "Account Already Exists!"
            
            
        else:
            new_file = open(n, "w")
            new_file.write(n + '\n')
            new_file.write(str(aN) + '\n')
            new_file.write(str(iA) + '\n')
            new_file.write(str(B) + '\n')
            new_file.close()
            
# Read (e.g. for validation)


def validate(n, aN):
    all_accounts = os.listdir()
    try:
        if n not in all_accounts:
            raise UserNameTypoError
        else:
            try:
                file = open(n, "r")
                file_data = file.read()
                file_data = file_data.split('\n')
                accountNum = file_data[1]
                
                if str(aN) != accountNum:
                    raise AccountNumberTypoError
                else:
                    print("Validation Pass!")
                    return True
            except AccountNumberTypoError:
                print("AccountNumberTypoError")
                print("Please check your account number!")
                return "Please check your account number!"
    except UserNameTypoError:
        print("UserNameTypoError")
        print("Please check your spell of name!")
        return "Please check your spell of name!"
    return "Validation Pass!"
    

# Delete an existing account
def delAccount(n, aN):
    try:
        if validate(n, aN) != True:
            raise NoAccountError
    except:
        print("NoAccountError")
    else:
        os.remove(n)
    

            

    
