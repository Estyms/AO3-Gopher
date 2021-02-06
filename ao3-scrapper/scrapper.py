from bs4 import BeautifulSoup
import requests
from urllib.parse import parse_qs, urlparse


class workSearchURL:
	entry_dict = {
		"commit" 				: "Search",
		"query" 				: "",
		"title" 				: "",
		"creators" 				: "",
		"revised_at" 			: "",
		"categories_id"			: "",
		"complete" 				: "",
		"crossover" 			: "",
		"single_chapter"		: "",
		"word_count" 			: "",
		"language_id"			: "",
		"fandom_names"			: "",
		"rating_ids"			: "",
		"character_names"		: "",
		"relationship_names"	: "",
		"freeform_names"		: "",
		"hits" 					: "",
		"kudos_count"			: "",
		"comments_count"		: "",
		"bookmarks_count"		: "",
		"sort_column"			: "",
		"sort_direction"		: "",
	}

def search(url):
	req = parse_qs(urlparse(url).query)
	print(req)
	return ""


if __name__ == "__main__":
	search("""
https://archiveofourown.org/works/search?utf8=%E2%9C%93&commit=Search&work_search%5Bquery%5D=e&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcategory_ids%5D%5B%5D=22&work_search%5Bcategory_ids%5D%5B%5D=21&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc
	""")