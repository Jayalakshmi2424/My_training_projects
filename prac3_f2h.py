#Scrape the website "Freshtohome" using selenium and xpath
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.freshtohome.com/" 
driver = webdriver.Chrome(executable_path=#path to chromedriver)
driver.get(url) #freshtohome url as input to the driver
#all locations in a dictionary
tdict={'Bangalore':1,'Delhi&NCR&Jaipur':3,'Hyderabad':14,'Mumbai':11,'Pune':12,'Kerala':2,'TamilNadu':7}
#scrapping using xpath
for loc in tdict.keys() :
	if(tdict[loc]==1):
		driver.find_element_by_id(tdict[loc]).send_keys(Keys.ENTER)
	if(tdict[loc]!=1):
		url = "https://www.freshtohome.com/" 
		driver = webdriver.Chrome(executable_path=#path to chromedriver)
		driver.get(url)
		driver.find_element_by_id(tdict[loc]).send_keys(Keys.ENTER)
		
	driver.find_element_by_link_text("All Products").send_keys(Keys.ENTER)

	item = driver.find_elements_by_xpath('//h3[@class="product-name"]')
	price = driver.find_elements_by_xpath('//span[@class="fexp0"]/span[@class="price"]')
	qty = driver.find_elements_by_xpath('//span[@class="label-price fexp0"]')
	img = driver.find_elements_by_xpath("//img[@class='lazy']")

	for itr in range(0,31) :
		with open(f'f2home-{loc}.txt', 'a+') as f: 
			appendEOL = False
			f.seek(0)
			data = f.read(100)
			if len(data)>0:
				appendEOL = True
			for i,j,k,l in zip(item,price,qty,img):
				if appendEOL == True:
					f.write("\n")			
				f.write(i.text+"; ")
				f.write(j.text+";")	
				f.write(k.text+";")	
				f.write('"'+l.get_attribute("data-src")+'"')
				if appendEOL==False:
					f.write("\n")
		  
		f.close()
		try:
			driver.find_element_by_xpath("//a[@class='next i-next fa fa-caret-right']").send_keys(Keys.ENTER)
			
			item=driver.find_elements_by_xpath('//h3[@class="product-name"]')
			price=driver.find_elements_by_xpath('//span[@class="fexp0"]/span[@class="price"]')
			qty = driver.find_elements_by_xpath('//span[@class="label-price fexp0"]')
			img = driver.find_elements_by_xpath("//img[@class='lazy']")
		except:
			for k in range(0,itr) :
				driver.back()
			break
	driver.back()
	df = pd.read_csv(f'f2home-{loc}.txt',delimiter=';')
	df.columns = ['Item Name', 'Price', 'Quantity','Image link'] 
	df.to_csv(f'f2home-{loc}.csv')
	driver.close()
