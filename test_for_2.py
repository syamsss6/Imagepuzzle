def ff(p):
 
 files = set() # holds lines already seen
 outfile = open('33out.txt', "w")
 for line in open('2.txt', "r"):
    if line not in files: # not a duplicate
        outfile.write(line)
        #outfile.writelines(sorted(lines_seen))
        files.add(line)
 outfile.close()

if __name__ == '__main__':
    ff(open('2.txt'))
