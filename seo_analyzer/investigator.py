from domain.web_info_model import WebInfo


class InvestigatorAnalysis:
    SUCCESS = 200

    def __init__(self, domain_name: str):
        self._domain_name: str = domain_name

    def get_analytics(self) -> dict:
        active_count = WebInfo.query.filter_by(
            domain_name=self._domain_name,
            status_code=self.SUCCESS
        ).count()

        db_obj = WebInfo.query.filter_by(
            domain_name=self._domain_name
        ).with_entities(WebInfo.final_url)

        result = [item.final_url for item in db_obj]

        return {
            'active_count': active_count,
            'url_list': result,
            'total_count': len(result),
        }
