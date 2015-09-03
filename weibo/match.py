__author__ = 'koala'
# get the final result
# -*- coding:utf8 -*-z


def match(path_segmentation, path_result, path_morph_entity):
    inputFile = open(path_segmentation, 'r')
    outputFile = open(path_result, 'w')
    matchListFile = open(path_morph_entity, 'r')

    matchList = []
    for line in matchListFile.readlines():
        if line[-1] == '\n':
                line = line[0:-1]
        tmp = line.split(" ")
        matchList.append(tmp[0])

    dictMatch = dict.fromkeys(matchList, 0)

    for line in inputFile.readlines():
        tmpList = line.split(" ")
        for morph in matchList:
            if morph in tmpList:
                dictMatch[morph] += 1

    for item in dictMatch:
        outputFile.write(item + ":" + str(dictMatch[item])+"\n")
