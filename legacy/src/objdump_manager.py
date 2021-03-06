import re
import pprint
import subprocess

from assembly_line import AssemblyLine
from regexes import TITLE_REGEX, SECTION_DISSASEMBLY_REGEX, SUBSECTION_REGEX, LINE_REGEX
from constants import SUBSECTION_NAME, SECTION_NAME, CONTENT, SECTION, SUBSECTION, TITLE, LINE


class ObjdumpManager(object):
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
                    dict_content[CONTENT][current_section][current_subsection].append(AssemblyLine(**line_info))
                
                elif match_subsection_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), SUBSECTION)) 
                    subsection_name = match_subsection_rx.groupdict()[SUBSECTION_NAME]
                    dict_content[CONTENT][current_section].update({subsection_name:[]})
                    current_subsection = subsection_name
                
                elif match_section_dissasembly_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), SECTION))
                    section_name = match_section_dissasembly_rx.groupdict()[SECTION_NAME]
                    dict_content[CONTENT].update({section_name:{}})
                    current_section = section_name

                elif match_title_rx:
                    if debug: content.append("{}--->{}".format(line.strip(), TITLE))    
                    dict_content = match_title_rx.groupdict()
                    dict_content.update({CONTENT:{}})
                else:
                    raise Exception("No regex to match this line: {}".format(line.strip()))

        
        return dict_content if not debug else content,dict_content

    def print_4_debug(self):
        pp = pprint.PrettyPrinter(indent=2)
        for line in self.content:
            print line

        print '\n\n\n\n'
        pp.pprint(self.dict_content)
        
