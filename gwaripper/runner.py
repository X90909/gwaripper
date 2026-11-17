#!python3
# Python 3.3 comes with PyLauncher "py.exe", installs it in the path, and registers it as the ".py" extension handler. With it, a special comment at the top of a script tells the launcher which version of Python to run
"""Convenience wrapper for running gwaripper directly from source tree.
    from: https://gehrcke.de/2014/02/distributing-a-python-command-line-application/

This module provides entry points for GWARipper CLI commands."""

import sys

from gwaripper.cli import main as cli_main
from gwaripper_webGUI.start_webgui import main as webgui_main
from gwaripper.config import get_root


def main():
    """Run the main gwaripper CLI."""
    return cli_main()


def run_webgui(args=None):
    """Run the web GUI."""
    try:
        get_root()
    except KeyError:
        print("Can't start webGUI before GWARipper has it's path set! Use gwaripper config -p")
        return False
    else:
        # Handle "webgui" subcommand argument
        if args and len(args) > 0 and args[0].lower() == "webgui":
            args = args[1:]
        webgui_main(args)
        return True


# Allow running from command line
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("webgui", "-w"):
        run_webgui(sys.argv[1:])
    else:
        main()