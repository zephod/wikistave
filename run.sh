#!/bin/bash

while read line
do
    ./tool.py ug_song_urls_from_letter $line
done <targets

