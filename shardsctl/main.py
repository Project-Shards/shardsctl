# main.py
#
# Copyright 2023 axtlos <axtlos@getcryst.al>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-only

import click
import sys
from shardsctl.functions.rebase import rebase_system
from shardsctl.utils.log import setup_logging

logger = setup_logging()


@click.group()
@click.option("--verbose", is_flag=True, help="Enables verbose mode.", default=False)
def main(verbose):
    print("here")
    if verbose:
        print("Verbose mode enabled")


@main.command()
@click.argument("image", type=click.STRING)
@click.argument("repository", type=click.STRING, default="")
def rebase(image, repository):
    rebase_system(image=image, repo=repository)


if __name__ == "__main__":
    sys.exit(main.main())
