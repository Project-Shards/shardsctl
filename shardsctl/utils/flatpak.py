# flatpak.py
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
import os
import sys
from shardsctl.utils.command import Command
from shardsctl.utils.log import setup_logging

logger = setup_logging()


class FlatpakUtils:
    @staticmethod
    def install(
        package: str,
        repo: str = None,
        crash: bool = False,
        elevated: bool = False,
    ):
        if repo is None or repo.strip() == "":
            repo = "shards"  # TODO: define this using a config file
        logger.info(f"Installing package {package} using repository {repo}")

        Command.execute_command(
            command=[
                "flatpak",
                "install",
                "--noninteractive",
                "--assumeyes",
                repo,
                package,
            ],
            command_description=f"Installing {package}",
            crash=crash,
        )

    @staticmethod
    def remove(
        package: str,
        repo: str = None,
        crash: bool = False,
        elevated: bool = False,
    ):
        if repo is None or repo.strip() == "":
            repo = "shards"  # TODO: set this using a config
        logger.info(f"Uninstalling package {package} from {repo}")
        Command.execute_command(
            command=["flatpak", "uninstall", repo, package],
            command_description=f"Uninstalling {package}",
            crash=crash,
        )

    @staticmethod
    def update(package: str = None, crash: bool = False, elevated: bool = False):
        logpart1 = f"Updating "
        logpart2 = f"package {package} " if package is not None else ""
        logger.info(logpart1 + logpart2)

        Command.execute_command(
            command=["flatpak", "update", package],
            command_description=logpart1 + logpart2,
            crash=crash,
        )

    @staticmethod
    def getpath(package: str) -> str:
        out = Command.execute_command(
            command=["flatpak", "info", "-l", package],
            command_description=f"Getting path for package {package}",
            crash=True,
            capture=True,
        )
        return out[1].decode("utf-8").strip()
