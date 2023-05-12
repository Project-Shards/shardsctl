# rebase.py
#
# Copyright 2023 axtloss <axtlos@getcryst.al>
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

import datetime
from shardsctl.utils.flatpak import FlatpakUtils
from shardsctl.utils.files import FileUtils
from shardsctl.utils.command import Command
from shardsctl.utils.log import setup_logging
logger = setup_logging()

def rebase_system(
        image: str,
        repo: str = None
):
    logger.info(f"Rebasing to image {image}")
    FlatpakUtils.install(
        package=image,
        repo=repo,
        crash=True,
        elevated=False
    )
    location = FlatpakUtils.getpath(image).split(".local/share/flatpak/app/")[1]
    logger.info(f"Updating init configuration")
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
    FileUtils.copy_file("/init.d/rootconf", f"/init.d/rootconf-{current_time}")
    FileUtils.write_file(
        path="/init.d/rootconf",
        content=f"""
export SYSIMAGENAME={image}
export SYSUSRPATH={location}/files/root/usr
export SYSVARPATH={location}/files/root/var
export SYSOPTPATH={location}/files/root/opt
export SYSETCPATH={location}/files/root/etc
"""
    )
