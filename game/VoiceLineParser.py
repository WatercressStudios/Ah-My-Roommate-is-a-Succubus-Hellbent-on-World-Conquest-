#MonMax18 Voice Line Parser
print('Please enter the file to be parsed. Include the file path.')
inputFilePath = input()

inputFileName = inputFilePath.rsplit('\\', 1)[1]
filePath = inputFilePath.rsplit('\\', 1)[0]

outputFileName = '\\parsed_' + inputFileName
outputFilePath = filePath + outputFileName

print('Please enter the scene\'s route tag.')
routeTag = input()

print('Please enter the scene number.')
sceneNumber = input()

lineCount = 1

with open(inputFilePath, encoding="utf8") as infile, open(outputFilePath, 'w') as outfile:
    for line in infile:
        if 'yum' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Yumi (Kathy Pfautsch)\n')
            outfile.write(line)
            lineCount += 1
        elif 'kam' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Kamika (Ariane Marchese)\n')
            outfile.write(line)
            lineCount += 1
        elif 'sat' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #S-Tan (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        elif 'luc' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Lucca (Victoria Wong)\n')
            outfile.write(line)
            lineCount += 1
        elif 'moe' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Moe (CJ Heineman)\n')
            outfile.write(line)
            lineCount += 1
        elif 'sta' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Stacey (Ashe Thurman)\n')
            outfile.write(line)
            lineCount += 1
        elif 'dee' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mister Deeks (???)\n')
            outfile.write(line)
            lineCount += 1
        elif 'ber' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mrs Bernardinelli (???)\n')
            outfile.write(line)
            lineCount += 1
        elif 'pg1' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Partygoer 1 (???)\n')
            outfile.write(line)
            lineCount += 1
        elif 'pg2' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Partygoer 2 (???)\n')
            outfile.write(line)
            lineCount += 1
        elif 'lev' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Levi (???)\n')
            outfile.write(line)
            lineCount += 1
        elif 'mst' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Male Student (???)\n')
            outfile.write(line)
            lineCount += 1 
        elif 'fst' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Female Student)\n')
            outfile.write(line)
            lineCount += 1 
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
