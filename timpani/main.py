"""
Main entry point to timpani.
"""

import fnmatch
import os
from typing import List


def list_test_files(test_dir: str, file_filter='test_*.py') -> List[str]:
    """
    List all of the python test files in the test directory.

    :param test_dir: Top-level folder containing test files.
    :param file_filter: Filename filter for test files.
    :return: List of test files.
    """
    test_files = []
    for root, _, file_names in os.walk(test_dir):
        for filename in fnmatch.filter(file_names, file_filter):
            test_files.append(os.path.join(root, filename))
    return test_files
