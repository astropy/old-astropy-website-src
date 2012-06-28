#!/usr/bin/env python

import subprocess

from sys import exit
from os import path
from argparse import ArgumentParser
from shutil import rmtree


_instructions_description = """
This script will perform all the steps required to update the astropy
github page to reflect the current build of the repository this script is
executed from. This should thus only be run in the root directory of a
clone of the astropy-website repository.

To make this work correctly, a few things must be true:

* You must have git installed and on your path
* You must have a clone of the astropy github site present - the default
  assumes it's in the directory ../astropy.github.com, so this would mean
  having this clone of astropy-website in $SOMETHING/astropy-website and the
  clone of the github page in $SOMETHING/astropy.github.com.  You run this
  script, then, in $SOMETHING/astropy-website.
* You must have push rights to the astropy.github.com repo. Normally this
  means the astropy/astropy.github.com repo, and by default it assumes you
  are pushing to the "master" branch on the remote named "origin".  You can
  change this with options, but that's what git will do automatically if
  you clone directly from astropy/astropy.github.com.

"""[1:-1]


def safe_syscall(cmd):
    res = subprocess.call(cmd, shell=True)
    if res != 0:
        print 'Command line call failed! Exiting...'
        exit(res)


def continue_check(msg, defaultyes=True):
    yn = '[y]/n' if defaultyes else 'y/[n]'
    res = raw_input(msg + ' ' + yn + ':')
    if defaultyes and res == '' or res == 'y':
        return
    else:
        print 'You chose to quit... exiting!'
        exit(1)


def check_for_uncommited_changes():
    p = subprocess.Popen('git status -s -u no', shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if p.returncode != 0:
        print out
        print err
        print 'Couldn\'t get current repo\'s status! Exiting...'
        exit(-3)
    elif out == '':
        return False
    else:
        return out


def get_current_sha():
    p = subprocess.Popen('git rev-parse HEAD', shell=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        print out
        print err
        print 'Couldn\'t get current repo\'s SHA! Exiting...'
        exit(-3)
    else:
        return out.strip()


def remake_page():
    builddir = path.abspath('_build')
    if path.exists(builddir):
        continue_check('Wipe old _build dir {0}?'.format(builddir))
        rmtree(builddir)
    print 'Building new page'
    safe_syscall('make html')

    if not path.isdir(builddir):
        print 'Build could not be found in', builddir, 'Exiting...'
        exit(-5)


def copy_html_to_page_repo(repodir):
    htmldir = path.abspath('_build/html')
    syscall = 'cp {0} {1}'.format(path.join(htmldir, '*'), repodir)
    print 'Copying contents of', htmldir, 'to', repodir
    print syscall
    safe_syscall(syscall)


def commit_to_page_repo(repodir, apywebsha, updatereason=''):
    if updatereason:
        commitmsg = 'Updated for {0} \n(commit {1} in astropy-website)'.format(updatereason, apywebsha)
    else:
        commitmsg = 'Updated page \n(commit {0} in astropy-website)'.format(apywebsha)

    syscall1 = 'cd ' + repodir + ';git add *'
    syscall2 = 'cd ' + repodir + ';git commit -m "{0}"'.format(commitmsg)
    print 'Adding to page repo'
    safe_syscall(syscall1)
    print 'Comitting to page repo with message: "{0}"'.format(commitmsg)
    safe_syscall(syscall2)


def push_page_repo(repodir, remotename, branchname):
    continue_check('Want to push to page repo?')
    syscall = 'cd ' + repodir + ';git push {0} {1}'.format(remotename, branchname)
    safe_syscall(syscall)


if __name__ == '__main__':
    descr = _instructions_description[:_instructions_description.index('.')+1]
    ap = ArgumentParser(description=descr)
    ap.add_argument('-l','--long-help', default=False, dest='longhelp',
        help='Print the installation/usage instructions', action='store_true')
    ap.add_argument('--reason', '-r', default='',
        help='The reason for the commit (used in the commit message)')
    ap.add_argument('--repo-dir', '-d', default='../astropy.github.com',
        help='The directory holding the page itself (astropy.github.com)',
        dest='repo')
    ap.add_argument('--remote', '-e', default='origin',
        help='The name of the remote to push the final page repo to')
    ap.add_argument('--branch', '-b', default='master',
        help='The name of the branch to use on the page repo')
    ap.add_argument('--skip-rebuild-page', '-s', default=False,
        help='Skip the step of cleaning the current build of the page and '
        're-building it', dest='nobuild', action='store_true')

    args = ap.parse_args()

    if args.longhelp:
        print _instructions_description
        exit(0)

    repodir = path.abspath(args.repo)
    if not path.isdir(repodir):
        print 'Requested repository directory', repodir, 'is not a directory! Exiting...'
        exit(-1)
    elif not path.isdir(path.join(repodir, '.git')):
        print 'Requested repository', repodir, 'is not a git repo! Exiting...'
        exit(-2)

    apywebsha = get_current_sha()

    stat = check_for_uncommited_changes()
    if stat:
        print 'Uncommited changes found:'
        print stat
        print 'Exiting!'
        exit(-4)

    if not args.nobuild:
        remake_page()

    copy_html_to_page_repo(repodir)
    commit_to_page_repo(repodir, apywebsha, args.reason)
    push_page_repo(repodir, args.remote, args.branch)
