#!/usr/bin/env python3

def validate_username(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("Username must be a string")
    if minlen < 5:
        raise ValueError("minlen must be at least 5")
    if len(username < minlen):
        return False
    if not username.isalnum():
        return False
    if username[0].isnumeric():
        return False
    return True 
