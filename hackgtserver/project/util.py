import bcrypt

def generate_first_hashed(password):
    """
        Use this method when creating after getting a new password from a user.
    """
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())
    
def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)