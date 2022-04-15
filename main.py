#!/env/usr/bin python3

from cryptography.hazmat.primitives import hashes
import requests
import sys


def get_website(url: str) -> str:
    return requests.get(url).text


def get_digest(text: str) -> bytes:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(bytes(text, "utf-8"))
    return digest.finalize()


def main(url):
    source = get_website(url)
    digest = get_digest(source)
    print(digest)


if __name__ == "__main__":
    main(sys.argv[1])
