#!/usr/bin/python

def eliminate_duplicates_and_print_sorted(file):
    #remove duplicate lines from `file' and print the sorted lines
    #hint: you can use a set and also the "sorted" function
      element=set()
      ob=open('3.txt','w')
      for line in file:
        element.add(line)
      p=sorted(element)
      for i in p:
        ob.write(i)
      ob.close()  
if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('2.txt'))
    
