import requests
from bs4 import BeautifulSoup
from .IndeedJob import IndeedJob


class IndeedJobSearch:
    def __init__(self, jobtype: str, location: str, state: str):
        self.jobtype = ''.join([ch if ch != ' ' else '+' for ch in jobtype])
        self.city = ''.join([ch if ch != ' ' else '+' for ch in location])

        if len(state) > 2:
            raise ValueError('Expected state to be 2 letter form.')
        else:
            self.state = state

        self.jobList = self._build_jobs()

    def _build_jobs(self)->list:
        url = 'https://indeed.com/jobs?q={}&l={}%2C+{}'.format(self.jobtype, self.city, self.state)
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        body = soup.find_all('a', {'data-tn-element':'jobTitle'})
        jobTitles = [i.text for i in body]
        linkList = []

        # There's some wonky stuff going on with being able to click these, so
        # we'll have to rewrite the link. Need to filter out "/rc/clk?".
        # Rather than do a regex, we'll just slice the string.

        for i in body:
            linkSoup = BeautifulSoup(str(i), 'html.parser')
            link = linkSoup.find('a', href=True)
            links = link['href']
            links = links[8:]
            linkList.append(('https://www.indeed.com/viewjob?'+links))

        body = soup.find_all('span', {'class':'summary'})
        shortList = []
        for i in body:
            shortList.append(i.text)

        longList = []

        for i in linkList:
            longList.append(self._build_longs(i))

        jobList = []

        for index, item in enumerate(jobTitles):
            job = IndeedJob(jobTitles[index], linkList[index], shortList[index], longList[index])
            jobList.append(job)

        return jobList


    def _build_longs(self, link: str)->list:
        r = requests.get(link).text
        soup = BeautifulSoup(r, 'html.parser')
        title = soup.find('title').text[:-12]
        long = soup.find('span', {'id':'job_summary'}).text
        long = title + long + '\n'
        return long

    def get_jobs(self):
        return self.jobList



