from constants import EMPTY_INSTRUCTION, EMPTY_COMMENT, EMPTY_ARGS

class AssemblyCode(object):
    def __init__(self, code):
        """ Code comes as string """ 
        self._instruction = code.split(" ")[0].strip() or EMPTY_INSTRUCTION
        self._arguments = " ".join(code.split("#")[0].split(" ")[1:]).strip()
        self._arguments = map(str.strip,self._arguments.split(',')) if self.arguments else EMPTY_ARGS
        self._comments = " ".join(code.split("#")[1:]).strip() or EMPTY_COMMENT

    def __repr__(self):
        return "{}(Instr: {}, args: {}, comments: {} )".format(self.__class__.__name__, self._instruction, self._arguments, self._comments)

    @property
    def instruction(self):
        return self._instruction
    
    @property
    def arguments(self):
        return self._arguments
    
    @property
    def comments(self):
        return self._comments

