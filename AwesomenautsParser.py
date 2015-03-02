#!/usr/bin/python

__author__ = 'mcstephe'

import sys  # Use to get args from CLI
import argparse  # Use to parse CLI args
import fnmatch  # Use to compare filename
import os
import Player  # Custom Player class
import xml.etree.ElementTree as ET  # Used to parse XML file
from collections import Counter  # Used to count number of player occurences

#rootdir = 'C:/Program Files (x86)/Steam/SteamApps/common/Awesomenauts/Data/Replays/'
#targetfile = 'Replays.info'
#targetwritefile = 'names.txt'
#localname = 'Stevenski8'


def parse():
    #for path,dirs,files in os.walk('C:/Program Files (x86)/Steam/SteamApps/common/Awesomenauts/Data/Replays/'):
    for path,dirs,files in os.walk(rootdir):
        for fn in files:
            if fnmatch.fnmatch(fn, 'Replays.info'):
                xml_file = open(os.path.join(path, fn))
                tree = ET.parse(xml_file)
                for replays in tree.iter(tag='Replay'):
                    for characters in replays.iter(tag='Character'):
                        if (searchForName(names, characters.get('name'))):
                            names[characterLocation].total_played += 1
                            #print(characters.get('name'))
                            # Name exists in list. Increase its count
                            #if (characterLocation != 0):
                                #print("Position is " + str(characterLocation))
                            #print(characterLocation)
                        elif (characters.get('name') != ""):
                            # Name doesn't exist and isn't blank.
                            #print(characterLocation)
                            player = Player.Player(characters.get('name'))
                            player.total_played += 1
                            names.append(player)
                            #names.append(characters.get('name'))
                        else:
                            pass
                            

                        #local_player_team =
                        #print (items.tag, items.attrib)
                        #print (items.get('name'))
                        #if (items.get('name') != "" and items.get('name') != "Stevenski8"):
                        #    names.append(items.get('name'))
                xml_file.close()
    return

def writetofile():
    with open(targetwritefile.name, 'w') as output_file:
        #output_file.write("Hello World\n")
        for elements in names:
            #print (elements)  # printing will cause unicode error on some names
            output_file.write(elements.name + " " + str(elements.total_played) + '\n')
    output_file.close()
    return


def searchForName(alist, character):  # Performs a simple linear search of characters name in the character list
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos].name == character:
            characterLocation = pos
            #print(characterLocation)
            found = True
        else:
            pos = pos+1

    return found
    

def get_cnt(lVals):
    d = dict(zip(lVals, [0] * len(lVals)))
    for x in lVals:
        d[x] += 1
    return d


def is_valid_file(parser, arg):
    """Check if arg is a valid file that already exists on the file
       system.
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument("-n", "--name",
                        dest='name',
                        metavar='NAME',
                        action='store',
                        help='Character name of local player'
    )

    parser.add_argument("-i", "--input",
                        dest='input',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        metavar='INPUT',
                        help='Input file name'
    )

    parser.add_argument("-d", "--directory",
                        dest='directory',
                        action='store',
                        metavar='DIRECTORY',
                        help='Directory to scan'
    )

    parser.add_argument("-o", "--output",
                        dest='output',
                        type=argparse.FileType('w'),
                        #default=sys.stdout,
                        metavar='OUTPUT',
                        help='Output file name'
    )

    return parser



if __name__ == "__main__":
    args = get_parser().parse_args()

    localname = args.name
    rootdir = args.directory
    targetwritefile = args.output

    characterLocation = 0; 
    #print(localname)
    #print(rootdir)
    #print(targetwritefile)
    #print(targetwritefile.name)

    names = []

    parse()
    writetofile()
#counttest = Counter(names)
#print (counttest)

#p1 = Player.Player("Player1")
#p1.match_outcome(True, True)
#p1.match_outcome(False, False)
#print(p1.was_friendly, p1.ratio())
