#!/env/usr/bin python3

import hashlib
from os.path import exists
from xmlrpc.client import Boolean
import requests
import sys


def get_target(url: str) -> str:
    return requests.get(url).text


def get_digest(text: str) -> str:
    return hashlib.md5(bytes(text, "utf-8")).hexdigest()


def compare_digests(digest: str) -> Boolean:
    has_changed = False

    if exists("digest.out"):
        with open("digest.out", "r") as f:
            saved_digest = f.read()
        with open("digest.out", "w") as f:
            f.write(digest)

        has_changed = saved_digest == digest
    else:
        with open("digest.out", "w") as f:
            print("[!] No digest found. Writing initial...")
            f.write(digest)

    return has_changed


def main(target_url: str):
    res_text = get_target(target_url)
    digest = get_digest(res_text)

    if compare_digests(digest):
        print("No changes")
    else:
        print("Site has changed")
        # Notify bot maintainer


if __name__ == "__main__":
    main(sys.argv[1])
