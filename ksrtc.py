from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Firefox()						#load the webpage
driver.get("https://www.ksrtc.in/")

q1 = driver.find_element_by_id("fromPlaceName")		#send from place
q1.send_keys("MANGALORE")
time.sleep(3)
driver.find_element_by_css_selector("#ui-id-4").click()

q2 = driver.find_element_by_id("toPlaceName")		#send to place
q2.send_keys("BANGALO")
time.sleep(3)
q2.send_keys(Keys.ENTER)

elem = driver.find_element_by_id("txtJourneyDate")
elem.click()
elem2 = driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr[2]/td[4]")
elem2.click()
time.sleep(3)										#select a date of journey

driver.find_element_by_id("searchBtn").click()		#click search
time.sleep(5)

result = driver.page_source

soup = BeautifulSoup(result,'html.parser')
#print soup.prettify()

csv_file = open('ksrtc.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Service Name', 'Departure Time', 'Arrival Time','Bus Type','Available Seats','Ticket Rate'])

print "Service Name | Departure Time | Arrival Time | Bus Type | Available Seats | Ticket Rate"
for item in soup.findAll('div',class_="rSetForward"):
	a = item.find('div',class_="col1")
	b = item.find('div',class_="col2")
	b1 = b.find('span',class_="StrtTm")
	b2 = b.find('span',class_="ArvTm`")
	c = item.find('div',class_="col3")
	c1 = c.find('div',class_="bustype")
	d = item.find('div',class_="col4")
	d1 = d.find('span',class_="availCs")
	e = item.find('div',class_="col5")
	e1 = e.find('span',class_="TickRate")

	first = a.get_text()
	second = b1.get_text()
	third = b2.get_text()
	fourth = c1.get_text()
	fifth = d1.get_text()
	sixth = e1.get_text()
	csv_writer.writerow([first,second,third,fourth,fifth,sixth]) 
	
	print a.get_text()+b1.get_text()+b2.get_text()
	print c1.get_text()
	print d1.get_text()
	print e1.get_text()
	print "\n"

driver.close()
csv_file.close()

