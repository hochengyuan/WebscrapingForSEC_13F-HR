from bs4 import BeautifulSoup
import requests
from collecturl import CollectURL
import sys

class CollectXML:
	def __init__(self , input_url):
		# Initialization
		self.__url = input_url
		self.__xml_url = None

		# Processing
		self.__fail_landing_url = None


	def run(self):
		src_html = self.__implement_GET_Request(self.__url)
		xml_url = self.__select_xml_url(src_html)
		self.__xml_url = xml_url


	def __select_xml_url(self , src_html):
		if src_html is None:
			print("the report page does not exist %s" % self.get_fail_landing_url())
			print("Application Terminated")
			sys.exit(1)

		url = None
		bs = BeautifulSoup(src_html , "lxml")
		table = bs.find("table" , {"class":"tableFile"})
		all_tr = table.find_all("tr")
		for tr in all_tr:
			all_td = tr.find_all("td")
			all_td_text = [td.get_text().lower() for td in all_td]
			if all_td_text and ".xml" in all_td_text[2] and "information table" in all_td_text[3]:
				url = "https://www.sec.gov" + all_td[2].find('a').get('href')

		return url



	# Supporting Function
	def get_xml_url(self):
		print("url for 13F-HR xml page: %s" % self.__xml_url)
		return self.__xml_url

	def get_fail_landing_url(self):
		return self.__fail_landing_url


	def __implement_GET_Request(self , url):
		try_time = 1
		while try_time < 3:
			response = requests.get(url)
			if response.status_code == 200:
				return response.text
			else:
				try_time += 1
		
		if try_time == 3:
			self.__fail_landing_url = url
			print("Could not implement GET Request on xml: %s ; Status Code: %s" % \
				(self.get_fail_landing_url() , response.status_code))
			print("Application Terminated")
			sys.exit(1)

		return None

