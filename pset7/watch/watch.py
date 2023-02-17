import re
import sys


def main():
    # print(parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'))
    print(parse(input("HTML: ")))


def parse(s):
    try:
        src_attr = re.search(r'src="[^"]*youtube\.com[^"]*"', s).group()
        url = src_attr[src_attr.index('"') + 1:src_attr.rindex('"')]
        return re.sub(r'(http://|https://|https://www\.)youtube\.com/embed', r"https://youtu.be", url)
    except:
        return None

if __name__ == "__main__":
    main()

