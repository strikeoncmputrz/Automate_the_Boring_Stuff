#Displays a player's inventory and adds loot to it

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'ruby']

def addToInventory(loot, inventory):
	for i in loot:
		if i in inventory:
			inventory[i] += 1
		else:
			inventory[i] = 1

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))

displayInventory(stuff)
addToInventory(dragonLoot, stuff)
displayInventory(stuff)

