from argparse import ArgumentParser
from disassembled_code import DisassembledCode
from constants import CODE_SECTION,MAIN_SUBSEC
from gdb_helper import GDBHelper

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f',dest='binary_filepath', help="The absolute path to the binary file.")
    parser.add_argument('-d', '--debug', dest='debug', action="store_true", help="Flag to activate debugging mode")
    args = parser.parse_args()

    if not args.binary_filepath:
        parser.error("Binary file path missing")

    disas_code = DisassembledCode(args.binary_filepath, args.debug)

    # Get Stack frame lines
    lines = disas_code.get_stack_frame(CODE_SECTION,MAIN_SUBSEC)
    stack_frame_end_address = lines[0][-1].get_address()
    print "Stack frame is created at: {}".format(stack_frame_end_address)

    #Get Amount of saved place in for stack vars
    amount_of_reserved =  disas_code.get_amount_of_place_reserved_for_stack_vars(CODE_SECTION,MAIN_SUBSEC)
    print "Amount of saved place for stack vars in main function: {}".format(amount_of_reserved)

    #Get amount of argv params
    amount_of_params = disas_code.get_amount_of_argv_args(amount_of_reserved, CODE_SECTION, MAIN_SUBSEC)
    print "Amount of params: {}".format(amount_of_params)

    #Get the value of RSP at the time of making the stack frame
    gdb_h = GDBHelper()
    value   = gdb_h.get_register_value_on_address("rsp", stack_frame_end_address, args.binary_filepath, 'asdd')
    print "Value of rsp/rbp inmediately after creating stack frame: {}".format(value)







