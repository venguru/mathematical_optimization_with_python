#!/bin/bash

port=$1
docker run -it --rm -p $port:8000 -v $(pwd):/home/project -w /home/project math_opt_python bash -c "pipenv run jupyter lab --allow-root --ip 0.0.0.0 --port 8000"

