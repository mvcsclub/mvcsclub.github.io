import re, urllib, time
def getChildLinks(link):
    links = [];
    start_time = time.time();
    try:
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(link).read(), re.I):
			links.append(ee)
    except:
        #print "Invalid link type"
        pass
    return links


#really simple python code that prints out all
#links on a given page

#it's your job to turn this into a real web crawler!!!

visited = [];

def dfs(url):
	if url in visited:
		return
	print url;
	visited.append(url);
	links = getChildLinks(url)
	for link in links:
		dfs(link); 


print "URL crawling with dfs:"
myurl = "http://drootr.com/"
#dfs(myurl);



ranks = {};
ranks[myurl] = 50;
d = 0.8

def rankAll(page):
	childlinks = getChildLinks(page);
	print page
	for childPage in childlinks:
		if childPage not in ranks:
			ranks[childPage] = 1-d;
		ranks[childPage] = d*ranks[page]/(len(childlinks));


for i in range(1, 1000)
	rankAll(myurl);



