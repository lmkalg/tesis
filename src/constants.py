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


#GDB 
TEMP_GDB_SCRIPT = '/tmp/.gdb_script'
TEMP_GDB_OUTPUT = '/tmp/.gdb_out'

# Shellcodes
SHELLCODE_27 = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'



# Lines models
STACK_FRAME_LINES_MODEL = ['push rbp','mov rbp, rsp']
RESERVED_AMOUNT_STACK_VARS_MODEL = ['push rbp','mov rbp, rsp', 'sub']
# STACK_FRAME_LINES = ['push rbp']


