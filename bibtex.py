def extractauthor(auth_str: str) -> (str, str):
    split_str = auth_str.split(" ")
    if len(split_str) == 1:
       return (split_str[0], "")
    elif "," in auth_str:
        split_str = auth_str.split(", ")
        return split_str[0], split_str[1]
    else:
        return split_str[-1],' '.join(split_str[:-1])

def extractauthors(auth_str: str):
    split_str = auth_str.split(" and ")
    res = []
    for author in split_str:
        res += [extractauthor(author)]
    return res

#expected return: surname, firstname
'''

    elif "and" in auth_str:
        auth_str = auth_str.split(" and ")

'''