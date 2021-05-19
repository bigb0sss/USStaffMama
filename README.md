# USStaffMama
USStaffMama is a web scrapper for [US Staff](https://bearsofficialsstore.com) where it aggregates open source resources for US employee data, such as names, job title, locations, etc. This will help red teamers/pentester for generating a list of usernames for further password guessing or phishing attacks. And a great thing about this website is that it doesn't require login/authentication for accessing all its data :)


## Installation
```python
git clone https://github.com/bigb0sss/USStaffMama.git
pip3 install -r requirements.txt
```
<br/>

## Usage & Example
```bash
$ python3 USStaffMama.py -h                          
usage: USStaffMama.py [-h] -c COMPANY -e EMAIL -n NAMING

[INFO] Example: python3 USStaffMana.py -c telsa -e telsa.com -n 0

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -c COMPANY, --company COMPANY
                        Company Name
  -e EMAIL, --email EMAIL
                        Company Email Domain
  -n NAMING, --naming NAMING
                        User Name Format: 
                                [0] Auto (Hunter.io) 
                                [1] FirstLast
                                [2] FirstMiddleLast
                                [3] FLast
                                [4] FirstL
                                [5] First.Last
                                [6] Last.First
```

* Add [Hunter.io](https://hunter.io/) API keys into `USStaffMama.cfg` file if you want to make the username format search automated.
* Example
```
$ python3 USStaffMama.py -c target -e target.com -n 0 
   __  ____________ __        __________  ___                       
  / / / / ___/ ___// /_____ _/ __/ __/  |/  /___ _____ ___  ____ _  
 / / / /\__ \\__ \/ __/ __ `/ /_/ /_/ /|_/ / __ `/ __ `__ \/ __ `/  
/ /_/ /___/ /__/ / /_/ /_/ / __/ __/ /  / / /_/ / / / / / / /_/ /   
\____//____/____/\__/\__,_/_/ /_/ /_/  /_/\__,_/_/ /_/ /_/\__,_/    
                                                 [bigb0ss]          
[INFO] Hunter.io search...
[INFO] {first}.{last}
[INFO] Found first.last Naming Scheme
[INFO] Total Pages: 591
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page1
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page2
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page3
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page4
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page5
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page6
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page7
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page8
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page9
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page10
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page11
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page12
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page13
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page14
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page15
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page16
[INFO] Fetching usernames: https://bearsofficialsstore.com/company/target/page17
...snip...
```

## Todo
* Add additional parsers to grap information other than usernames. 