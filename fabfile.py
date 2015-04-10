
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.project import rsync_project

env.gateway = 'linux-bastion.tudelft.nl'
env.user = 'hledoux'
env.hosts = ['3dgeoinfo.bk.tudelft.nl']


def deploy():
    local("jekyll build")
    local("tar -zcf w.tar.gz _site/")
    code_dir = '/var/www/people/hledoux'
    with cd(code_dir):
        run('rm -Rf site')
        put('w.tar.gz', code_dir)
        run("tar -xvf w.tar.gz")
        run("mv _site site")
        run("rm w.tar.gz")
    local("rm w.tar.gz")