from domain import db


class WebInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    final_url = db.Column(db.String)
    final_status_code = db.Column(db.Integer)
    status_code = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text)
    domain_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Final url: {self.final_url}, ' \
               f'Final status code: {self.final_status_code}, ' \
               f'Status code: {self.status_code}, ' \
               f'Title: {self.status_code}, ' \
               f'Domain name: {self.status_code}.'


web_info_domain_status_code_index = db.Index(
    'web_info_domain_status_code_index',
    WebInfo.domain_name,
    WebInfo.status_code
)

web_info_domain_index = db.Index(
    'web_info_domain_index',
    WebInfo.domain_name
)
