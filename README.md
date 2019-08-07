# Link Analyzer

## Contents
 - [Current Features](#linkAnalyzer-can-currently)
 - [Requirements](#requirements)
 - [How to Use](#how-to-use-script)

## linkAnalyzer can Currently:

  - Unshorten URL's that have been shortened by external services.
  - Perform reputation checks from:
    - [VirusTotal](https://www.virustotal.com)
    - [URLscan](https://www.urlscan.io/)
  - Get links and compare them against [VirusTotal](https://www.virustotal.com) (see requirements)
  - Get links and compare them against [URLscan](https://www.urlscan.io/) to see screenshot of page.   

## Requirements
 - [Python 3.x](https://www.python.org/)
 - Install all dependencies from the requirements.txt file. `pip install -r requirements.txt`
### You need to complete the following steps to have the script run properly.  
It is important to not expose your API Keys!  
To handle this concern, I have hidden the 'config.py' from future git commits.
#### Create a file named 'config.py' on the root directory of this repo and add the following (replace 'API-KEY' with your keys):  

```
urlScanAPIKey = 'API-KEY'
vtAPIKey = 'API-KEY' 
```

## How to use script
The main script file is linkAnalyzer.py  
To run the script,  
Open CMD, PowerShell or terminal and enter :  

```
python linkAnalyzer.py
```
