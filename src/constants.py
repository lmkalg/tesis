## Regexes
SECTION_NAME = 'section_name'
SUBSECTION_NAME = 'subsection_name'
ADDR = 'addr' #Binded to vars name in AssemblyLine object
BYTECODE = 'bytecode' #Binded to vars name in AssemblyLine object
CODE = 'code' #Binded to vars name in AssemblyLine object
FILE_FORMAT = 'file_format'
TITLE = "title"

# Debugging
SUBSECTION = "subsection"
SECTION = "section"
TITLE = "title" 
LINE = "line"

# Sections
CODE_SECTION = ".text"
DATA_SECTION = ".data"
PLT_SECTION = ".plt"
RODATA_SECTION = ".rodata"


# Subsections
MAIN_SUBSEC = "main"


# Misc2
EMPTY_INSTRUCTION = "EMPTY"
EMPTY_COMMENT =  "EMPTY"
EMPTY_ARGS =  "EMPTY"





# Lines models
STACK_FRAME_LINES_MODEL = ['push rbp','mov rbp, rsp']
RESERVED_AMOUNT_STACK_VARS_MODEL = ['push rbp','mov rbp, rsp', 'sub']
# STACK_FRAME_LINES = ['push rbp']


