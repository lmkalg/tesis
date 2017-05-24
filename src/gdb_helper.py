import subprocess
import os

from constants import TEMP_GDB_SCRIPT, TEMP_GDB_OUTPUT

class GDBHelper(object):

    def _add_to_script(self, new_instruction):
        self.script +=  '\n' + new_instruction

    def _set_break_in_addr(self, addr):
        self._add_to_script("b *0x{}".format(addr))

    def _get_value_of_register(self, reg):
        self._add_to_script("i r {}".format(reg))

    def _run(self):
        self._add_to_script("r")

    def _turn_on_logging(self):
        self._add_to_script("set logging file {}\nset logging on".format(TEMP_GDB_OUTPUT))

    def _turn_off_logging(self):
        self._add_to_script("set logging off")

    def _write_down_script(self):
        self._add_to_script("quit")
        with open(TEMP_GDB_SCRIPT, 'w') as f:
            f.write(self.script)

    def _execute_gdb(self, binary_path, args):
        fnull = open(os.devnull, 'w')
        res = subprocess.call(["gdb","-x",TEMP_GDB_SCRIPT, binary_path], stdout=fnull)
        fnull.close()
        if res == 0:
            return
        else:
            raise Exception("Error when trying to start gdb. \n\n {} ".format(res))

    def _clean_temp_files(self):
        try:
            os.remove(TEMP_GDB_OUTPUT)
            os.remove(TEMP_GDB_SCRIPT)
        except Exception:
            pass

    def get_register_value_on_address(self, reg, addr, binary_file, args):

        def _parse_output():
            with open(TEMP_GDB_OUTPUT,'r') as f:
                content = f.read()
            self._clean_temp_files()

            #UGLY, very UGLY
            idx_from = content.index('x')-1
            idx_to = content[idx_from:].index('\t') + idx_from
            return content[idx_from:idx_to+1]

        self.script = ""
        self._set_break_in_addr(addr)
        self._run()
        self._turn_on_logging()
        self._get_value_of_register(reg)
        self._turn_off_logging()

        self._write_down_script()
        self._execute_gdb(binary_file, args)
        return _parse_output()







