import csv
import json
import os
from addUnfilledCategories import addUnfilledCategories
dirPath = os.path.dirname(os.path.realpath(__file__))

cats = ["glitchless", "legacy", "unrestricted", "inbounds", "oob"]



def formatTime(seconds):
    ms = seconds - seconds//1
    seconds = seconds//1

    finalString = ""
    hours = seconds//3600
    if hours != 0:  
        finalString += str(int(hours))+":"
    seconds = seconds%3600

    minutes = seconds//60
    if minutes != 0:
        finalString += str(int(minutes))+":"

    seconds = seconds%60

    finalString += str(int(seconds)).zfill(2)+"."
    if not str(ms) == "0":
        finalString += (str(round(ms, 3)).split(".")[1])
    else:
        finalString += (str(round(ms, 3)))

    return finalString

def generate():
    with open(dirPath+"/data/runnerProfiles.json", "r") as f:
        runners = json.load(f)


    for cat in cats:
        leaderboard = []
        for runner in runners.keys():
            runnerValues = addUnfilledCategories(runners[runner])
            if runnerValues[cat]:
                leaderboard.append([runner, runnerValues[cat]])

        output = sorted(leaderboard, key=lambda k: k[1])



        with open(dirPath+"/output/"+cat+"Leaderboard.csv", "w", newline="") as f:
            e = csv.writer(f, delimiter=",")
            for row in output:
                row[1] = formatTime(row[1])
                e.writerow(row)

if __name__ == "__main__":
    generate()
