import re

from constants import SECTION_NAME, SUBSECTION_NAME, TITLE, FILE_FORMAT, ADDR, BYTECODE, CODE

TITLE_REGEX = re.compile(r"^\s*(?P<{}>.*)\s*:\s*file\sformat\s*(?P<{}>.*$)".format(TITLE ,FILE_FORMAT), re.IGNORECASE)
SECTION_DISSASEMBLY_REGEX = re.compile(r"^\s*disassembly\s*of\s*section\s*(?P<{}>.*)\s*:$".format(SECTION_NAME), re.IGNORECASE)
SUBSECTION_REGEX = re.compile(r"^\s*[0-9a-f]*\s*\<(?P<{}>.*)\s*>\s*:$".format(SUBSECTION_NAME), re.IGNORECASE)
LINE_REGEX = re.compile(r"^\s*(?P<{}>[0-9a-f]*)\s*:\s*(?P<{}>([0-9a-f][0-9a-f]\s)*)\s*(?P<{}>.*)\s*$".format(ADDR,BYTECODE,CODE), re.IGNORECASE)
