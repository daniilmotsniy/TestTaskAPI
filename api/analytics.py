import json
from json import loads

from flask import Blueprint, request

from seo_analyzer.analyzer import InitialWebAnalytics
from seo_analyzer.investigator import InvestigatorAnalysis


analytics_blueprint = Blueprint('analytics_blueprint', __name__)


@analytics_blueprint.route('/', methods=('GET',))
def hello():
    return json.dumps("Welcome to the SEO analysis tool!")


@analytics_blueprint.route('/create_analytics', methods=('POST',))
def create_analytics():
    """
    this endpoint allows to make
    analytics from URL and post it to DB
    """
    raw_data: dict = loads(request.data)
    url: str = raw_data.get('url')
    analyzer = InitialWebAnalytics(url)

    data = analyzer.initial_seo_analyze()
    analyzer.save_to_db()

    return json.dumps(data)


@analytics_blueprint.route('/investigate_analytics', methods=('POST',))
def investigate_analytics():
    """
    this endpoint allows to get analytics
    from DB using website domain
    """
    raw_data = loads(request.data)
    domain: str = raw_data.get('domain_name')
    data = InvestigatorAnalysis(domain).get_analytics()

    return json.dumps(data)
