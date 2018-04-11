import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert 'docker' in host.user('docker_test').groups


def test_packages(host):
    assert host.package('docker-ce').is_installed


def test_files(host):
    assert host.file('/etc/docker/daemon.json').is_file
