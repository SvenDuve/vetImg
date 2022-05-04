import os

originalPath = "/Users/svenduve/HiDrive/vetData/HH_Blut"


for i, el in enumerate(os.listdir(originalPath)[:10]):
    orgFile = os.path.join(originalPath, el)
    renamedFile = os.path.join(originalPath, "blood" + str(1000000 + i) + ".JPG")
    print(orgFile)
    print(renamedFile)


