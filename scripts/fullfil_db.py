import csv
import logging
import os

from gateway.server import app
from seo_analyzer.analyzer import InitialWebAnalytics

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler())


def fill_from_file(file_name: str):
    file_path = os.path.abspath(
        os.path.dirname(__file__)
    ).split('/scripts')[0] + '/dump/' + file_name
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            next(reader)
            for row in reader:
                analyzer = InitialWebAnalytics(row[0])
                analyzer.initial_seo_analyze()
                analyzer.save_to_db()
    except FileNotFoundError:
        logger.error(f'File {file_path} was not found!')


if __name__ == '__main__':
    with app.app_context():
        fill_from_file('visits.csv')
