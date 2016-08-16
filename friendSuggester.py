from node import *

def mockData():
	users = [
		{ "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Tho" },
        { "id": 6, "name": "Thr" },

	]

	# connectivity tree
	tree = Tree(0, Tree(1, Tree(2), Tree(3)), Tree(4, Tree(5), Tree(6)))

	return tree

def interestsofUsers():
	interests = [ 	(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
					(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        		  	(1, "Postgres"), 
				]

def countHowManyFriends(root):
	if root is None:
		return 0
	
	num_left = 0
	num_right = 0
	
	if root.left is not None:
		num_left = 1 + countHowManyFriends(root.left)
	
	if root.right is not None:
		num_right = 1 + countHowManyFriends(root.right)

	return num_left + num_right

def sizeOfFriendTree(tree):
	count = 1
	if tree is None:
		return 0

	if tree is not None:
		if tree.left is not None:
			count += sizeOfFriendTree(tree.left)
		if tree.right is not None:
			count += sizeOfFriendTree(tree.right)
	
	return count

def recommendScientist(friend, arrayOfFriends):
	if friend is None:
		return 0
	if friend is not None:
		if friend.left is not None:
			arrayOfFriends.append(friend.left)
			recommendScientist(friend.left, arrayOfFriends)
		if friend.right is not None:
			arrayOfFriends.append(friend.right)
			recommendScientist(friend.right, arrayOfFriends)

def main():
	tree = mockData()
	find_friend = tree.right

	friends = countHowManyFriends(find_friend)
	print "number of friends for" + " " + str(find_friend) + " " + "is:" 
	print friends

	size = sizeOfFriendTree(tree)
	print "size of tree:" + " " + str(size)

	arrayOfFriends = []
	recommendScientist(tree.right, arrayOfFriends)

	# remove friends that are already friends
	# with you
	arrayOfFriends.remove(find_friend.right)
	arrayOfFriends.remove(find_friend.left)

	if len(arrayOfFriends) == 0:
		print "No friends to recommend"

	for i in range(len(arrayOfFriends)):
		print "Your friends: " + " " + str(arrayOfFriends[i])

if __name__ == '__main__':
	main()

