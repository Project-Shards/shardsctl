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
from shardimg.utils.log import setup_logging
logger = setup_logging()


@click.group()
@click.option('--verbose', is_flag=True, help='Enables verbose mode.', default=False)
def main(verbose):
    if verbose:
        print("Verbose mode enabled")

@main.command()
@click.argument('image', help='The image to rebase to.')
@click.argument('repository', help='The repository to pull the image from.', default=None)
def rebase(image, repository):
    logger.info(f"Rebasing to image {image}")
    logger.info(f"Using repository {repository}")
