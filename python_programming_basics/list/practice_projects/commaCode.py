spam = ["apples", "bananas", "tofu", "cats"]


def comma(list):
    # initialize an empty string
    str = ""
    maxIndex = len(list)
    # make a for for the list and append every single item through the list
    for item in range(maxIndex - 1):
        # add the item with comma
        str += list[item] + ", "
    # append the last item in the list
    str += list[-1]
    # return string
    return str


print(comma(spam))
