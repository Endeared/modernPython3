import re

def parse_date(check):
    checkFor = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
    found = checkFor.search(check)
    if found:
        return {
            "d": found.group(1),
            "m": found.group(2),
            "y": found.group(3)
        }