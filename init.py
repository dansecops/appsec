#!/usr/bin/env python

# Program that creates a Hash Table manually

# add
# contains

class SimpleHashTable:


    element = []
    tableSize = 0

    def __init__(self, load, tableSize):
        self.load = load
        self.tableSize = tableSize
        #why don't specifiy array len here -> element[tableSize]

    def add(self, element):
        bucketIndex = self.computeHash(element)

        expectedPlace = element[bucketIndex]

        if expectedPlace is None:
            currentNode = expectedPlace
            for i in self.load:
                # This won't work as childElement will never get called:
                if currentNode.childElement is not None:
                    currentNode = currentNode.childElement
                else:
                    #what to do here?
                    currentNode.ChildElement #create a new childElement here
                    return True
                    break
        raise ValueError("Wrong map balance, too many elements for hash map")

    def computeHash(self, element):
        return element % self.tableSize

class Element:
    def __init__(self, childElement):
        self.childElement = childElement

def main():
    print("HI")
    sth = SimpleHashTable(3, 10)
    element = Element(4567)

    print(sth.computeHash(100))



if __name__  == "__main__": main()