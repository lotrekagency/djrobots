
def test_simple_robots_request(settings, client):
    settings.DEBUG = True
    assert 'Disallow: /' in str(client.get('/robots.txt').content)


def test_simple_robots_request_on_production(settings, client):
    settings.DEBUG = False
    assert 'Disallow: /' not in str(client.get('/robots.txt').content)


def test_simple_robots_prod_request_with_disallow(settings, client):
    settings.DEBUG = False
    settings.DJROBOTS_DISALLOWALL = True
    assert 'Disallow: /' in str(client.get('/robots.txt').content)


def test_simple_robots_debug_request_with_disallow(settings, client):
    settings.DEBUG = True
    settings.DJROBOTS_DISALLOWALL = True
    assert 'Disallow: /' in str(client.get('/robots.txt').content)


def test_sitemap(settings, client):
    settings.DJROBOTS_SITEMAPS = [
        'sitemap', '/my-sitemap-index.xml'
    ]
    assert 'sitemap.xml' in str(client.get('/robots.txt').content)
    assert '/my-sitemap-index.xml' in str(client.get('/robots.txt').content)


def test_sitemap_set_as_a_string(settings, client):
    settings.DJROBOTS_SITEMAPS = 'sitemap'
    assert 'sitemap.xml' in str(client.get('/robots.txt').content)


def test_sitemap_set_as_a_string_for_abs_uri(settings, client):
    settings.DJROBOTS_SITEMAPS = '/my-sitemap-index.xml'
    assert '/my-sitemap-index.xml' in str(client.get('/robots.txt').content)
