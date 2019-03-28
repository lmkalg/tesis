import re
import pprint
import subprocess

from assembly_line import AssemblyLine
from assembly_code import AssemblyCode
from regexes import TITLE_REGEX, SECTION_DISSASEMBLY_REGEX, SUBSECTION_REGEX, LINE_REGEX
from constants import (SUBSECTION_NAME, SECTION_NAME, SECTION, SUBSECTION, TITLE, LINE,STACK_FRAME_LINES_MODEL, RESERVED_AMOUNT_STACK_VARS_MODEL, 
                      EMPTY_INSTRUCTION, EMPTY_ARGS, GET_PARAMS_ARGV_MODEL)


class DisassembledCode(object):
    """ Object Dump wrapper"""

    def __init__(self, bin_filepath, debug=False):

        self.raw_content = subprocess.check_output(["objdump","-M","intel","-d", bin_filepath]).split('\n')

        if debug:
            self.content, self.dict_content = self.parse_objdump_file(self.raw_content, debug)
            self.print_4_debug()
        else:
            self.dict_content = self.parse_objdump_file(self.raw_content, debug)

    @staticmethod
    def parse_objdump_file(raw_content, debug):
        content = []
        dict_content = {}
        current_section = ''
        current_subsection = ''

        for line in raw_content:
            if len(line.strip()) != 0:
                #Match regexes
                match_line_rx = re.match(LINE_REGEX,line) 
                match_subsection_rx = re.match(SUBSECTION_REGEX,line) 
                match_section_dissasembly_rx = re.match(SECTION_DISSASEMBLY_REGEX,line) 
                match_title_rx = re.match(TITLE_REGEX,line) 
                if match_line_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), LINE)) 
                    line_info = match_line_rx.groupdict()
                    dict_content[current_section][current_subsection].append(AssemblyLine(**line_info))
                
                elif match_subsection_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), SUBSECTION)) 
                    subsection_name = match_subsection_rx.groupdict()[SUBSECTION_NAME]
                    dict_content[current_section].update({subsection_name:[]})
                    current_subsection = subsection_name
                
                elif match_section_dissasembly_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), SECTION))
                    section_name = match_section_dissasembly_rx.groupdict()[SECTION_NAME]
                    dict_content.update({section_name:{}})
                    current_section = section_name

                elif match_title_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), TITLE))    
                    dict_content = match_title_rx.groupdict()
                else:
                    raise Exception("No regex to match this line: {}".format(line.strip()))

        
        return dict_content if not debug else (content,dict_content)

    def print_4_debug(self):
        pp = pprint.PrettyPrinter(indent=2)
        for line in self.content:
            print line

        print '\n\n\n\n'
        pp.pprint(self.dict_content)
        


    def get_n_lines_of_section_subsection(self, section, subsection, n):
        return self.dict_content[section][subsection][:n]

    @staticmethod
    def look_for_lines(lines_to_search, lines_where_to_search_for):
        def included_in(arg, list_args):
            for _arg in list_args:
                if arg in _arg:
                    return True
            return False

        res = []
        for line_where_to_search_for in lines_where_to_search_for:
            first_line = lines_to_search[0]
            same_instruction = (first_line.instruction == line_where_to_search_for.get_code().instruction) or (first_line.instruction == EMPTY_INSTRUCTION)
            # same_args =  (first_line.arguments == line_where_to_search_for.get_code().arguments) or (first_line.arguments == EMPTY_ARGS)
            args_are_included = all(included_in(arg,line_where_to_search_for.get_code().arguments) for arg in first_line.arguments) or (first_line.arguments == EMPTY_ARGS)
            if (same_instruction and args_are_included ): #same_args):
                # We must ensure now, that the rest are all together
                line_where_to_search_for_index = lines_where_to_search_for.index(line_where_to_search_for)
                lines_where_to_search_for_rest = lines_where_to_search_for[line_where_to_search_for_index+1:]
                
                how_depth = len(lines_to_search) - 1
                rest_is_equal = True
                for i in xrange(how_depth):
                    same_instruction = (lines_to_search[i+1].instruction == lines_where_to_search_for_rest[i].get_code().instruction) or (lines_to_search[i+1].instruction == EMPTY_INSTRUCTION)
                    # same_args =  (lines_to_search[i].arguments == lines_where_to_search_for_rest[i].get_code().arguments) or (lines_to_search[i].arguments == EMPTY_ARGS)
                    args_are_included = all(included_in(arg,lines_where_to_search_for_rest[i].get_code().arguments) for arg in (lines_to_search[i+1].arguments)) or   (lines_to_search[i+1].arguments == EMPTY_ARGS)

                    rest_is_equal &= (same_instruction and args_are_included)  
                    if not rest_is_equal:
                        rest_is_equal = False
                        break
                if rest_is_equal:
                    res.append(lines_where_to_search_for[line_where_to_search_for_index:line_where_to_search_for_index+how_depth+1])
        return res

    def get_stack_frame(self, section=None, subsection=None):
        lines_to_search = [AssemblyCode(line) for line in STACK_FRAME_LINES_MODEL]
        return self.look_for_lines(lines_to_search, self.dict_content[section][subsection])


    def get_amount_of_place_reserved_for_stack_vars(self, section=None, subsection=None):
        lines_to_search = [AssemblyCode(line) for line in RESERVED_AMOUNT_STACK_VARS_MODEL]
        lines = self.look_for_lines(lines_to_search, self.dict_content[section][subsection])
        return lines[0][-1].get_code().arguments[-1]


    def get_amount_of_argv_args(self, amount_reserved, section=None, subsection=None):
        lines_to_search = [AssemblyCode(line.format(amount_reserved)) for line in GET_PARAMS_ARGV_MODEL]
        results = self.look_for_lines(lines_to_search, self.dict_content[section][subsection])
        argv_offsets = set()
        for lines in results:
            for line in lines:
                if line.get_code().instruction == 'add':
                    arg_offset = filter(lambda x: x != 'rax', line.get_code().arguments)[0]
                    argv_offsets.add(arg_offset)
        return len(argv_offsets)







