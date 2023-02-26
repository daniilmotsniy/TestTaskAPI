from seo_analyzer.analyzer import InitialWebAnalytics


mock_data = {
    "url": "https://google.com"
}


def test_seo_analyze():
    result = InitialWebAnalytics(
        mock_data
    ).initial_seo_analyze()

    assert result['final_status_code'] == 200
    assert result['final_url'] == 'https://google.com'
    assert result['domain_name'] == 'google.com'
    assert result['title'] == 'Google'
