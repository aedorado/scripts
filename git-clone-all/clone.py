import json
from URL import *
from Git import *

url = URL('https://api.github.com/users/aedorado/repos?per_page=1000')
all_repos = json.loads(url.fetch())

# print urllib2.urlopen('http://www.google.com').read(
for repo in all_repos:
	# print repo['html_url']
	Git.clone(repo['html_url'])
