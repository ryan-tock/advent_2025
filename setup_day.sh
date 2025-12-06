#!/bin/bash

DIR_NAME="day_${1}"
mkdir -p "${DIR_NAME}"
touch "${DIR_NAME}/input.txt"
touch "${DIR_NAME}/small.txt"
touch "${DIR_NAME}/test.txt"
touch "${DIR_NAME}/part1.py"
touch "${DIR_NAME}/part2.py"

cat <<'EOF' > "${DIR_NAME}/part1.py"
import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
EOF
