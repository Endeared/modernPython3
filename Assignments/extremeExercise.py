def extremes(list):
    values = []
    lowest = min(list)
    highest = max(list)
    values.append(lowest)
    values.append(highest)
    staticValues = tuple(values)
    return staticValues