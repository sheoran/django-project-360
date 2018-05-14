#!/usr/bin/env python3
import os

import plumbum

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(BASE_DIR)
    docker_compose = plumbum.local['docker-compose']
    (plumbum.local["{0}/bin/env_generator.py".format(BASE_DIR)]) & plumbum.FG
    (docker_compose['build']) & plumbum.FG
    (docker_compose['up', '-d', 'db']) & plumbum.FG
    (docker_compose['up', '-d', 'web']) & plumbum.FG
