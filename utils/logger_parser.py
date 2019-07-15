#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
from typing import Any, List
import os

from tabulate import tabulate
try:
    import appdirs  # type: ignore
except ImportError:
    appdirs = None

def main():
    """main func"""
    default_log_files = []  # List(Any)
    if appdirs:
        default_log_files += list(Path(
            os.path.join(
                appdirs.user_data_dir('searx', 'asciimoo'), 'log'
            )).glob('*.log'))
    default_log_files += list(Path('.').glob('searx_*.log'))
    log_files = default_log_files
    print('log files:\n{}'.format('\n.'.join(map(str, log_files))))
    contents = []
    for ff in log_files:
        with open(ff) as f:
            contents.append(f.read())

    line_counter = Counter('\n'.join(contents).splitlines())
    print(tabulate(line_counter.most_common()))


if __name__ == '__main__':
    main()
