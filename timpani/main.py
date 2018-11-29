"""
Main entry point to timpani.
"""

import fnmatch
import os
from typing import List


def list_test_files(test_dir: str, pattern='test_*.py') -> List[str]:
    """
    List all python test files in the test directory.

    :param test_dir: Top-level folder containing test files.
    :param pattern: Filename filter for test files.
    :return: List of test files.
    """
    return filter_files(test_dir, pattern)


def list_source_files(source_dir: str, pattern='*.py') -> List[str]:
    """
    List all source files in the source directory.

    :param source_dir: Top-level folder containing source code.
    :param pattern: Filename filter for source files.
    :return: List of source files.
    """
    return filter_files(source_dir, pattern)


def filter_files(directory: str, pattern: str) -> List[str]:
    """
    Generic method to list all files in directory matching pattern.

    :param directory: Top-level search directory.
    :param pattern: File matching pattern, uses the fnmatch syntax.
    :return: List of matching files.
    """
    matches = []
    for root, _, file_names in os.walk(directory):
        for filename in fnmatch.filter(file_names, pattern):
            matches.append(os.path.join(root, filename))
    return matches
