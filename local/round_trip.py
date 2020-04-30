import sys

import ruamel.yaml as yaml
import argparse
from pathlib import Path

from regolith.fsclient import dump_yaml

THIS_DIR = Path('.')
collsdir = THIS_DIR / ".." / ".." / "rg-db-public" / "db"


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--collections", nargs='+',
                        help="collections or collections to round-trip "
                             "e.g., -c people contacts expenses")
    args = parser.parse_args()
    return args


def main():
    args = parser()
    if not args.collections:
        sys.exit("please specify a collection, or list of collections, using "
                 "the -c switch, e.g., -c people contacts expenses")
    if isinstance(args.collections, str):
        collections = [args.collections]
    else:
        collections = args.collections
    needed_dbs = collections

    for coll in needed_dbs:
        fullcoll = coll + ".yml"
        collfile = collsdir / fullcoll
        with open(collfile, "r", encoding='utf8') as i:
            current = yaml.safe_load(i)
        sync_coll(collfile, current)
        print("{} has been roundtripped".format(coll))


def sync_coll(collfile, dict):
    with open(collfile, "r", encoding='utf8') as i:
        current = yaml.safe_load(i)
    current.update(dict)
    for k, v in current.items():
        v.update({"_id": k})
    dump_yaml(collfile, current)


if __name__ == '__main__':
    main()
