from bs4 import BeautifulSoup
import csv
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

page = requests.get("https://zach-adams.com/2014/05/music-to-listen-to-while-coding/")
soup = BeautifulSoup(page.content,'html.parser')
songs = soup.find('div',class_="entry-content")

csv_file = open('CodeSongs.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['S.No','Song Name', 'Link'])

count = 0
for item in songs.find_all('ul'):
	for item1 in item.find_all('li'):
		a = item1.find('a')
		b = a['href']
		#print a.get_text(),b
		count+=1
		#print count
		csv_writer.writerow([count,a.get_text(), b])

page = requests.get("https://zach-adams.com/2015/01/music-listen-coding-part-2/")
soup = BeautifulSoup(page.content,'html.parser')
songs = soup.find('div',class_="entry-content")
flag = True

for item in songs.find_all('ul'):

		for item1 in item.find_all('li'):
			a = item1.find('a')
			b = a['href']
			#print a.get_text(),b
			count+=1
			#print count
			csv_writer.writerow([count,a.get_text(), b])
	
csv_file.close()