import os
from os import path
import subprocess
import re
from contextlib import contextmanager
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

DEFAULT_ROOT = path.expanduser('~/dev')  # TODO, be able to change
GITHUB_RE = re.compile(
    '(?P<protocol>(?:(?:(?:http|https)://|git@))?)(github.com)(:|/)'
    '(?P<owner>\w+)(/)(?P<repo>\w+)(.git)?')

root = DEFAULT_ROOT


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.version_option()
def cli(ctx):
    """Manage development repositories.
    """
    # Do `list` command by default
    if ctx.invoked_subcommand is None:
        ctx.invoke(list)


@cli.command()
def list():
    """List the current repositories."""
    print(tree(root, 2))


def tree(directory, depth, _first=True):
    lines = [pretty_path(directory)] if _first else [path.basename(directory)]

    paths = sorted(os.listdir(directory), key=lambda s: s.lower())
    for idx, inner in enumerate(paths):
        last = idx == len(paths) - 1
        outsep = '└── ' if last else '├── '
        innsep = '    ' if last else '│   '
        pathfull = path.join(directory, inner)
        if path.isdir(pathfull) and depth > 1:
            first = True
            for line in tree(pathfull, depth-1, False).splitlines():
                lines.append((outsep if first else innsep) + line)
                first = False
        else:
            lines.append(outsep + inner)
    return '\n'.join(lines)


def pretty_path(p):
    return p.replace(path.expanduser('~'), '~')


@cli.command()
@click.argument('url')
def clone(url):
    """Clone a new url into the repositories."""
    match = GITHUB_RE.match(url)
    if match:
        clone_like_github(match.group('owner'), match.group('repo'))


def clone_like_github(owner, repo, site='github.com'):
    clone_url = f'git@{site}:{owner}/{repo}.git'
    local_user = f'{owner}@{site}'
    os.makedirs(path.join(root, local_user), exist_ok=True)
    with pushd(path.join(root, local_user)):
        subprocess.check_call(['git', 'clone', clone_url])
    os.chdir(path.join(root, local_user, repo))


@contextmanager
def pushd(new_dir):
    """https://gist.github.com/howardhamilton/537e13179489d6896dd3"""
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


@cli.command()
def test():
    """Run program tests."""
    eg_url = [
        'https://github.com/ashgillman/systems',
        'http://github.com/ashgillman/systems',
        'github.com/ashgillman/systems',
        'git@github.com:ashgillman/systems.git',
        'https://github.com/ashgillman/systems.git',
    ]
    for url in eg_url:
        match = GITHUB_RE.match(url)
        if not (match
                and match.group('owner') == 'ashgillman'
                and match.group('repo') == 'systems'):
            raise RuntimeError('Failed on {}'.format(url))
