import os
import pytest

from timpani import main


def mock_os_walk_return(path):
    return [
        ('tests', ['core'], ['data.dat', 'common.py', 'test_main.py']),
        ('tests/core', [], ['test_core.py'])
    ]


@pytest.fixture
def patch_os_walk(monkeypatch):
    monkeypatch.setattr(os, 'walk', mock_os_walk_return)


def test_list_test_files(patch_os_walk):
    tests = main.list_test_files('foo')
    assert tests == ['tests/test_main.py', 'tests/core/test_core.py']


def test_list_test_files_filter(patch_os_walk):
    tests = main.list_test_files('foo', '*.py')
    assert tests == ['tests/common.py', 'tests/test_main.py', 'tests/core/test_core.py']


def test_list_test_files_no_tests(patch_os_walk):
    tests = main.list_test_files('foo', 'bar_*.py')
    assert not tests
