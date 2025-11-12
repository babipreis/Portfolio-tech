# password_strength_checker.py
# Simple Password Strength Checker by Bárbara dos Reis

import re

def check_password_strength(password):
    # Criteria for strong password
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count errors
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error].count(True)

    if errors == 0:
        return "🔒 Strong password"
    elif errors <= 2:
        return "🟡 Medium strength password"
    else:
        return "🔴 Weak password"

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    print(check_password_strength(user_password))
