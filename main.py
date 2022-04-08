#!/usr/bin/env python

from getYoutubeLink import inputYoutubeLink
from commentAnalysis import wordAnalysis


def main():
    print("yo what up")
    link = inputYoutubeLink()
    print(link)
    print("preceding to read comments")
    wordAnalysis()
    print("comments were read with success")    
main()
print("success")