"""Kills a tasks by id via CLI."""

import inductiva


def kill_task(args):
    """Kills a task by id."""
    inductiva.tasks.Task(args.id).kill(wait_timeout=args.wait)


def register(parser):
    """Register the kill task command."""

    subparser = parser.add_parser("kill", help="Kill a running task.")
    subparser.add_argument("id", type=str, help="Id of the task to kill.")
    subparser.add_argument("-w",
                           "--wait",
                           type=float,
                           default=None,
                           help="Wait timer for kill to complete.")

    subparser.set_defaults(func=kill_task)
