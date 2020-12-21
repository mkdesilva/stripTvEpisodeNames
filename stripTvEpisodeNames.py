import os
import sys
import re

# Rename files in a folder e.g
# The Mandalorian S01E01.mkv -> Episode S01E01.mkv 
def stripTvEpisodeNames(folderPath):
    files = os.listdir(folderPath)
    for fileName in files:
        fileNameFormat = re.search(r's\d+e\d+', fileName, re.IGNORECASE)
        extensionStartIndex = fileName.rfind('.')
        extension = fileName[extensionStartIndex:len(fileName)]

        if fileNameFormat is None:
            return

        oldFile = folderName + "\\" + fileName
        newFileName = fileNameFormat.group() + extension
        filePath = folderName + "\\" + newFileName
        print(filePath)
        os.rename(oldFile, filePath)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folderName = sys.argv[1]
    else:
        folderName = input("Please provide the folder name: \n")
    stripTvEpisodeNames(folderName)