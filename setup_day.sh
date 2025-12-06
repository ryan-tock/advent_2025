#!/bin/bash

DIR_NAME="day_${1}"
mkdir -p "${DIR_NAME}"
touch "${DIR_NAME}/input.txt"
touch "${DIR_NAME}/small.txt"
touch "${DIR_NAME}/test.txt"
touch "${DIR_NAME}/part1.py"
touch "${DIR_NAME}/part2.py"

cat <<EOF > "${DIR_NAME}/part1.py"
import utils
import time

data = utils.fetch_input(${1##0})
# data = utils.fetch_small(${1##0})
# data = utils.fetch_test(${1##0})
benchmark_start = time.time()

lines = data.splitlines()

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
EOF
