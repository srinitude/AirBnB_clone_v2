#!/usr/bin/python3
"""
Pack tarball and deploy to servers
"""
do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')


def deploy():
    """
    Pack tarball and deploy to servers
    """
    filepath = do_pack.do_pack()
    if not filepath:
        return False
    return do_deploy.do_deploy(filepath)
