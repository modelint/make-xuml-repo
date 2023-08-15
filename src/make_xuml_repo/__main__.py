"""
__main__.py

Make an xUML repo
"""

import logging
import logging.config
import sys
import argparse
from pathlib import Path
from make_xuml_repo.metamodel import Metamodel
from make_xuml_repo import version

_logpath = Path("make_xuml_repo.log")
_progname = 'Make xUML repsitory'

def get_logger():
    """Initiate the logger"""
    log_conf_path = Path(__file__).parent / 'log.conf'  # Logging configuration is in this file
    logging.config.fileConfig(fname=log_conf_path, disable_existing_loggers=False)
    return logging.getLogger(__name__)  # Create a logger for this module

# Configure the expected parameters and actions for the argparse module
def parse(cl_input):
    """
    The command line interface is for diagnostic purposes

    :param cl_input:
    :return:
    """
    parser = argparse.ArgumentParser(description=_progname)
    parser.add_argument('-D', '--debug', action='store_true',
                        help='Debug mode'),
    parser.add_argument('-V', '--version', action='store_true',
                        help='Print the current version of parser')
    return parser.parse_args(cl_input)


def main():
    # Start logging
    logger = get_logger()
    logger.info(f'{_progname}: {version}')

    # Parse the command line args
    args = parse(sys.argv[1:])

    if args.version:
        # Just print the version and quit
        print(f'{_progname} version: {version}')

    Metamodel.create_db()

    logger.info("No problemo")  # We didn't die on an exception, basically
    print("\nNo problemo")


if __name__ == "__main__":
    main()
