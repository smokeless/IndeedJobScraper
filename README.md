# Indeed Job Scraper
This package searches indeed.com and returns a list of results. It requires BeautifulSoup to function.

Example code:
```
from IndeedJobScraper.IndeedJobSearch import IndeedJobSearch

jobs = IndeedJobSearch('super man', 'redwood city', 'CA')
jobList = jobs.get_jobs()
for i in jobList:
    print(i.title) #The posted title.
    print(i.link)  #The link to the job.
    print(i.shortDesc) #Job short description
    print(i.longDesc)  #Job long description
```
