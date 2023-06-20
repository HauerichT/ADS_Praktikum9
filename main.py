from datetime import datetime


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

    def delete(self, key):
        print("Delete", key)

    def printHashTable(self):
        print("\n--- Hash-Tabelle ---")
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


def readFile():
    try:
        with open('data.txt', 'r') as f:
            dataInFile = f.read()
            arrFileData = dataInFile.split(",")
            for s in range(len(arrFileData)):
                arrFileData[s] = arrFileData[s].strip()
            return arrFileData
    except FileNotFoundError:
        print("Auslesen der Datei fehlgeschlagen!")
    finally:
        f.close()
        print("Daten aus data.txt eingelesen.\n")


# Driver code
if __name__ == '__main__':
    ht = HashTable()
    # Startzeitpunkt: einlesen und eintragen der 50 Datensätze
    startTime = datetime.now()
    # 50 Datensätze initial einlesen
    filedata = readFile()
    # Datensätze in Hash Tabelle eintragen
    for i in filedata:
        ht.insert(i)
    # Endzeitpunkt: einlesen und eintragen der 50 Datensätze
    endTime = datetime.now()
    # Benötigte Zeit ausgeben
    diffTime = (endTime - startTime).total_seconds()
    print("Zeit einlesen und eintragen 50 Datensätze:", diffTime, "Sekunden")

    # Menü
    while True:
        print("\n--- Menü ---")
        print("1. Datensatz hinzufügen")
        print("2. Datensatz löschen")
        print("3. Hashtabelle anzeigen")
        print("4. Hashtabelle speichern")
        print("5. Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            record = input("Geben Sie den neuen Datensatz ein: ")
            ht.insert(record)
            print("Datensatz wurde hinzugefügt.")
        elif choice == "2":
            record = input("Geben Sie den zu löschenden Datensatz ein (Key): ")
            ht.delete(record)
            print("Datensatz wurde gelöscht.")
        elif choice == "3":
            ht.printHashTable()
        elif choice == "4":
            print("Speichern")
        elif choice == "5":
            break
        else:
            print("Ungültige Auswahl.")
