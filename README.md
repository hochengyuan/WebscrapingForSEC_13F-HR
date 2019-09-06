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
</table>

## ii. API Flow


## iii. Function Description for each API
<b>1. manager.py</b>
<table border='1'>
	<tr><th>Function Name</th><th>Return</th><th>Description</th></tr>
	<tr>
		<td>execute()</td>
		<td>void</td>
		<td>Propel the web scraping for each input CIK/Ticker.</td>
	</tr>
</table>

<b>2. collecturl.py</b>
<table border='1'>
	<tr><th>Function Name</th><th>Return</th><th>Description</th></tr>
	<tr>
		<td>run()</td>
		<td>void</td>
		<td>Go through all process for collecting the url of the document page.</td>
	</tr>
	<tr>
		<td>__connect()</td>
		<td>void</td>
		<td>If the status code for the HTTP GET Request is 200, retrieve source html text. Otherwise, terminate the application.</td>
	</tr>
	<tr>
		<td>__implement_GET_Request()</td>
		<td>void</td>
		<td>Implement HTTP GET Request of the Search Result Page.</td>
	</tr>
	<tr>
		<td>__generate_url()</td>
		<td>void</td>
		<td>Generate the url of the search result of the Search Rsult Page for the input Ticker/CIK.</td>
	</tr>
	<tr>
		<td>__checkPageFound()</td>
		<td>void</td>
		<td>If the words "No matching Ticker Symbol" show on the search result page, terminate the whole application.</td>
	</tr>
	<tr>
		<td>__collect_report_link()</td>
		<td>void</td>
		<td>Collect the url of documentation page. If there is no documentation page link shown on the Search Result Page, terminate the whole application.</td>
	</tr>
	<tr>
		<td>get_report_url()</td>
		<td>string</td>
		<td>Get the collected url of the lastest documentation page.</td>
	</tr>
	<tr>
		<td>get_html()</td>
		<td>string</td>
		<td>Get the source html of the Search Result Page</td>
	</tr>
</table>