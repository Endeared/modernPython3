def list_check(checklist):

    for item in checklist:
        print(item)
        if not isinstance(item, list):
            return False

    return True