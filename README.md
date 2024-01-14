# Dutch Government Bug Bounty Scope Analysis
Welcome to the repository dedicated to the analysis of the Dutch government's bug bounty program. This comprehensive repository includes an extensive list of domains, subdomains, and URLs, along with in-depth daily analysis.
## Overview
This project aims to provide a detailed overview of the digital landscape covered by the Dutch government's bug bounty program. By cataloging and analyzing various aspects of the web infrastructure, it's aim to contribute to the security and robustness of these digital assets.
### What is in scope?
This repository focuses on specific government-related resources. Each resource is carefully selected based on the following criteria:
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
## Repository Structure
 - [domains.txt](/domains.txt): List of all domains in scope
 - [subdomains.txt](/subdomains.txt): Detailed list of **0** alive subdomains.
 - [urls.txt](/urls.txt): Compilation of **10025** URLs.
 - [all_subdomains.txt](/all_subdomains.txt): All **32151** subdomains that were found all over the time 
 - [data/](/data): Folder containing daily updated analysis for every domain.
## Key Statistics


### SSL Grades
|$${\color{green}A}$$|$${\color{lightgreen}B}$$|$${\color{orange}C/D}$$|$${\color{red}E/F}$$|
|---|---|---|---|
 |1156|61|0|9|


### Cookies Security Flags
Cookies play a crucial role in web security and with special flag attributes security could enhance cookie of customers very much:
 - **HttpOnly (1391):** Helps mitigate the risk of client-side script accessing the protected cookie.
 - **Secure (**1397): Ensures cookies are sent over secure, HTTPS connections.**
 - **Same-Site (**24):** Prevents the browser from sending this cookie along with cross-site requests.


### Top 5 servers
 - nginx \- **3080**
 - Microsoft-IIS/10... \- **984**
 - Apache \- **863**
 - BigIP \- **151**
 - Microsoft-HTTPAP... \- **134**
 - Apache/2 \- **119**


### Most widespread tech
- HSTS \- **7423** 
- Nginx \- **3224** 
- Server \- **2126** 
- Microsoft \- **1254** 
- Apache \- **1202** 
- ASP.NET \- **1114** 
- HTTP \- **1089** 
- Windows \- **1028** 
- IIS \- **1027** 
- PHP \- **552** 
- Bloomreach \- **477** 
- Amazon \- **334** 
- Azure \- **284** 
- Basic \- **271** 
- Drupal \- **233** 
- Java \- **233** 
- Bootstrap \- **211** 
- F5 \- **188** 
- BigIP \- **188** 
- Web \- **158** 
- Services \- **158** 
- WordPress \- **147** 
- MySQL \- **144** 
- HTTPAPI \- **137** 
- Cloudflare \- **135** 
- Tomcat \- **109** 