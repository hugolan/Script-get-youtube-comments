#!/usr/bin/env python

from __future__ import print_function

import io
import json
import os
import sys
import time

import argparse
import lxml.html
import requests
from lxml.cssselect import CSSSelector


import pyspark
from pyspark import *

def wordAnalysis():
    conf = SparkConf()
    sc = SparkContext(conf)
    sqlContext = pyspark.SQLContext(sc)

    comments = sqlContext.read.json("comments.json")

    comments.show(5,False)
    rows = comments.count()
    print(rows)
    print("wordAnalysis over")


