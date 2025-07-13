#!/usr/bin/python2.7
"""HDFS with Python (Snakebite): Create Module"""
from snakebite.client import Client


def createdir(l):
    """Function that creates the directories listed on l within HDFS"""
    client = Client('localhost', 9000)
    output = client.mkdir(l, create_parent=True)
    for entry in output:
        print(entry)
