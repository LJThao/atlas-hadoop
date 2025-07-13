#!/usr/bin/python2.7
"""HDFS with Python (Snakebite): Download Module"""
from snakebite.client import Client


def download(paths):
    """Downloads HDFS files listed in 'paths' to the /tmp directory"""
    client = Client('localhost', 9000)
    output = client.copyToLocal(paths, '/tmp')
    for entry in output:
        print(entry)
