#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy"""

from fabric.api import env, put, run
import os


env.hosts = ["34.224.6.206", "34.201.161.84"]


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
