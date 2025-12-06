import os
from pathlib import Path
import browser_cookie3
import requests
from requests.cookies import RequestsCookieJar

def get_cookies():
    cookies = browser_cookie3.firefox()
    filtered = RequestsCookieJar()
    for c in cookies:
        if "adventofcode.com" in c.domain:
            filtered.set(c.name, c.value, domain=c.domain, path=c.path)

    return filtered

def fetch_input(day):
    day_str = "%02d" % (day,)
    day_path = os.path.join(Path(__file__).parent, f"day_{day_str}")
    input_file = open(os.path.join(day_path, "input.txt"), 'r')
    input_data = input_file.read()

    if input_data != "":
        return input_data

    filtered = get_cookies()
    url = f"https://adventofcode.com/2025/day/{day}/input"
    response = requests.get(url, cookies=filtered)

    data = "\n".join(response.text.split("\n")[:-1])
    input_file.close()
    input_file = open(os.path.join(day_path, "input.txt"), 'w')
    input_file.write(data)
    input_file.close()

    return data

def fetch_small(day):
    day_str = "%02d" % (day,)
    day_path = os.path.join(Path(__file__).parent, f"day_{day_str}")
    input_file = open(os.path.join(day_path, "small.txt"), 'r')
    input_data = input_file.read()

    if input_data != "":
        return input_data

    filtered = get_cookies()
    url = f"https://adventofcode.com/2025/day/{day}"
    response = requests.get(url, cookies=filtered)

    data = response.text.split("<pre><code>")[1].split("</code></pre>")[0]
    if data[-1] == "\n":
        data = data[:-1]
    input_file.close()
    input_file = open(os.path.join(day_path, "small.txt"), 'w')
    input_file.write(data)
    input_file.close()

    return data

def fetch_test(day):
    day_str = "%02d" % (day,)
    day_path = os.path.join(Path(__file__).parent, f"day_{day_str}")
    input_file = open(os.path.join(day_path, "input.txt"), 'r')
    input_data = input_file.read()
    input_file.close()

    return input_data

def get_neighbors(point, x_max, y_max):
    neighbors = [(point[0] + i, point[1] + j) for i in range(-1, 2) for j in range(-1, 2)]
    neighbors = [n for n in neighbors if n != point]
    neighbors = [n for n in neighbors if 0 <= n[0] < x_max and 0 <= n[1] < y_max]

    return neighbors