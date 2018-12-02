from unittest import mock

from timpani import test_runner


COVERAGE_LINES = [
    "Name                     Stmts   Miss  Cover",
    "--------------------------------------------",
    "timpani/__init__.py          0      0   100%",
    "timpani/main.py             13     13     0%",
    "timpani/test_runner.py      23      9    61%",
    "--------------------------------------------",
    "TOTAL                       36     22    39%",
]

TOUCHED_SOURCES = [
    'timpani/__init__.py',
    'timpani/test_runner.py',
]


@mock.patch('timpani.test_runner.generate_coverage')
def test_find_tested_sources(mock_generate_coverage):
    mock_generate_coverage.return_value = COVERAGE_LINES

    out = test_runner.find_tested_sources('timpani', 'tests/test_main.py')
    assert mock_generate_coverage.called_once_with('timpani', 'tests/test_main.py')
    assert out == TOUCHED_SOURCES


def test_parse_coverage():
    tests = test_runner.parse_coverage(COVERAGE_LINES)
    assert tests == TOUCHED_SOURCES


@mock.patch('timpani.test_runner.run_pytest')
def test_generate_coverage(mock_run_pytest):
    mock_run_pytest.return_value = COVERAGE_LINES
    out = test_runner.generate_coverage('timpani', 'tests/test_main.py')
    assert mock_run_pytest.called_once_with(['--cov=timpani', 'tests/test_main.py'])
    assert out == COVERAGE_LINES


@mock.patch('subprocess.Popen')
def test_run_pytest(mock_subproc_popen):
    process_mock = mock.Mock()
    attrs = {'communicate.return_value': (b'1\n2\n', 'error')}
    process_mock.configure_mock(**attrs)
    mock_subproc_popen.return_value = process_mock

    out = test_runner.run_pytest(['1', '2'])
    assert mock_subproc_popen.called_once_with(['py.test', '1', '2'])
    assert mock_subproc_popen.communicate.called_once()
    assert out == ['1', '2']
