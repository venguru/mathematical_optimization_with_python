#!/bin/bash

docker run -it -v $(pwd):/home/project -w /home/project math_opt_python bash -c "pipenv run python $1"
