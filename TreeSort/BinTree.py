#!/bin/python3

# !/bin/python3

class treenode:
    def __init__(self, id):
        self.id = id

class NTree:
    def __init__(self):
        self.n = 1
        self.root = []
        self.subTrees = []

    def save(self):
        """
        Deze functie zal de items in de binaire boom omzetten naar een dictionary.
        Als output zal deze functie self.toReturn returnen.
        """
        self.toReturn = {}

        if self.root[0].id == None:
            self.toReturn = None
        else:
            # als de root wel een waarde bezit, maak dan root aan en voeg de id van de node toe.
            self.toReturn['root'] = []
            self.toReturn['root']=self.root[0].id

        # Maak 'children' aan als er kinderen bestaan.
        for j in self.subTrees:
            if j.root!=[]:
                self.toReturn['children']=[]
                break
        # recursieve loop om kinderen toe te voegen in 'children' als dat van toepassing is.
        for i in self.subTrees:
            if i.root != []:
                self.toReturn['children'].append(i.save())

        return self.toReturn

    def inorder(self):
        # print(self.root[0],self.subTrees)
        if self.subTrees==[]:
            return
        else:

            self.subTrees[0].inorder()
            print(self.root[0].id)
            self.subTrees[1].inorder()
            return self.root[0]

    def maxinlist(self,list):
        a=-10e10
        for i in list:
            if a<i:
                a=i
        return a

    def hoogte(self):
        comparisonlist = []

        if self.subTrees == []:
            return 1

        for i in self.subTrees:
            comparisonlist.append(i.hoogte())
        return (1 + self.maxinlist(comparisonlist))

    def insert(self,node):
        goto = 0

        a = len(self.root)

        if self.root == []:
            self.root.insert(0,node)
            for j in range(self.n+1):
                self.subTrees.append(NTree())
        else:
            if node.id > self.root[0].id:
                goto+=1

            if self.subTrees==[]:
                for j in range(self.n+1):
                    self.subTrees.append(NTree())
            self.subTrees[goto].insert(node)
