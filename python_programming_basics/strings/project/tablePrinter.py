#! python3

tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(table):
    colWidths = [0] * len(table)
    # Get the highest string length on every row
    for i in range(len(table)):
        maxLength = []
        for str in table[i]:
            maxLength.append(len(str))
        colWidths[i] = max(maxLength)

    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(table[x][y].rjust(colWidths[x] + 1), end="")
        print()

    return colWidths


printTable(tableData)
