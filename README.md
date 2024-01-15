# Dutch Government Bug Bounty Scope Analysis
Welcome to the repository dedicated to the analysis of the Dutch government's bug bounty program which includes an extensive list of domains, subdomains, and URLs, along with in-depth daily analysis. *This is **NOT** official bugbounty scope.*
## Overview
This project aims to provide a detailed overview of the digital landscape covered by the Dutch government's bug bounty program. By cataloging and analyzing various aspects of the web infrastructure, it's aim to contribute to the security and robustness of these digital assets.
### What is in scope?
This repository focuses on specific government-related resources. Each resource is selected based on the following criteria:
1. **Meta Information Requirement:** The resource must include 'RIJKSOVERHEID.Organisatie' in its meta information.
2. **Government Logo:** It's essential that the resource displays the official government logo.
3. **Affiliation Declaration:** The page must clearly state its affiliation with the government.
### How It Works
Process for updating this repository is thorough and regular. Here's an overview of how it operates:
1. **Daily Review and Addition:** New resources are added regulary, either through manual review or automatic processes.
2. **Use of Specialized Tools:** shrewdeye.app and its standalone version are used to build pipline for analysis and discovery.
3. **Workflow Pipeline:**
      - **Subdomain discovery:**  - Shrewdeye.App(API), Amass, Subfinder, Assetfinder, and DnsX.
      - **DNS Clearout:** This step is dedicated to filtering and clarifying DNS data.
      - **URL Collection:** Httpx is used for further data processing and refinement.
      - **SSL Analysis:** Lastly, we apply the SSLLabs API to assess SSL configurations and grades.




This structured approach ensures that our repository is always up-to-date and accurately reflects the current digital landscape of the Dutch government.
In the [`data/`](/data) directory, there's an analysis of security configurations for various resources, including the following information:
 - **URL**
 - **SSL:** Grade from [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
 - **Server:** *Server header* from web serber
 - **Cookie:** :white_check_mark: if HttpOnly, Secure and Same-Site flag are set
 - **HSTS:** :white_check_mark: if *Strict-Transport-Security* header is set
 - **CSP:** :white_check_mark: if *Content-Security-Policy* header is set and *unsafe-inline* and *unsafe-eval* not present in configuration.
 - **XFO:** :white_check_mark: if *X-Frame-Options* header is set
 - **XXP:** :white_check_mark: if *X-Xss-Protection* header is set
 - **RP:** :white_check_mark: if *Referrer-Policy* header is set
## Repository Structure
 - [domains.txt](/domains.txt): List of all domains in scope
 - [subdomains.txt](/subdomains.txt): Detailed list of **16298** alive subdomains.
 - [urls.txt](/urls.txt): Compilation of **10025** URLs.
 - [all_subdomains.txt](/all_subdomains.txt): All **32182** subdomains that were found all over the time 
 - [data/](/data): Folder containing daily updated analysis for every domain.
## Links and acknowledgements
 - [basisbeveiliging.nl](https://basisbeveiliging.nl/) \- *How well the Dutch government implements basic security requirements with great security map!*
 - [overheid.nl](https://www.overheid.nl/english/dutch-government-websites)
 - [gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad](https://https://gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad)
 - [communicatierijk.nl/vakkennis/r/rijkswebsites/verplichte-richtlijnen/websiteregister-rijksoverheid](https://www.communicatierijk.nl/vakkennis/r/rijkswebsites/verplichte-richtlijnen/websiteregister-rijksoverheid)
 - [ncsc.nl](https://www.ncsc.nl/contact/kwetsbaarheid-melden/cvd-meldingen-formulier)
 - [shrewdeye.app](https://shrewdeye.app)
 - [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
## Key Statistics




### SSL Grades
Analysys and grade statistics of SSL configuration with [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
|$${\color{green}A}$$|$${\color{lightgreen}B}$$|$${\color{orange}C/D}$$|$${\color{red}E/F}$$|
|---|---|---|---|
 |1157|61|0|10|


### Cookies Security Flags
Cookies play a crucial role in web security and with special flag attributes security could enhance cookie of customers very much:
 - **HttpOnly (1399):** Helps mitigate the risk of client-side script accessing the protected cookie.
 - **Secure (1405):** Ensures cookies are sent over secure, HTTPS connections.**
 - **Same-Site (24):** Prevents the browser from sending this cookie along with cross-site requests.


### Top 5 server headers
 - nginx \- **3079**
 - Microsoft-IIS/10.0 \- **990**
 - Apache \- **860**
 - BigIP \- **150**
 - Microsoft-HTTPAPI/2.0 \- **135**
 - Apache/2 \- **119**


### Most 20 widespread tech
- HSTS \- **7465** 
- Nginx \- **3230** 
- Server \- **2132** 
- Microsoft \- **1263** 
- Apache \- **1199** 
- ASP.NET \- **1122** 
- HTTP \- **1087** 
- Windows \- **1036** 
- IIS \- **1035** 
- PHP \- **550** 
- Bloomreach \- **477** 
- Amazon \- **338** 
- Azure \- **285** 
- Basic \- **273** 
- Drupal \- **233** 
- Java \- **231** 
- Bootstrap \- **207** 
- F5 \- **187** 
- BigIP \- **187** 
- Web \- **160** 
- Services \- **160** 