import textfsm
#import jtextfsm as textfsm
import sys

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
''

class TextFSMExt:
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
    def get_tup(self, template_file, cli_input):
        with open(template_file, 'r') as fd:
            fsm = textfsm.TextFSM(fd)
        fsm_results = fsm.ParseText(cli_input)
        return (fsm.header, fsm_results)


ts = TextFSMExt()
print(ts.get_dict('sh_mem.txt', input))
print(ts.get_tup('sh_mem.txt', input))


