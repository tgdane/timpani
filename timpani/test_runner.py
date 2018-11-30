import subprocess

from typing import List


def list_touched_files(project: str, test_file: str) -> List[str]:
    """
    Run a single test in isolation and get all source files that
    were impacted by the test.

    The method reads the output of a py.test --cov run and looks for
    all source files that have > 0% coverage.

    :param project: Name of the source directory.
    :param test_file: Name of the test file.
    :return: List of source files that were touched.
    """
    stdout = run_isolated_test(project, test_file)
    lines = [l for l in stdout.splitlines() if l]
    return lines


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


def run_pytest(options: List[str] = None) -> str:
    """
    Run a pytest command and return the stdout.

    pytest is run via subprocess rather than pytest.main() is running pytest
    as a module will interfere with coverage.

    see: https://docs.pytest.org/en/latest/usage.html#calling-pytest-from-python-code

    :param options: List of options to pass to pytest.
    :return:
    """
    cmd = ['py.test']
    if options:
        cmd.extend(options)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    return stdout.decode()
