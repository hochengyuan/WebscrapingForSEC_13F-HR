import requests
from bs4 import BeautifulSoup
import sys

class CollectURL:
	def __init__(self , input_string):
		# Initialization
		self.__input_string = input_string
		self.__url = None
		self.__response = None
		self.__src_html = None 

		# Collect Link
		self.__report_url = None


	def run(self):
		self.__connect()
		self.__checkPageFound()
		self.__collect_report_link()
		print("Collected the current 13F-HR report page of %s" % self.__input_string)



	def __collect_report_link(self):
		bs = BeautifulSoup(self.get_html() , "lxml")
		table = bs.find("table" , {"class":"tableFile2"})
		all_tr = table.find_all('tr')

		if len(all_tr) < 2: # Only Header, so no 13F-HR
			print("ticker/CIK %s does not have 13F-HR" % self.__input_string)
			sys.exit(1)
		
		first_row = all_tr[1]
		self.__report_url = "https://www.sec.gov" + first_row.find_all('td')[1].find('a').get('href')


	def __connect(self):
		self.__implement_GET_Request()

		if self.__response.status_code == 200:
			self.__src_html = self.__response.text

		else:
			print("Failed: Status Code = " , self.__response.status_code)
			print("Failed URL:\n" , self.__url)
			print("Application Terminated")
			sys.exit(1)

	
	def __implement_GET_Request(self):
		self.__generate_url()
		self.__response = requests.get(self.__url)


	def __checkPageFound(self):
		if "No matching Ticker Symbol" in self.get_html():
			print("No matching CIK/Ticker: %s" % self.__input_string)
			print("Application Failed")
			sys.exit(1)


	def __generate_url(self):
		self.__url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=13F-HR&dateb=&owner=exclude" %\
		           (self.__input_string)
		


	# Supporting Function
	def get_report_url(self):
		print("url for 13F-HR report page: %s" % self.__report_url)
		return self.__report_url

	def get_html(self):
		return self.__src_html