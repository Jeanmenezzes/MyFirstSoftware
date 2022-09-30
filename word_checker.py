# All those functions contains two responses: Where is the mistake and why this is wrong
# In case of exists an error this wil return a tuple contain False and what error is
# In case of no exists it this will return a tuple contain True and a void value

def email_features(email):
    error = 'This Email is Invalid.'
    if email == '':
        return False, error
    if email.count('@') != 1:
        return False, error
    if email.count(' ') != 0:
        return False, error
    return True, None


def password_features(password):
    error = 'This Password is Invalid.'
    if password == '':
        return False, error
    if password.count(' ') != 0:
        return False, error
    return True, None


def name_features(name):
    error = 'This Name is Invalid.'
    if name == '':
        return False, error
    if not name.isalpha():
        return False, error
    return True, None
