"""
__main__.py

Make an xUML repo
"""

# System
import logging
import logging.config
import sys
import atexit
import argparse
from pathlib import Path

# Make xuml repo
from make_xuml_repo.metamodel import Metamodel
from make_xuml_repo import version

_logpath = Path("make_xuml_repo.log")
_progname = 'Make xUML repository'

def clean_up():
    """Normal and exception exit activities"""
    _logpath.unlink(missing_ok=True)

def get_logger(verbose=False):
    """Initiate the logger"""
    log_conf_path = Path(__file__).parent / 'log.conf'  # Logging configuration is in this file
    logging.config.fileConfig(fname=log_conf_path, disable_existing_loggers=False)
    if not verbose:
        # Suppress warnings on the console; they still go to the log file.
        # Raise the level of any console (non-file) stream handler above WARNING.
        for handler in logging.getLogger().handlers:
            if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
                handler.setLevel(logging.ERROR)
    return logging.getLogger(__name__)  # Create a logger for this module

# Configure the expected parameters and actions for the argparse module
def parse(cl_input):
    parser = argparse.ArgumentParser(description=_progname)
    parser.add_argument('-D', '--debug', action='store_true',
                        help='Debug mode'),
    parser.add_argument('-V', '--version', action='store_true',
                        help='Print the current version of parser')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show warnings on the console')
    parser.add_argument('-L', '--log', action='store_true',
                        help='Generate a diagnostic make_xuml_repo.log file')
    return parser.parse_args(cl_input)


def main():
    # Parse the command line args
    args = parse(sys.argv[1:])

    # Start logging (warnings appear on the console only in verbose mode)
    logger = get_logger(verbose=args.verbose)
    logger.info(f'{_progname}: {version}')

    if not args.log:
        # If no log file is requested, remove the log file before termination
        atexit.register(clean_up)

    if args.version:
        # Just print the version and quit
        print(f'{_progname} version: {version}')
        sys.exit(0)

    Metamodel.create_db()

    logger.info("No problemo")  # We didn't die on an exception, basically
    if args.verbose:
        print("\nNo problemo")


if __name__ == "__main__":
    main()
