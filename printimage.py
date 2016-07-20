#!/usr/bin/python

import requests,urllib

def print_urls(file):

   ptr=open('2.txt','w')
   for i in file:
    val=i.split(' ')
    ptr.write(val[1])
   ptr.close()

def eliminate_duplicates_and_print_sorted(file):
      element=set()
      ob=open('3.txt','w')
      for line in file:
        element.add(line)
      p=sorted(element)
      for i in p:
        ob.write(i)
      ob.close()

def save_image(url, filename):
     urllib.urlretrieve(url,filename)

def main():

    filename = 1
    url_base = 'http://code.google.com'
    for url in open('3.txt'):
      save_image(url_base+url,str(filename)+'.jpg')
      filename=filename+1


def htm():
 print '<html>'
 print ' <head><title>Images</title></head>'
 print '<body>'
 for i in range(0,20):
  print '<img src="'+str(i)+'.jpg">'
 print '</body></html>'


f = open('1.txt')
print_urls(f)
f.close()

if __name__ == '__main__':
    eliminate_duplicates_and_print_sorted(open('2.txt'))

r = requests.get('http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg')
f1 = open('img0.jpg', 'w')
f1.write(r.content)
f1.close()

main()

htm()

