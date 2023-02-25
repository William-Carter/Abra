import os
import json
dirPath = os.path.dirname(os.path.realpath(__file__))
class Player:
    def __init__(self, name, pbs, kinchStandards, attributeStandards):
        self.name = name
        self.pbs = pbs
        self.kinches = self.getKinches(kinchStandards)
        self.attributes = self.getAttributes(attributeStandards)
        self.score = self.getFinalSum(attributeStandards)


    def getKinches(self, kinchStandards: dict) -> dict:
        """
        Calculates kinch ranks for each of the categories, used in calculating the values of each attribute
        """
        kinches = {}
        for category in kinchStandards.keys():
            if category in self.pbs.keys():
                kinches[category] = kinchStandards[category]/self.pbs[category]*100
            else:
                kinches[category] = 0

        return kinches
    
    def getAttributes(self, attributeStandards: dict) -> dict:
        """
        Calculates player attributes for each attribute
        """

        attributes = attributeStandards

        playerAttributes = {}

        for attributeName in attributes.keys():
            attributeValues = []
            for category in self.kinches:
                attributeValues += [self.kinches[category]*attributes[attributeName][category]]
            playerAttributes[attributeName] = max(attributeValues)

        return playerAttributes
    

    def getFinalSum(self, attributeStandards: dict) -> dict:
        """
        Calculates the players final sum, based on their individual attribute values and the weights of those attributes
        """
        finalSum = 0
        for attributeName in self.attributes:
            scaledAttribute = self.attributes[attributeName]*attributeStandards[attributeName]["weight"]
            finalSum += scaledAttribute

        return finalSum