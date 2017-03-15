s = "city"
print s[3:]
print 'city'.find('y')


##########################################################################

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
first_quote = page.find('"', start_link) + 1
second_quote = page.find('"', first_quote)
url = page[first_quote : second_quote]
print url

##########################################################################

print "x = " + url[0:] # Will print the entire string

##########################################################################