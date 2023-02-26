import logging
from urllib.parse import urlparse

import cloudscraper
import requests
from bs4 import BeautifulSoup

from domain import db
from domain.web_info_model import WebInfo

scraper = cloudscraper.create_scraper()

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())


class InitialWebAnalytics:
    def __init__(self, url: str):
        self._url: str = url
        self._result = None

    def initial_seo_analyze(self) -> dict:
        """
        allows to scrap website SEO data by given URL
        """
        try:
            html = requests.get(self._url)
        except requests.exceptions.RequestException:
            logger.error('There was connection error!')
            return {"final_url": self._url}

        soup = BeautifulSoup(html.text, features="html.parser")
        meta_title = (soup.find('title')).get_text()

        self._result = {
            "final_url": self._url,
            "final_status_code": html.status_code,
            "status_code": html.status_code,
            "title": meta_title,
            "domain_name": urlparse(self._url).netloc
        }

        if not html.is_redirect:
            return self._result

        html = html.history[-1]
        self._result['final_url'] = urlparse(html.url).netloc
        self._result['final_status_code'] = html.status_code

        return self._result

    def save_to_db(self):
        """
        saving SEO to DB
        """
        if not self._result:
            return

        db_obj = WebInfo(**self._result)
        db.session.add(db_obj)
        db.session.commit()
