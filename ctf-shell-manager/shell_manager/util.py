"""
Common utilities for the shell manager.
"""

from os import listdir, unlink, sep
from os.path import join, isdir, isfile

import shutil
from shutil import copytree, copy2

# the root of the hacksports local store
HACKSPORTS_ROOT = "/opt/hacksports/"
PROBLEM_ROOT = join(HACKSPORTS_ROOT, "sources")
STAGING_ROOT = join(HACKSPORTS_ROOT, "staging")
DEPLOYED_ROOT = join(HACKSPORTS_ROOT, "deployed")
BUNDLE_ROOT = join(HACKSPORTS_ROOT, "bundles")

#I will never understand why the shutil functions act
#the way they do...

def full_copy(source, destination, ignore=[]):
    for f in listdir(source):
        if f in ignore:
            continue
        source_item = join(source, f)
        destination_item = join(destination, f)

        if isdir(source_item):
            if not isdir(destination_item):
                copytree(source_item, destination_item)
        else:
            copy2(source_item, destination_item)

def move(source, destination, clobber=True):
    if sep in source:
        file_name = source.split(sep)[-1]
    else:
        file_name = source

    new_path = join(destination, file_name)
    if clobber and isfile(new_path):
        unlink(new_path)

    shutil.move(source, destination)
