#
# installclass_atomic.py
#
# Atomic-specific partitioning defaults
#
# Copyright (C) 2014  Red Hat, Inc.  All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from pyanaconda.installclasses.fedora import FedoraBaseInstallClass
from pyanaconda.constants import *
from pyanaconda.product import *
from pyanaconda.kickstart import getAvailableDiskSpace
from blivet.partspec import PartSpec
from blivet.autopart import swapSuggestion
from blivet.platform import platform
from blivet.size import Size

class AtomicInstallClass(FedoraBaseInstallClass):
    name = "Atomic Host"
    sortPriority = 11000
    hidden = False

    def setDefaultPartitioning(self, storage):
        # 3GB is obviously arbitrary, but we have to pick some default.
        autorequests = [PartSpec(mountpoint="/", fstype=storage.defaultFSType,
                                size=Size("1GiB"), maxSize=Size("3GiB"),
                                grow=True, lv=True)]

        bootreqs = platform.setDefaultPartitioning()
        if bootreqs:
            autorequests.extend(bootreqs)

        disk_space = getAvailableDiskSpace(storage)
        swp = swapSuggestion(disk_space=disk_space)
        autorequests.append(PartSpec(fstype="swap", size=swp, grow=False,
                                    lv=True, encrypted=True))

        for autoreq in autorequests:
            if autoreq.fstype is None:
                if autoreq.mountpoint == "/boot":
                    autoreq.fstype = storage.defaultBootFSType
                    autoreq.size = Size("300MiB")
                else:
                    autoreq.fstype = storage.defaultFSType

        storage.autoPartitionRequests = autorequests

