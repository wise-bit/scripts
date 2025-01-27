import re

def validPhoneNumber(phoneNumber):
    return bool(re.match("(\([0-9]{3}\)\ [0-9]{3}\-[0-9]{4})", phoneNumber) and len(phoneNumber) <= 14)

