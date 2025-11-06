from logging import warning
from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt
def check_strength(password):
    result = zxcvbn(password)
    score = result['score']
    if score == 3:
        return "Strong"
    elif score == 4:
        return "Very Strong"
    else: 
        feedback = result.get("feedback")
        warnings = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = "Weak password: Score of " + str(score)
        response += "\nWarning: " + warning
        reponse += "\nSuggestions: "
        for suggestion in suggestions:
            response += " " + suggestions
    return response

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(),salt)
    return hashed

def verify_password(pw_attempt,hashed):
    if bcrypt.checkpw(pw_attempt.encode(),hashed):
        return "Password is correct"
    else:
        return "Password is incorrect"

if __name__ == "__main__":
    while True:
        password1 = getpass("Enter password: ")
        print(check_strength(password1))
        if check_strength(password1).startswith("Weak"):
            print("Please enter a stronger password")
        else:
            break
    hashed_password = hash_pw(password1)
    print("Hashed password: ", hashed_password)
    attempt = getpass("Enter password to verify: ")
    print(verify_password(attempt,hashed_password))