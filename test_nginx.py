import testinfra

def test_nginx_installed(host):
    assert host.package("apache2").is_installed