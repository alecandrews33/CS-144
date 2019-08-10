from fetcher3 import *
import networkx as nx
import time
import json

def create_graph(page_limit, start_URL):
	hyperlinks = {}
	hyperlinks_to = {}
	curr_URL = start_URL
	links = []
	num_pages = 0
	while num_pages < page_limit:
		time.sleep(3)
		new_links = fetch_links(curr_URL)
		if new_links == None:
			new_links = []
		links.extend(new_links)
		hyperlinks[curr_URL] = new_links
		for url in new_links:
			if url in hyperlinks_to:
				hyperlinks_to[url].append(curr_URL)
			else:
				hyperlinks_to[url] = [curr_URL]
		
		while True:
			curr_URL = links.pop(0)
			if curr_URL[-1] = '/':
				curr_URL = curr_URL[:-1]
			if '?' not in curr_URL and "caltech.edu" in curr_URL \
				and curr_URL not in hyperlinks:	
				break
		num_pages += 1

		print(str(num_pages) + ' - ' + str(len(hyperlinks)))
	return hyperlinks, hyperlinks_to


def dictionary_write(dict, file):
	with open(file, 'w') as f:
		json.dump(dict, f)


if __name__ == "__main__":
	links_dict, links_to_dict = create_graph(2000, "http://www.caltech.edu")
	dictionary_write(links_dict, "hyperlinks.txt")
	dictionary_write(links_to_dict, "hyperlinks_to.txt")
		
