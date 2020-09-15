'''
Contains the secret password that can be stored and changed here.
'''

def hold_password():
    secret_credentials = '123456789' # Enter your secret here.
    return secret_credentials

if __name__ == "__main__":
    print(f"password is-\n{hold_password()}")
