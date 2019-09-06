from collecturl import CollectURL
from collectxml import CollectXML
from parsexml import ParseXML
import pandas as pd
import csv
import os

class Manager:
	def __init__(self , line):
		self.cik_container = line
		self.__parent_dir = os.path.abspath("..")

	def execute(self):
		# Make Directory
		parent_dir = os.path.abspath("..")
		output_dir = parent_dir + "/output/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)

		for cik in self.cik_container:
			url = self.__run_collecturl(cik)
			print("Collected the current 13F-HR report page of %s" % cik)
			xml_url = self.__run_collectxml(url)
			print("Collected the XML url of the current 13F-HR for %s" % cik)
			df = self.__run_parsexml(xml_url)
			print("Parsed XML file of Ticker/CIK 13F-HR: %s" % cik)
			self.__write_df_to_tsv(df , cik)
			print("Written the parsed XML file to path of \"../output/%s.tsv\"" % cik)
			print("--")


	def __run_collecturl(self , cik):
		# Collect the Document Page URL from Search Result Page
		collecturl = CollectURL(cik)
		collecturl.run()
		return collecturl.get_report_url()


	def __run_collectxml(self , url):
		# Collect the XML URL from Document Page
		collectxml = CollectXML(url)
		collectxml.run()
		return collectxml.get_xml_url()


	def __run_parsexml(self , xml_url):
		# Parse the XML URL to Pandas DataFrame
		parsexml = ParseXML(xml_url)
		parsexml.run()
		return parsexml.get_parsed_xml_df()


	def __write_df_to_tsv(self , dataframe , cik):
		path = "%s/output/%s.tsv" % (self.__parent_dir , cik)
		header = ["COLUMN 1: Name of Issuer" , "COLUMN 2: Title of Class" , "COLUMN 3: CUSIP Number" , "COLUMN 4: Market Value" ,\
		          "COLUMN 5: Amount and Type of Security" , " " , " " , \
		          "COLUMN 6: Investment Discretion" , "COLUMN 7: Other Managers" , "COLUMN 8: Voting Authority" , " " , " "]
		with open(path , 'w' , newline='') as tsvfile:
			writer = csv.writer(tsvfile , delimiter='\t')
			writer.writerow(header)

		dataframe.to_csv(path , sep='\t' , mode='a' , index=False)