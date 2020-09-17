# pylint: disable=invalid-name
import os

from flupy.fluent import flu


def walk_files(*pathes: str, abspath=True) -> "flu[str]":
    """Yield files recursively starting from each location in *pathes"""

    if pathes == ():
        pathes = (".",)

    def _impl():
        for path in pathes:
            for d, _, files in os.walk(path):
                for x in files:
                    rel_path = os.path.join(d, x)
                    if abspath:
                        yield os.path.abspath(rel_path)
                    else:
                        yield rel_path

    return flu(_impl())


def walk_dirs(path: str = ".") -> "flu[str]":
    """Yield files recursively starting from *path"""

    def _impl():
        for d, _, _ in os.walk(path):
            yield d

    return flu(_impl())
