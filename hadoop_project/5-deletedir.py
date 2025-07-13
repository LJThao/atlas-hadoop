#!/usr/bin/python2.7
"""HDFS with Python (Snakebite) Module"""
from snakebite.client import Client


def deletedir(paths):
    """Function that removes the directories listed on l within HDFS"""
    client = Client('localhost', 9000)
    for path in sorted(paths, reverse=True):
        for entry in client.delete([path], recurse=True):
            print(entry)
