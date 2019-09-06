from parsexml import ParseXML
import os

class Manager:
	def __init__(self , line):
		self.cik_container = line

	def execute(self):
		# Make Directory
		parent_dir = os.path.abspath("..")
		output_dir = parent_dir + "/output/"
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)

		for cik in self.cik_container:
			parsexml = ParseXML(cik)
			parsexml.run()
			print("--")