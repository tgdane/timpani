import os
import pytest
from unittest import mock

from timpani import main


def mock_os_walk_return(path):
    return [
        ('tests', ['core'], ['data.dat', 'common.py', 'test_main.py']),
        ('tests/core', [], ['test_core.py'])
    ]


@pytest.fixture
def patch_os_walk(monkeypatch):
    monkeypatch.setattr(os, 'walk', mock_os_walk_return)


def test_filter_files(patch_os_walk):
    files = main.filter_files('foo', '*.py')
    assert files == ['tests/common.py', 'tests/test_main.py', 'tests/core/test_core.py']


def test_filter_files_no_tests(patch_os_walk):
    files = main.filter_files('foo', 'bar_*.py')
    assert not files


def test_list_test_files(patch_os_walk):
    main.filter_files = mock.MagicMock()
    main.list_test_files('foo')
    assert main.filter_files.called_once_with('foo', 'test_*.py')


def test_list_source_files(patch_os_walk):
    main.filter_files = mock.MagicMock()
    main.list_source_files('foo')
    assert main.filter_files.called_once_with('foo', '*.py')
