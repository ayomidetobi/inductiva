"""Register CLI commands for logs."""
from ast import Constant
import os
from inductiva import constants

from inductiva._cli import loader, utils


def register(root_parser):

    parser = root_parser.add_parser(
        "resources", help="Computational resource management utilities")
    utils.show_help_msg(parser)

    subparsers = parser.add_subparsers()
    loader.load_commands(subparsers,
                         os.path.dirname(__file__),
                         package=__name__,
                         ignores_prefix=constants.LOADER_IGNORE_PREFIX)
