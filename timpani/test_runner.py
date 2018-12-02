import subprocess

from typing import List


def find_tested_sources(project: str, test_file: str) -> List[str]:
    """
    Run a single test in isolation and get all source files that
    were impacted by the test.

    :param project: Name of the source directory.
    :param test_file: Name of the test file.
    :return: List of source files that were touched.
    """
    coverage = generate_coverage(project, test_file)
    return parse_coverage(coverage)


def parse_coverage(lines: List[str]) -> List[str]:
    """
    Return a list of source files impacted by a test run.

    The method reads the output of a py.test --cov run and looks for
    all source files that have > 0% coverage.

    :param lines: Output lines from py.test
    :return: List of test files.
    """
    sources = []
    for line in lines:
        cols = line.split()
        if (len(cols) is 4) and (cols[0].endswith('.py')) and ('%' in cols[3]):
            if int(cols[3].strip('%')) > 0:
                sources.append(cols[0])
    return sources


def generate_coverage(project: str, test_file: str):
    """
    Run a single test file in and return coverage results.

    :param project: Name of the source directory.
    :param test_file: Name of the test file.
    :return: py.test output.
    """
    options = [
        '--cov={}'.format(project),
        test_file,
    ]
    return run_pytest(options)


def run_pytest(options: List[str] = None) -> List[str]:
    """
    Run a pytest command and return the stdout.

    pytest is run via subprocess rather than pytest.main() is running pytest
    as a module will interfere with coverage.

    see: https://docs.pytest.org/en/latest/usage.html#calling-pytest-from-python-code

    :param options: List of options to pass to pytest.
    :return: List of lines output to stdout during pytest run.
    """
    cmd = ['py.test']
    if options:
        cmd.extend(options)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    return stdout.decode().splitlines()
