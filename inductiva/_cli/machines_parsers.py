"""Resources CLI subcommand."""
from inductiva import _cli


def add_start_machine_group_subparser(parser):
    """Subparser for start command."""

    subparser = parser.add_parser("machine_group", help="Start a machine Group")

    subparser.add_argument("machine_type",
                           type=str,
                           help="Select the type of each machine")
    subparser.add_argument("-e", "--elastic", default=False, type=bool,
                           help="Whether to use an elastic machine group. " \
                           "If true, the maximum number of machines can be " \
                           "set with the --max_machines flag.")
    subparser.add_argument("-n",
                           "--num_machines",
                           default=1,
                           type=int,
                           help="Number of machines of the group")
    subparser.add_argument("--max_machines", type=int,
                           help="Maximum number of machines of the elastic " \
                           "group. Select a number higher or equal to the " \
                           "number of machines selected with -n or " \
                           "--num_machines. If elastic=False this parameter" \
                           "is not used.")
    subparser.add_argument("-d",
                           "--disk_size",
                           default=70,
                           type=int,
                           help="Disk size in GB")
    subparser.add_argument("-s",
                           "--spot",
                           default=False,
                           type=bool,
                           help="Whether to use spot instances")

    subparser.set_defaults(func=_cli.machines.start_machine_group)


def add_start_machines_cluster_subparser(parser):
    """Subparser for start command."""

    subparser = parser.add_parser("mpi_cluster",
                                  help="Start a MPI machine cluster")

    subparser.add_argument("machine_type",
                           type=str,
                           help="Select the type of each machine")
    subparser.add_argument("-n",
                           "--num_machines",
                           default=1,
                           type=int,
                           help="Number of machines of the group")
    subparser.add_argument("-d",
                           "--disk_size",
                           default=70,
                           type=int,
                           help="Disk size in GB")

    subparser.set_defaults(func=_cli.machines.start_mpi_cluster)


def add_cost_subparser(parser):
    """Subparser for cost command."""

    subparser = parser.add_parser(
        "cost",
        help="Estimate cost of a machine in the cloud",
    )
    subparser.add_argument("machine_type",
                           type=str,
                           help="Type of machine to check the cost.")
    subparser.add_argument("--spot",
                           default=False,
                           type=bool,
                           help="Select between spot instances or not.")

    subparser.set_defaults(func=_cli.machines.estimate_machine_cost)


def add_terminate_subparser(parser):
    """Subparser for terminate command."""
    subparser = parser.add_parser("terminate",
                                  help="Terminate a machine resource")
    subparser.add_argument("name",
                           type=str,
                           help="Name of the machine resource to terminate")
    subparser.set_defaults(func=_cli.machines.terminate_machine_group)


def add_list_subparser(parser):
    """Subparser for list command."""
    subparser = parser.add_parser("list",
                                  help="List currently active resources")
    subparser.set_defaults(func=_cli.machines.list_machine_groups)


def add_available_subparser(parser):
    """Subparser for available command."""
    subparser = parser.add_parser("available",
                                  help="List available machine types")
    subparser.set_defaults(func=_cli.machines.list_machine_types_available)


def register_machines_cli(parser):
    _cli.utils.show_help_msg(parser)
    subparsers = parser.add_subparsers()
    add_list_subparser(subparsers)
    add_available_subparser(subparsers)
    add_cost_subparser(subparsers)
    add_terminate_subparser(subparsers)

    start_resources_subparser = subparsers.add_parser(
        "start", help="Start a computational resource")
    _cli.register_machines_start_cli(start_resources_subparser)


def register_machines_start_cli(parser):
    """Register subcommands for start command."""
    _cli.utils.show_help_msg(parser)
    subparsers = parser.add_subparsers()
    add_start_machine_group_subparser(subparsers)
    add_start_machines_cluster_subparser(subparsers)
