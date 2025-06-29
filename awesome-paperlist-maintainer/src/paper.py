import requests
import feedparser
import re
from config.config import VENUE, TOPIC_CATAGORIES_ABBR

class Paper():
    def __init__(self, dict):
        self.title = dict.get("title", "")
        try:
            self.link = dict.get("link")
        except KeyError:
            raise ValueError("Paper dictionary must contain a 'link' key.")
        self.topic = dict.get("topic", "")

        self.authors = dict.get("authors", [])
        self.abstract = dict.get("abstract", "")  # one sentence summary
        self.summary = dict.get("summary", "")   
        self.time = dict.get("time", "")
        self.year = dict.get("year", "")
        self.tags = dict.get("tags", [])
        self.venue = dict.get("venue", "")
        self.topic = dict.get("topic", "")
        self.keywords = dict.get("keywords", [])
        if self.topic not in TOPIC_CATAGORIES_ABBR.values():
            try:
                self.topic = TOPIC_CATAGORIES_ABBR[self.topic]
            except:
                print(f"Warning: Invalid topic category '{self.topic}' in paper with link '{self.link}'.")
                self.topic = "Other"

    def get_info_arxiv(self):
        if not self.link.startswith("http://arxiv.org/"):
            print(f"Warning: Link is not an arXiv URL: {self.link}. Skipping...")
            return False
        arxiv_url = self.link

        match = re.search(r'arxiv\.org/(abs|pdf)/([0-9]+\.[0-9]+)', arxiv_url)
        if not match:
            raise ValueError("Invalid arXiv URL")
        arxiv_id = match.group(2)
        api_url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
        response = requests.get(api_url)
        feed = feedparser.parse(response.text)
        if not feed.entries:
            raise ValueError("No entry found for given arXiv ID")
        entry = feed.entries[0]
        self.title = entry.title.replace("\\", "").replace("\n", "").replace("  ", " ")
        self.authors = [author.name for author in entry.authors] if 'authors' in entry else []
        self.summary = entry.summary if 'summary' in entry else ""
        self.time = entry.published if 'published' in entry else ""
        self.year = entry.published.split("-")[0] if 'published' in entry else ""
        if 'arxiv_comment' in entry:
            matching_venue = next((v for v in VENUE if v in entry.arxiv_comment), None)
            if matching_venue:
                year_match = re.search(r'\b(19|20)\d{2}\b', entry.arxiv_comment) 
                if year_match:
                    year = year_match.group(0) 
                    self.venue = f"{matching_venue} {year}"
        if self.authors == [] or self.title == "":
            raise ValueError("Failed to retrieve complete metadata from arXiv")

    def brief_str(self):
        string = ""
        if self.venue == "":
            string += f"* **{self.title}** [[paper]({self.link})] {self.time[:7]}  \n      {', '.join(self.authors)}."
        else:
            string += f"* **{self.title}** [[paper]({self.link})] {self.time[:7]}  \n      {', '.join(self.authors)}. **{self.venue}**."
        if self.keywords != []:
            string += f"\n\n  Keywords: {', '.join(self.keywords)}."
        return string

    def __repr__(self):
        return f"* **{self.title}** [[paper]({self.link})] {self.time[:7]}  \n      {self.abstract} {" ".join(self.tags)}  \n      {', '.join(self.authors)}.  {self.venue}."