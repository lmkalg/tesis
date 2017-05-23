import re
import pprint
import subprocess

from assembly_line import AssemblyLine
from assembly_code import AssemblyCode
from regexes import TITLE_REGEX, SECTION_DISSASEMBLY_REGEX, SUBSECTION_REGEX, LINE_REGEX
from constants import (SUBSECTION_NAME, SECTION_NAME, SECTION, SUBSECTION, TITLE, LINE,STACK_FRAME_LINES_MODEL, RESERVED_AMOUNT_STACK_VARS_MODEL, 
                      EMPTY_INSTRUCTION, EMPTY_ARGS)


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
        for line_to_search in lines_to_search:
            for line_where_to_search_for in lines_where_to_search_for:
                same_instruction = (line_to_search.instruction == line_where_to_search_for.get_code().instruction) or (line_to_search.instruction == EMPTY_INSTRUCTION)
                same_args =  (line_to_search.arguments == line_where_to_search_for.get_code().arguments) or (line_to_search.arguments == EMPTY_ARGS)
                if (same_instruction and same_args):
                    # We must ensure now, that the rest are all together
                    line_to_search_index = lines_to_search.index(line_to_search)
                    line_where_to_search_for_index = lines_where_to_search_for.index(line_where_to_search_for)

                    lines_to_search_rest = lines_to_search[line_to_search_index+1:]
                    lines_where_to_search_for_rest = lines_where_to_search_for[line_where_to_search_for_index+1:]
                    
                    how_depth = len(lines_to_search_rest)
                    rest_is_equal = True
                    for i in xrange(how_depth):
                        same_instruction = (lines_to_search_rest[i].instruction == lines_where_to_search_for_rest[i].get_code().instruction) or (lines_to_search_rest[i].instruction == EMPTY_INSTRUCTION)
                        same_args =  (lines_to_search_rest[i].arguments == lines_where_to_search_for_rest[i].get_code().arguments) or (lines_to_search_rest[i].arguments == EMPTY_ARGS)
                        rest_is_equal &= (same_instruction and same_args)  
                        if not rest_is_equal:
                            rest_is_equal = False
                            break
                    if rest_is_equal:
                        return lines_where_to_search_for[line_where_to_search_for_index:line_where_to_search_for_index+how_depth+1]
                    else:
                        break
        return None

    def get_stack_frame(self, section=None, subsection=None):
        lines_to_search = [AssemblyCode(line) for line in STACK_FRAME_LINES_MODEL]
        return self.look_for_lines(lines_to_search, self.dict_content[section][subsection])


    def get_amount_of_place_reserved_for_stack_vars(self, section=None, subsection=None):
        lines_to_search = [AssemblyCode(line) for line in RESERVED_AMOUNT_STACK_VARS_MODEL]
        lines = self.look_for_lines(lines_to_search, self.dict_content[section][subsection])
        return lines[-1].get_code().arguments[-1]




