import re, urllib
def getChildLinks(link):
    links = [];
    try:
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(link).read(), re.I):
            links.append(ee);
    except:
        print "Invalid link type"
        pass
    return links


#really simple python code that prints out all
#links on a given page

#it's your job to turn this into a real web crawler!

print "URL crawling:"
myurl = "http://drootr.com/"
for i in getChildLinks(myurl):
    print i


