#!/bin/bash

#source /your/conda.sh/location
source /home/candra/anaconda3/etc/profile.d/conda.sh

#conda activate yourenvirontmentname
conda activate flaskmvcv2

#uwsgi /your/site/configuration/file.ini
uwsgi /mnt/f/PythonProjects/FLASKMVC/V2/site.ini # > /dev/null 2>&1

#deactivate upon exist
conda deactivate

#endofcode
