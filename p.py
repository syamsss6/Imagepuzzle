'''
file 1.py
-----------------------
def mn(f):
# line=f.readline()
 #while line:
    #print line
  #  p=line.split()
   # return p[1]
#    line = f.readline()
  pt=open('2.txt','w')
  for i in f:
   p=i.split(' ')
   pt.write(p[1])
  pt.close()

f=open('1.txt')
print mn(f)
f.close() 

2.py
--------------------
def eliminate_duplicates_and_print_sorted(file):
        element = set()
        outfile = open('33out.txt', "w")
        for line in file:
          #s = sorted(s)
          #outfile.write(s)
          element.add(line)
        p=sorted(element)
        #outfile = open('33out.txt', "w")
        for i in p:
         outfile.write(i)
        outfile.close()


if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('2.txt'))

3.py
----------------



'''

