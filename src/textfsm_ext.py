'''
class is extension to textFSM library. it adds up extra
functionality to textFSM to create dict or tuple of lists.    
'''
import textfsm
import sys
import io
import os
import pdb

class TextFSMExt:
    '''
    input:
       template_file: textFSM template file path
       cli_input: CLI  string
    return: dictionary of rows
    '''
    def get_dict(self, template_file, cli_input):
        res = []
        with open(template_file, 'r') as fd:
            fsm = textfsm.TextFSM(fd)
            fsm_results = fsm.ParseText(cli_input)
            for entry in fsm_results:
                dataDict = {}
                for idx, key in enumerate(fsm.header):
                    dataDict[key] = entry[idx]
                    res.append(dataDict)
        return (res)
    '''
    input:
       template_file: textFSM template str
       cli_input: CLI  string
    return: dictionary of rows
    '''

    def get_dict_from_str(self, template_str, cli_input):
        res = []
        #pdb.set_trace()
        with io.StringIO(template_str) as fd:
            fsm = textfsm.TextFSM(fd)
            fsm_results = fsm.ParseText(cli_input)
            for entry in fsm_results:
                dataDict = {}
                for idx, key in enumerate(fsm.header):
                    dataDict[key] = entry[idx]
                res.append(dataDict)
        return (res)
    '''
    input:
       template_file: textFSM template file path
       cli_input: CLI  string
    return: tuple of header(list), data rows(list) of rows
    '''

    def get_tup(self, template_file, cli_input):
        with open(template_file, 'r') as fd:
            fsm = textfsm.TextFSM(fd)
        fsm_results = fsm.ParseText(cli_input)
        return (fsm.header, fsm_results)
    '''
    input:
       template_file: textFSM template string
       cli_input: CLI  string
    return: tuple of header(list), data rows(list) of rows
    '''

    def get_tup_from_str(self, template_str, cli_input):

        with io.StringIO(template_str) as fd:
            fsm = textfsm.TextFSM(fd)
        fsm_results = fsm.ParseText(cli_input)
        return (fsm.header, fsm_results)

if __name__=="__main__":
    input = '''
Thu Jan 31 01:26:22.103 UTC
---- node0_4_CPU0 ----
Memory information:
    Physical Memory     : 5472.0   MB
    Free Memory         : 2716.882 MB
    Memory State        :   Normal
---- node0_RP1_CPU0 ----
Memory information:
    Physical Memory     : 18570.0   MB
    Free Memory         : 15869.667 MB
    Memory State        :   Normal
---- node0_RP0_CPU0 ----
Memory information:
    Physical Memory     : 18570.0   MB
    Free Memory         : 16039.164 MB
    Memory State        :   Normal
---- node0_6_CPU0 ----
Memory information:
    Physical Memory     : 5472.0   MB
    Free Memory         : 3386.253 MB
    Memory State        :   Normal
'''
    template = '''Value node (\S+)
Value physical_mem (\S+)
Value physical_mem_unit (MB|B|KB)
Value free_mem (\S+)
Value free_mem_unit (MB|B|KB)

Start
  ^\-+\s+${node}
  ^\s+Physical Memory\s+:\s+${physical_mem}\s+${physical_mem_unit}
  ^\s+Free Memory\s+:\s+${free_mem}\s+${free_mem_unit} -> Record
      '''
    ts = TextFSMExt()
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(fileDir, '../examples/template_sh_memory.txt')
    print ('DICT\n')
    print(ts.get_dict(path, input))
    print ('List\n')
    print(ts.get_tup(path, input))
    print ('DICT from str\n')
    print(ts.get_dict_from_str(template, input))

             
