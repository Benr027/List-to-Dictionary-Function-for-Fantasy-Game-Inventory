
# Fantasy Game Inventory
def displayInventory(dictoInventory):
    '''The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detail-
ing how many of that item the player has.'''
    print("Inventory:")
    totalNumber = 0
    for k, v in dictoInventory.items():

        print(f'{v} {k}')
        totalNumber += v
    print(f'Total number of items: {totalNumber}')
    # return totalNumber

# List to Dictionary Function for Fantasy Game Inventory


def addToInventory(inventory, addedItems):
    '''Afunction named addToInventory(inventory, addedItems) , where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot .
The addToInventory() function should return a dictionary that represents the
updated inventory.'''
    count = {}
    for i in addedItems:
        count.setdefault(i, 0)
        count[i] = count[i]+1

    for k, v in count.items():
        if k not in inventory:
            inventory[k] = v
        else:
            inventory[k] = inventory[k] + v
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
