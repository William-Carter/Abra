import json
import os
import csv
import PortalPlayer
dirPath = os.path.dirname(os.path.realpath(__file__))
records = {
    "glitchless": 869.205, 
    "legacy": 681.820,
    "unrestricted": 639.495,
    "inbounds": 515.505,
    "oob": 353.46
}

def getRunners() -> dict:
    with open(dirPath+"/data/runnerProfiles.json", "r") as f:
        runnerProfiles = json.load(f)

    with open(dirPath+"/data/attributes.json", "r") as f:
            attributes = json.load(f)


    runners = [PortalPlayer.Player(x, runnerProfiles[x], records, attributes) for x in runnerProfiles.keys()]
    return runners


def calculate():
    runners = getRunners()
    sortedRunners = sorted(runners, key=lambda k: k.score, reverse=True)
    output = [(x.name, round(x.score, 2)) for x in sortedRunners]
    with open(dirPath+"/output/ABRA.csv", "w", newline="") as f:
        e = csv.writer(f, delimiter=",")
        for row in output:
            e.writerow(row)
    
if __name__ == "__main__":
     calculate()