import re

def parse_bytes(check):
    binaryList = []
    checkFor = re.compile(r'[0-1]{8}')
    found = checkFor.findall(check)
    return found