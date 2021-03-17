def toString(item):
    return f'"{item}"'if isinstance(item, str)else str(item)
