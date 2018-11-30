import subprocess
from unittest import mock

from timpani import test_runner


@mock.patch('timpani.test_runner.run_pytest')
def test_run_isolated_test(mock_run_pytest):
    mock_run_pytest.return_value = 'output'
    out = test_runner.run_isolated_test('bob', 'tests/test_bob.py')
    assert mock_run_pytest.called_once_with(
        ['--cov=bob', 'tests/test_bob.py']
    )
    assert out == 'output'


@mock.patch('subprocess.Popen')
def test_run_pytest(mock_subproc_popen):
    process_mock = mock.Mock()
    attrs = {'communicate.return_value': ('output', 'error')}
    process_mock.configure_mock(**attrs)
    mock_subproc_popen.return_value = process_mock

    out = test_runner.run_pytest([1, 2])
    assert mock_subproc_popen.called_once_with(['py.test', 1, 2])
    assert mock_subproc_popen.communicate.called_once()
    assert out == 'output'
