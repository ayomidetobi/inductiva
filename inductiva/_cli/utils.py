"""CLI utils."""
from inductiva import api


def show_help_msg(parser):
    """Show help message for command if no subcommand is provided."""
    parser.set_defaults(func=lambda _: parser.print_help())


def register():
    """Register a new user."""
    print("Registering user...")

    login_manager = api.LoginManager()
    login_manager.start_web_server()
    login_manager.open_browser()

