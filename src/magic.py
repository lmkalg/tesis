from argparse import ArgumentParser
from objdump_manager import ObjdumpManager

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f',dest='filename', help="The absolute path to the CSV file.")
    parser.add_argument('-d', '--debug', dest='debug', action="store_true", help="Flag to activate debugging mode")
    args = parser.parse_args()

    if not args.filename:
        parser.error("Objdump missing")

    ObjdumpManager(args.filename, args.debug)






