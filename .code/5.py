#!/usr/bin/python

#Generate an html page with images
#number 0 to 20, in order


print """<html>
         <head><title>Images</title></head>
         <body>
      """

for i in range(0,21):
    print '<img src="%s">' % (str(i) + ".jpg")


print """</body></html>"""
