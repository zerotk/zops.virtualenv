# -*- coding: utf-8 -*-
import glob
from contextlib import contextmanager
from tempfile import NamedTemporaryFile

import click


click.disable_unicode_literals_warning = True


@click.group('virtualenv')
def main():
    pass


@main.command()
@click.argument('name')
def create(name):
    """
    Create a virtualenv, caching when possible.
    """
