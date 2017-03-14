import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_authorized_keys_added(File):
    f = File('/root/.ssh/authorized_keys')
    assert f.contains('test1@example.com')
    assert f.contains('test2@example.com')


def test_authorized_keys_removed(File):
    f = File('/root/.ssh/authorized_keys')
    assert not f.contains('test3@example.com')
    assert not f.contains('test4@example.com')
