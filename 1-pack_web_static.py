#!/usr/bin/python3
"""
Packages up web static files into a tarball
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Packages up web static files into a tarball
    """
    date_fmt = "%Y%m%d%H%M%S"
    today = datetime.now().strftime(date_fmt)
    if not os.path.isdir("versions"):
        os.makedirs("versions")
    file = "versions/web_static_{}.tgz".format(today)
    try:
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None
