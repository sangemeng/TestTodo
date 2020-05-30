def get_dict_last(dict):
    i = 0
    for k in dict:
        i += 1
        if len(dict) == i:
            return {k: dict[str(k)]}
