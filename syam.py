
print '<html>'
print ' <head><title>Images</title></head>'
print '<body>'
      

#You need to print lines of the form
#<img src="1.jpg">
#<img src="2.jpg">
#and so on. Think of using a for-loop to do this
for i in range(0,20):
 print '<img src="'+str(i)+'.jpg">'

print '</body></html>'
