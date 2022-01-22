def discover_schema(collection):
    buffer = []
    for item in collection:
        for key in item.keys():
            if key not in buffer:
                buffer.append(key)
    return buffer

def group_map_reduce(collection, key_func, map_func, reduce_func):
    buffer = {}
    for item in collection:
        key = key_func(item)
        value = map_func(item)
        if key in buffer:
            buffer[key] = reduce_func(buffer[key], value)
        else:
            buffer[key] = value
    return buffer

def merge_dicts(a, b, merge_values):
    result = dict(a)
    for key, value in b.items():
        if key in a:
            result[key] = merge_values(key, result[key], value)
        else:
            result[key] = value
    return result
