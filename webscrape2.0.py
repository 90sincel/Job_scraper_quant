import requests
from bs4 import BeautifulSoup
import pprint

URL = "https://wilmott.com/jobs/"
page = requests.get(URL)
page_content = page.content
#print(page_content)
soup = BeautifulSoup(page_content, 'html.parser')
results = soup.find(id='main-content')
#print(results.prettify())
job_elems = results.find_all('div', class_='wpjb-job-list wpjb-grid')
#print(job_elems)
#for job_elem in job_elems:
#    trading_jobs = []
#    title_elem = job_elem.find('a', class_='wpjb-job_title wpjb-title')
#    type_elem = job_elem.find('span', class_='wpjb-job_type wpjb-sub-title')
#    company_elem = job_elem.find('span', class_='wpjb-sub wpjb-company_name')
#    location_elem = job_elem.find('span', class_='wpjb-glyphs wpjb-icon-location')
#    if None in (title_elem, type_elem, company_elem, location_elem):
#        continue
#    elif 'Quant Trading' in title_elem.text.strip():
#        trading_jobs.append(title_elem.text.strip())
#    else:
#        print(title_elem.text.strip())
#        print(type_elem.text.strip())
#        print(company_elem.text.strip())
#        print(location_elem.text.strip())
#        print(trading_jobs)

quant_jobs = results.find_all('div', class_='wpjb-category-quantitative-analyst')
#print(quant_jobs)
#qaunt_hunt(quant_jobs):
for quant_job in quant_jobs:
    link = quant_job.find('a')['href']
    trading_jobs = []
    trad_jobs_href = []
    job = quant_job.find('a', class_='wpjb-job_title wpjb-title')
    job_title = job.text.strip()
    if 'quant trading' in job_title.lower():
        trading_jobs.append(job_title)
if len(trading_jobs) > 0:
    print("There are {} trading jobs availiable.".format(len(trading_jobs)))
else:
    print("No trading jobs availiable right now.")
        

for quant_job in quant_jobs:
    link = quant_job.find('a')['href']
    link = link.strip()
    print(f'Apply here: {link}\n')