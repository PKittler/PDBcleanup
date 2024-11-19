import os

'''
Entry point for PDBcleanup
params: string filepath
'''
def cleanup(filepath: str):
    print("Start Cleanup Process")

    # extract filename from filepath
    filename = os.path.basename(filepath)

    # extract path from filename
    path = os.path.dirname(filepath)

    # read file at filepath
    pdb = readfile(filepath)

    # list for relevant lines of pdb
    cleanedfile = []

    # clean pdb line by line
    for line in pdb:
        if extractline(line) != None:
            cleanedfile.append(extractline(line))

    # write cleaned pdb to file
    writefile(path, filename, cleanedfile)

'''
function: readfile
params: string filename
description: reads a file line by line and returns all lines
'''
def readfile(filename: str):
    print("Read PDB file")
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

'''
function: writefile
params: path, filename, list content
description: writes a file line by line
'''
def writefile(path, filename, content: list):
    os.makedirs(path + "/clean/", exist_ok=True)
    print("Write in folder:", path + "/clean/")
    print("Write c_" + filename)

    with open(path + "/clean/c_" + filename, "w") as file:
        for line in content:
            file.write(str(line))

'''
function: extractline
params: line
description: checks if line starts with "ATOM", if true, then returns this line
'''
def extractline(line):
    if line.startswith("ATOM"):
        return line
