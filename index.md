---
layout: default
---
## Overview
This project aims to provide a detailed overview of the digital landscape covered by the Dutch government's bug bounty program. By cataloging and analyzing various aspects of the web infrastructure, it's aim is to contribute to the security and robustness of these digital assets.
### What is in scope?
This repository focuses on specific government-related resources. Each resource is selected based on the following criteria:
1. **Meta Information Requirement:** The resource must include 'RIJKSOVERHEID.Organisatie' in its meta information.
2. **Government Logo:** It's essential that the resource displays the official government logo.
3. **Affiliation Declaration:** The page must clearly state its affiliation with the government.
### How It Works
Process for updating this repository is thorough and regular. Here's an overview of how it operates:
1. **Daily Review and Addition:** New resources are added regularly, either through manual review or automatic processes.
2. **Use of Specialized Tools:** shrewdeye.app and its standalone version are used to build pipeline for analysis and discovery.
3. **Workflow Pipeline:**
      - **Subdomain discovery:**  - Shrewdeye.App(API), Amass, Subfinder, Assetfinder, and DnsX.
      - **DNS Clearout:** This step is dedicated to filtering and clarifying DNS data.
      - **URL Collection:** Httpx is used for further data processing and refinement.
      - **SSL Analysis:** Lastly, we apply the SSLLabs API to assess SSL configurations and grades.




This structured approach ensures that our repository is always up-to-date and accurately reflects the current digital landscape of the Dutch government.
 - **URL**
 - **SSL:** Grade from [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
 - **HTTP Rank:** Based on HTTP headers statistics from below
 - **Server:** *Server header* from web server. If not set +5 points
 - **Cookie:** :white_check_mark: if HttpOnly (+7), Secure(+7) and Same-Site(+6) flag are set
 - **HSTS:** :white_check_mark: if *Strict-Transport-Security* header is set(+30)
 - **CSP:** :white_check_mark: if *Content-Security-Policy* header is set(+10) and *unsafe-inline* and *unsafe-eval* not present in configuration (+5)
 - **XFO:** :white_check_mark: if *X-Frame-Options* header is set (+10)
 - **XXP:** :white_check_mark: if *X-Xss-Protection* header is set (+10)
 - **RP:** :white_check_mark: if *Referrer-Policy* header is set (+10)
 - **FP:** :white_check_mark: if *Feature-Policy* header is set (+10)
 - **CORS:** :white_check_mark: if *CORS* header is set without issues (+10)
## Summary
 - Number of domains: **1429**
 - Number of subdomains: **91570**
 - Number of urls: **61792**
 -  Average HTTP Security headers rank: **E**
 - Average SSL grade: **F**
 - Number of [security.txt](https://www.digitaleoverheid.nl/nieuws/standaard-security-txt-nu-verplicht-voor-overheid/): **5503**
### Repository Structure
 - [domains.txt](https://raw.githubusercontent.com/zzzteph/DutchGovScope/main/storage/dutchgov/domains.txt): List of **1429** domains in scope
 - [subdomains.txt](https://raw.githubusercontent.com/zzzteph/DutchGovScope/main/storage/dutchgov/subdomains.txt): Detailed list of **91570** alive subdomains.
 - [urls.txt](https://raw.githubusercontent.com/zzzteph/DutchGovScope/main/storage/dutchgov/urls.txt): Compilation of **61792** URLs.
 - [all_subdomains.txt](https://raw.githubusercontent.com/zzzteph/DutchGovScope/main/storage/dutchgov/all_subdomains.txt): All **119273** subdomains that were found all over the time 
## Links and acknowledgements
 - [bug-bounty-dutch-goverment-scope.md](https://gist.github.com/zzzteph/99a7bd2acde12cb4b2626fc9261bc56d)
 - [basisbeveiliging.nl](https://basisbeveiliging.nl/)
 - [overheid.nl](https://www.overheid.nl/english/dutch-government-websites)
 - [random-robbie/f985ad14fede2c04ac82dd89653f52ad](https://gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad)
 - [communicatierijk.nl](https://www.communicatierijk.nl/vakkennis/r/rijkswebsites/verplichte-richtlijnen/websiteregister-rijksoverheid)
 - [ncsc.nl](https://www.ncsc.nl/contact/kwetsbaarheid-melden/cvd-meldingen-formulier)
 - [shrewdeye.app](https://shrewdeye.app)
 - [ssllabs.com/ssltest](https://www.ssllabs.com/ssltest/)
 - [securityheaders.com](https://securityheaders.com/)
 - [NCSC HOF](https://www.ncsc.nl/contact/kwetsbaarheid-melden/wall-of-fame)