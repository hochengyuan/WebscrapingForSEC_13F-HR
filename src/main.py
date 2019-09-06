from manager import Manager
import sys

if __name__ == '__main__':
	print("!!Web Scraping for Holding Report!!")
	print("Input the CIK or Ticker you would like to pull down. Press Enter after each one. Input Empty String to end input session\n")
	
	line = []
	while True:
		cik = input("Input CIK/ticker: ")
		if cik is None or cik == '' or cik.isspace():
			break
		line.append(cik)

	print()
	print("Start Web Scraping the above %s CIK/ticker" % len(line))
	print('--')
	manager = Manager(line)
	manager.execute()
	print()
	print("FINISH ALL WEB SCRAPING")