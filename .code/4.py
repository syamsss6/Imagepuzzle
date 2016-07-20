#!/usr/bin/python

import requests

#save images to files.
#sorted and duplicates-removed urls
#are obtained from a file

def save_image(url, filename):
    print url
    r = requests.get(url)
    f = open(filename, 'w')
    f.write(r.content)
    f.close()


def main():

    filename = 1
    url_base = 'http://code.google.com'

    #open file 3.txt

    #using a for loop, save each url to a file
    #you can use the save_image function for doing 
    #this.
    #The files to which you are saving the urls should
    #be called 0.jpg, 1.jpg, 2.jpg etc.
    
    for url in open('3.txt'):
        save_image(url_base + url.strip(), "images/" + str(filename) + ".jpg")
        print 'saved file %d' % filename
        filename += 1

main()
