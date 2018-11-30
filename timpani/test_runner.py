import subprocess

from typing import List


def run_isolated_test(project: str, test_file: str):
    """
    Run a single test file in isolation.

    :param project: Name of the source directory.
    :param test_file: Name of the test file.
    :return: py.test output.
    """
    options = [
        '--cov={}'.format(project),
        test_file,
    ]
    return run_pytest(options)


def run_pytest(options: List[str] = []) -> str:
    """
    Run a pytest command and return the stdout.

    pytest is run via subprocess rather than pytest.main() is running pytest
    as a module will interfere with coverage.

    see: https://docs.pytest.org/en/latest/usage.html#calling-pytest-from-python-code

    :param options: List of options to pass to pytest.
    :return:
    """
    cmd = ['py.test'] + options
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    return stdout
