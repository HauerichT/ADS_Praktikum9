class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self):
        self.hashTable = [None] * 53

    def insert(self, key):
        hashValue = 1
        if self.hashTable[hashValue] is None:
            self.hashTable[hashValue] = Node(key)
        else:
            cur = self.hashTable[hashValue]
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(key)

    def printHashTable(self):
        for j in range(len(self.hashTable)):
            if self.hashTable[j] is not None:
                print("Index " + str(j) + ": ", end="")
                cur = self.hashTable[j]
                while cur.next is not None:
                    print(cur.key, end=", ")
                    cur = cur.next
                print(cur.key)
            else:
                print("Index " + str(j))


# Driver code
if __name__ == '__main__':
    # Create a hash table with
    # a capacity of 5
    ht = HashTable()

    with open('data.txt', 'r') as f:
        dataInFile = f.read()
        arrFileData = dataInFile.split(",")
        for s in arrFileData:
            element = s.strip()
            ht.insert(element)

    ht.printHashTable()
