from argparse import ArgumentParser
from disassembled_code import DisassembledCode
from constants import CODE_SECTION,MAIN_SUBSEC


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f',dest='binary_filepath', help="The absolute path to the binary file.")
    parser.add_argument('-d', '--debug', dest='debug', action="store_true", help="Flag to activate debugging mode")
    args = parser.parse_args()

    if not args.binary_filepath:
        parser.error("Binary file path missing")

    disas_code = DisassembledCode(args.binary_filepath, args.debug)



    lines =  disas_code.get_stack_frame(CODE_SECTION,MAIN_SUBSEC)
    for line in lines:
        print line



    amount =  disas_code.get_amount_of_place_reserved_for_stack_vars(CODE_SECTION,MAIN_SUBSEC)
    print amount









