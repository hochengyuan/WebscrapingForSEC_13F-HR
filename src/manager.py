from parsexml import ParseXML
import os

class Manager:
	def __init__(self , line):
		self.cik_container = line

	def execute(self):
		# Make Directory
		if not os.path.exists("output"):
			os.makedirs("output")

		for cik in self.cik_container:
			parsexml = ParseXML(cik)
			parsexml.run()
			print("--")