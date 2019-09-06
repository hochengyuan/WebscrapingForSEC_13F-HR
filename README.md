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
<br>&nbsp;&nbsp; - Sample of the output for CIK: 0001166559
<image src="./screenshot/output_sample.png">

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
		<td>Parse the input CIK/Ticker, and propel the web scraping for each CIK/Ticker.</td>
	</tr>
	<tr>
		<td>collecturl.py</td>
		<td>Go to the search result page of CIK/Ticker 13F-HR report on SEC Search EDGAR. Then, retrieve the url of the latest document page.</td>
	</tr>
	<tr>
		<td>collectxml.py</td>
		<td>Go to the lastest document page of CIK/Ticker 13F-HR report. Then, retrieve the url of the xml file(information table of 13F-HR).</td>
	</tr>
	<tr>
		<td>parsexml.py</td>
		<td>Parse the information table of xml file. Then save the parsed Pandas dataframe to .tsv file in directory "./output". The parsing is based on the <a href="https://www.sec.gov/pdf/form13f.pdf">13F-HR Form of SEC</a>.</td>
	</tr>
</table>

## ii. API Flow


## iii. Function Description for each API
<br><b>1. manager.py</b>
<table border='1'>
	<tr><th>Function Name</th><th>Return Type</th><th>Input Parameter</th><th>Description</th></tr>
	<tr>
		<td>execute()</td>
		<td>void</td>
		<td>void</td>
		<td>Propel the web scraping for each input CIK/Ticker.</td>
	</tr>
</table>

<br><b>2. collecturl.py</b>
<table border='1'>
	<tr><th>Function Name</th><th>Return Type</th><th>Input Parameter</th><th>Description</th></tr>
	<tr>
		<td>run()</td>
		<td>void</td>
		<td>void</td>
		<td>Go through all process for collecting the url of the document page.</td>
	</tr>
	<tr>
		<td>__connect()</td>
		<td>void</td>
		<td>void</td>
		<td>If the status code for the HTTP GET Request is 200, retrieve source html text. Otherwise, terminate the application.</td>
	</tr>
	<tr>
		<td>__implement_GET_Request()</td>
		<td>void</td>
		<td>void</td>
		<td>Implement HTTP GET Request of the Search Result Page.</td>
	</tr>
	<tr>
		<td>__generate_url()</td>
		<td>void</td>
		<td>void</td>
		<td>Generate the url of the search result of the Search Rsult Page for the input Ticker/CIK.</td>
	</tr>
	<tr>
		<td>__checkPageFound()</td>
		<td>void</td>
		<td>void</td>
		<td>If the words "No matching Ticker Symbol" show on the search result page, terminate the whole application.</td>
	</tr>
	<tr>
		<td>__collect_report_link()</td>
		<td>void</td>
		<td>void</td>
		<td>Collect the url of documentation page. If there is no documentation page link shown on the Search Result Page, terminate the whole application.</td>
	</tr>
	<tr>
		<td>get_report_url()</td>
		<td>string</td>
		<td>void</td>
		<td>Get the collected url of the lastest documentation page.</td>
	</tr>
	<tr>
		<td>get_html()</td>
		<td>string</td>
		<td>void</td>
		<td>Get the source html of the Search Result Page</td>
	</tr>
</table>

<br><b>3. collectxml.py</b>
<table border="1">
	<tr><th>Function Name</th><th>Return Type</th><th>Input Parameter</th><th>Description</th></tr>
	<tr>
		<td>run()</td>
		<td>void</td>
		<td>void</td>
		<td>Go through all process for collecting the url of xml file for the lastest 13F-HR.</td>
	</tr>
	<tr>
		<td>__bridge_url()</td>
		<td>string</td>
		<td>void</td>
		<td>Bridge the parsed result (url) of Search Result Page through "collecturl.py".</td>
	</tr>
	<tr>
		<td>__collect_xml_url(url)</td>
		<td>string</td>
		<td>url (string)</td>
		<td>Connect the url of Documentation Page and retreive the xml url of 13F-HR.</td>
	</tr>
	<tr>
		<td>__select_xml_url(src_html)</td>
		<td>string</td>
		<td>html (string)</td>
		<td>Parse the xml url of 13F-HR from input html.</td>
	</tr>
	<tr>
		<td>__implement_GET_Request(url)</td>
		<td>string / None (when failed)</td>
		<td>url (string)</td>
		<td>Implement HTTP GET Request of the Documentation Page and retrieve the html text.</td>
	</tr>
	<tr>
		<td>get_xml_url()</td>
		<td>void</td>
		<td>xml_url (string)</td>
		<td>Return the parsed url of the xml.</td>
	</tr>
	<tr>
		<td>get_fail_landing_url</td>
		<td>void</td>
		<td>url (string)</td>
		<td>Return the failed url of Documentation Page. This function is for debugging.</td>
	</tr>
</table>

<br><b>4. parsexml.py</b>
<table border="1">
	<tr><th>Function Name</th><th>Return Type</th><th>Input Parameter</th><th>Description</th></tr>
	<tr>
		<td>run()</td>
		<td>void</td>
		<td>void</td>
		<td>Go through the whole process, including parsing input xml and save parsed result to .tsv file</td>
	</tr>
	<tr>
		<td>__bridge_xml_url()</td>
		<td>void</td>
		<td>url (string)</td>
		<td>Bridge the parsed result (url of xml) of Documentation Page through "collectxml.py"</td>
	</tr>
	<tr>
		<td>__implement_GET_Request(url)</td>
		<td>string / None (when failed)</td>
		<td>url (string)</td>
		<td>Implement HTTP GET Request of the xml url and retrieve the xml text.</td>
	</tr>
	<tr>
		<td>__parse_single_xml_to_df(src_xml)</td>
		<td>Pandas.DataFrame</td>
		<td>xml (string)</td>
		<td>Parsed the input xml text to Pandas Dataframe.</td>
	</tr>
	<tr>
		<td>__write_df_to_tsv()</td>
		<td>void</td>
		<td>void</td>
		<td>Save the parsed dataframe to .tsv file under "./output" directory.</td>
	</tr>
	<tr>
		<td>print_df()</td>
		<td>void</td>
		<td>void</td>
		<td>Print out parsed xml in Pandas DataFrame type. This function is for supporting and debugging.</td>
	</tr>
</table>

## iv. Corner Cases
<br><b>1. Exception and Errors</b>
<br><b>2. Limitations</b>