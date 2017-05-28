import urllib.request as urlRequest

output = "files/"

OTBookDetails = [
	{"name": "Genesis", "chapters": 50, "abbreviation": "Gen"},
	{"name": "Exodus", "chapters": 40, "abbreviation": "Exod"},
	{"name": "Leviticus", "chapters": 27, "abbreviation": "Lev"},
	{"name": "Numbers", "chapters": 36, "abbreviation": "Num"},
	{"name": "Deuteronomy", "chapters": 34, "abbreviation": "Deut"},
	{"name": "Joshua", "chapters": 24, "abbreviation": "Josh"},
	{"name": "Judges", "chapters": 21, "abbreviation": "Judg"},
	{"name": "Ruth", "chapters": 4, "abbreviation": "Ruth"},
	{"name": "1 Samuel", "chapters": 31, "abbreviation": "1 Sam"},
	{"name": "2 Samuel", "chapters": 24, "abbreviation": "2 Sam"},
	{"name": "1 Kings", "chapters": 22, "abbreviation": "1 Kgs"},
	{"name": "2 Kings", "chapters": 25, "abbreviation": "2 Kgs"},
	{"name": "1 Chronicles", "chapters": 29, "abbreviation": "1 Chr"},
	{"name": "2 Chronicles", "chapters": 36, "abbreviation": "2 Chr"},
	{"name": "Ezra", "chapters": 10, "abbreviation": "Ezra"},
	{"name": "Nehemiah", "chapters": 13, "abbreviation": "Neh"},
	{"name": "Esther", "chapters": 10, "abbreviation": "Est"},
	{"name": "Job", "chapters": 42, "abbreviation": "Job"},
	{"name": "Psalms", "chapters": 150, "abbreviation": "Ps"},
	{"name": "Proverbs", "chapters": 31, "abbreviation": "Prov"},
	{"name": "Ecclesiastes", "chapters": 12, "abbreviation": "Eccl"},
	{"name": "Song of songs", "chapters": 8, "abbreviation": "Songs"},
	{"name": "Isaiah", "chapters": 66, "abbreviation": "Isa"},
	{"name": "Jeremiah", "chapters": 52, "abbreviation": "Jer"},
	{"name": "Lamentations", "chapters": 5, "abbreviation": "Lam"},
	{"name": "Ezekiel", "chapters": 48, "abbreviation": "Ezek"},
	{"name": "Daniel", "chapters": 12, "abbreviation": "Dan"},
	{"name": "Hosea", "chapters": 14, "abbreviation": "Hos"},
	{"name": "Joel", "chapters": 4, "abbreviation": "Joel"},
	{"name": "Amos", "chapters": 9, "abbreviation": "Amos"},
	{"name": "Obadiah", "chapters": 1, "abbreviation": "Obad"},
	{"name": "Jonah", "chapters": 4, "abbreviation": "Jonah"},
	{"name": "Micah", "chapters": 7, "abbreviation": "Mic"},
	{"name": "Nahum", "chapters": 3, "abbreviation": "Nah"},
	{"name": "Habakkuk", "chapters": 3, "abbreviation": "Hab"},
	{"name": "Zephaniah", "chapters": 3, "abbreviation": "Zeph"},
	{"name": "Haggai", "chapters": 2, "abbreviation": "Hag"},
	{"name": "Zechariah", "chapters": 14, "abbreviation": "Zech"},
	{"name": "Malachi", "chapters": 3, "abbreviation": "Mal"}
]

url = "http://qbible.tk/api/book_chapter"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}


print("Processing...")
for book in OTBookDetails:
	print(book["name"])
	for chapter in range(1, book["chapters"] + 1):
		query = '{{"reference":{{ "book":"{book}","chapter":{chapter} }},"display_by":"verse"}}'.format(book=book["name"], chapter=chapter).encode('utf-8')
		targetUrl = urlRequest.Request(url = url, data=query)
		x = urlRequest.urlopen(targetUrl)
		filename = book["abbreviation"].replace(" ", "_") + str(chapter) + ".json"
		with open(output + filename, 'w') as f:
			f.write(x.read().decode('utf-8'))

print("\nDone")