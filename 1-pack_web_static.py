#!/usr/bin/python3
"""Fabric script that generates a
    .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack"""

from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """packs web_static folder to .tgz"""
    timeDate = datetime.now()
    arch = "web_static_{}".format(timeDate.strftime('%Y%m%d%H%M%S'))

    if not os.path.exists("./versions"):
        local("mkdir versions")

    tarFile = local("tar -czvf versions/{}.tgz ./web_static".format(arch))

    if tarFile.failed:
        return (None)

    return ("versions/{}.tgz".format(arch))
