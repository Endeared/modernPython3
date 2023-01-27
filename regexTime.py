import re

def is_valid_time(check):
    checkFor = re.compile(r'^\d\d?:\d\d$')
    found = checkFor.search(check)
    if found:
        return True
    return False