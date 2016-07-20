#!/usr/bin/python

def eliminate_duplicates_and_sort(file):
    #remove duplicate lines from `file'
    r = sorted(set(file))
    for line in r:
        print line,

if __name__ == '__main__':
    eliminate_duplicates_and_sort(open('2.txt'))
    
