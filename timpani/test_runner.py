import nose

from typing import List


def exec_nose(options: List[str] = []) -> bool:
    """
    Run a nose command.

    :param options: List of options to pass to nose
    :return: True if tests passed
    """
    return nose.run(options)
