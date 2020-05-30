import testinfra

def test_nginx_installed(host):
    assert host.package("nginx").is_installed