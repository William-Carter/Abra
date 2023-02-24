import json
import os
import PortalPlayer
dirPath = os.path.dirname(os.path.realpath(__file__))
with open(dirPath+"/data/attributes.json", "r") as f:
            attributes = json.load(f)

testStandards = {"oob": 75, "inbounds": 75, "unrestricted": 75, "legacy": 75, "glitchless": 75}
oobPlayer = PortalPlayer.Player("testPlayer", {"oob": 100}, testStandards, attributes)
inboundsPlayer = PortalPlayer.Player("testPlayer", {"inbounds": 110}, testStandards, attributes)
unrestrictedPlayer = PortalPlayer.Player("testPlayer", {"unrestricted": 100}, testStandards, attributes)
legacyPlayer = PortalPlayer.Player("testPlayer", {"legacy": 100}, testStandards, attributes)
glitchlessPlayer = PortalPlayer.Player("testPlayer", {"glitchless": 100}, testStandards, attributes)
print("oob:", oobPlayer.score)
print("inbounds:", inboundsPlayer.score)
print("unrestricted:", unrestrictedPlayer.score)
print("legacy:", legacyPlayer.score)
print("glitchless:", glitchlessPlayer.score)
