#-------------------------------------------------------------------------------
# Name:        parse2xml.py
# Purpose:     Creates tags from header of csv file and writes xml
#
# Author:      Linda Ackers
#
# Created:     11/14/2016
#
#-------------------------------------------------------------------------------
import sys, os, time
import xml.etree.cElementTree as ET

def main():

    #openfile for reading
    readfile=open('collegenow.csv', 'r')
    writefile=open('collegenow.xml', 'w')
    while True:        
        theline=readfile.readline()
        if len(theline) == 0:
            break
        print(theline, end="")
        #write to file
        writefile.write(theline)
    readfile.close()
    writefile.close()
    
    #test element tree
    tree=ET.Element.Tree(file='collegenow.xml')
    tree.getroot()
    root = tree.getroot()
    root.tag, root.attrib   
    

if __name__ == '__main__':
    main()