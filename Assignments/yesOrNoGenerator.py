def yes_or_no():
    count = 1
    while True:
        if count % 2 == 0:
            yield "no"
        else:
            yield "yes"
        count += 1