# Web Scraping for the Latest 13F-HR Report on SEC of the U.S.A. Search EDGAR

# I. Introduction
This Python Application 

# II. Instruction
## i. Enviroment
<br> Python Version 3.x
## ii. Dependency
<br> 1. requests==2.18.4
<br> 2. pandas==0.20.3
<br> 3. beautifulsoup4==4.8.0
## iii. Process
<br> 1. Open Terminal
<br> 2. Go into directory: "./src/"
<br> 3. Command Line: python3 main.py
<br> 4. Follow the instruction on the terminal screen
<image src="./screenshot/command_line.png">
<br> 5. Output Directory: "./output/"

# III. Documentation
## i. API Profile
<table border='1'>
	<tr><th>API Name</th><th>Description</th></tr>
	<tr>
		<td>main.py</td>
		<td>The main program to run the web scraping application.</td>
	</tr>
	<tr>
		<td>manager.py</td>
		<td>Parse the input CIK/Ticker, and propel the web scraping for each CIK/Ticker</td>
	</tr>
	<tr>
		<td>collecturl.py</td>
		<td>Go to the search result page of CIK/Ticker 13F-HR report on SEC Search EDGAR. Then, retrieve the url of the latest document page</td>
	</tr>
	<tr>
		<td>collectxml.py</td>
		<td>Go to the lastest document page of CIK/Ticker 13F-HR report. Then, retrieve the url of the xml file(information table of 13F-HR)</td>
	</tr>
	<tr>
		<td>parsexml.py</td>
		<td>Parse the information table of xml file. Then save the parsed Pandas dataframe to .tsv file</td>
	</tr>
</table>>
## ii.