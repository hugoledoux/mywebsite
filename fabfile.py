
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.project import rsync_project

env.gateway = 'linux-bastion.tudelft.nl'
env.user = 'hledoux'
env.hosts = ['3dgeoinfo.bk.tudelft.nl']


def deploy():
    local("jekyll build")
    code_dir = '/var/www/people/hledoux'
    with cd(code_dir):
        run('rm -Rf site')
        put('_site', code_dir)
        run("mv _site site")