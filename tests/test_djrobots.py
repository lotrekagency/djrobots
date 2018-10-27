
def test_simple_robots_request(settings, client):
    settings.DEBUG = True
    assert 'Disallow: /' in str(client.get('/robots.txt').content)


def test_simple_robots_request_on_production(settings, client):
    settings.DEBUG = False
    assert 'Disallow: /' not in str(client.get('/robots.txt').content)
