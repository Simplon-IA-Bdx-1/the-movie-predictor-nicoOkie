def split_name(name):
    name_list = name.split(" ")
    for name in name_list:
        firstnames = (len(name_list) - 1)
        firstname = " ".join(name_list[:firstnames])
        lastname = name_list[firstnames]
    return (firstname, lastname)
