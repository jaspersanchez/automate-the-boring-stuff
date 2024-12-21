stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


# create function that accepts the inventory as parameter and prints the iventory item: quantity
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print()
    print("Total number of items: " + str(item_total))


def addToInventory(inventory: dict, addedItems):
    # loop through addedItems
    for item in addedItems:
        # check if item exist
        # if item exist add to existing item
        # else add new entry
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


# Practice project 1
displayInventory(stuff)
print()
# Practice project 2
inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
