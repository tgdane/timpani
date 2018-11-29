import nose
from unittest import mock

from timpani import test_runner


def test_exec_nose():
    nose.run = mock.MagicMock(return_value=True)
    ret = test_runner.exec_nose()
    assert nose.run.called_once()
    assert ret


def test_exec_nose_failure():
    nose.run = mock.MagicMock(return_value=False)
    ret = test_runner.exec_nose()
    assert not ret


def test_exec_nose_with_options():
    nose.run = mock.MagicMock()
    test_runner.exec_nose([1, 2])
    assert nose.run.called_once_with([1, 2])
