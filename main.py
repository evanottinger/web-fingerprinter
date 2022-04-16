#!/env/usr/bin python3

import hashlib
import requests
import sys


def get_target(url: str) -> str:
    return requests.get(url).text


def get_digest(text: str) -> str:
    return hashlib.md5(bytes(text, "utf-8")).hexdigest()


def main(target_url):
    res_text = get_target(target_url)
    digest = get_digest(res_text)
    print(digest)


if __name__ == "__main__":
    main(sys.argv[1])
