import re

def censor(check):
    checkFor = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return checkFor.sub("CENSORED", check)