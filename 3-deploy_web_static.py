#!/usr/bin/python3
"""Fabric script that generates a
    .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack"""


import os
from datetime import datetime
from fabric.api import env, local, put, run


env.hosts = ["34.224.6.206", "34.201.161.84"]


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


def do_deploy(archive_path):
    """deploys web_static archive to the remote servers"""
    if not os.path.exists(archive_path):
        return (False)

    try:
        file = archive_path.split("/")[1]
        file2 = file.split(".")[0]

        put(archive_path, "/tmp/", use_sudo=True)
        run("tar -xvzf /tmp/{} -C /data/web_static/releases/".format(file))
        run("mv /data/web_static/releases/web_static {}".format(
            "/data/web_static/releases/{}".format(file2)
        ))
        run("rm -rf /tmp/{}".format(file))
        run("rm /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(
            "/data/web_static/releases/{}".format(file2)
        ))
        return (True)
    except Exception:
        return (False)

def deploy():
    """creates and distributes an archive
    to your web servers, using the function deploy"""

    arch = do_pack()
    if arch is None:
        return (False)

    return (do_deploy(arch))
