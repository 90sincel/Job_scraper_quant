import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
page_content = page.content
soup = BeautifulSoup(page_content, 'html.parser')
results = soup.find(id="ResultsContainer")
job_elems = results.find_all('section', class_='card-content')

# Naive filter for python jobs: TOO SPECIFIC, everything has to be exactly the same as 'Python Developer'
# **** python_jobs = results.find_all('h2', string='Python Developer')
# Much better filter for python jobs, becomes case insensitive and only looks for python. 
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
print(len(python_jobs))


for job_elem in job_elems:
    # Each job_elem is now a new BeautifulSoup object
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    # To skip over problamatic elements with NONE 
    if None in (title_elem, company_elem, location_elem):
        continue
    # As a BeautifulSoup object you can perform a text-only action on html elements
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()


#print(results.prettify())
#pprint(page_content)