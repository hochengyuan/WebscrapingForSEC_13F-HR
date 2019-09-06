from collectxml import CollectXML
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

class ParseXML:
	def __init__(self , input_string):
		self.__cik = input_string

		# Processing
		self.__fail_xml_url = None
		self.columns = ["nameOfIssuer" , "titleOfClass" , "cusip" , "value" , "sshPrnamt" , "sshPrnamtType" , "putCall" , \
           "investmentDiscretion" , "otherManager" , "Sole" , "Shared" , "None"]
		self.df = pd.DataFrame(columns=self.columns)


	def run(self):
		url = self.__bridge_xml_url()
		src_xml = self.__implement_GET_Request(url)
		self.__parse_single_xml_to_df(src_xml)
		self.__write_df_to_tsv()
		print("Written the parsed XML file to path of \"./output/%s.tsv\"" % self.__cik)


	def __parse_single_xml_to_df(self , src_xml):
		if src_xml is None:
			print("the xml url does not work. url: %s" % self.__fail_xml_url)
			print("Application Terminated")
			sys.exit(1)

		bs = BeautifulSoup(src_xml , "xml")
		outer_infotable = bs.find("informationTable")
		all_infotable = outer_infotable.find_all("infoTable")
		
		for infotable in all_infotable:
			cur_row = []
			for tag in self.columns:
				temp = ""
				if infotable.find(tag) is not None:
					temp = infotable.find(tag).get_text()
				cur_row.append(temp)
			self.df = self.df.append(pd.Series(cur_row , index=self.columns).astype(str) , ignore_index=True)

		self.df.rename(columns={"value" : "value (x$1000)"} , inplace=True)
		return self.df

	def __write_df_to_tsv(self):
		path = "./output/" + self.__cik + ".tsv"
		header = ["COLUMN 1: Name of Issuer" , "COLUMN 2: Title of Class" , "COLUMN 3: CUSIP Number" , "COLUMN 4: Market Value" ,\
		          "COLUMN 5: Amount and Type of Security" , " " , " " , \
		          "COLUMN 6: Investment Discretion" , "COLUMN 7: Other Managers" , "COLUMN 8: Voting Authority" , " " , " "]
		with open(path , 'w' , newline='') as tsvfile:
			writer = csv.writer(tsvfile , delimiter='\t')
			writer.writerow(header)

		self.df.to_csv(path , sep='\t' , mode='a' , index=False)


	# Supporting Functions
	def print_df(self):
		print(self.df)

	def __bridge_xml_url(self):
		collectxml = CollectXML(self.__cik)
		collectxml.run()
		return collectxml.get_xml_url()

	def __implement_GET_Request(self , url):
		try_time = 1
		while try_time < 3:
			response = requests.get(url)
			if response.status_code == 200:
				return response.text
			else:
				try_time += 1

		if try_time == 3:
			self.__fail_xml_url = url
			print("Could not implement GET Request on xml: %s ; Status Code: %s" % \
				(self.__fail_xml_url , response.status_code))
			print("Application Terminated")
			sys.exit(1)

		return None