from assembly_code import AssemblyCode


class AssemblyLine(object):
    """ Object to model a line code of assembly"""

    def __init__(self, addr, bytecode, code):
        self.addr = addr
        self.bytecode = bytecode.strip().split(' ')
        self.code = AssemblyCode(code)

    def get_address(self):
        return self.addr

    def get_code(self):
        return self.code

    def get_bytecode(self):
        return self.bytecode

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__, self.addr, self.code, self.bytecode)

    def __str__(self):
        return "Addr:{}, Code:{}, Bytecode:{} ".format(self.addr, self.code, self.bytecode)
