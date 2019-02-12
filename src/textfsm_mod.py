import textfsm
#import jtextfsm as textfsm
import sys
import io

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
template = """Value Filldown date ((Mon|Tue|Wed|Thu|Fri|Sat|Sun).*)
Value Filldown node (\S+)

Start
  ^${date} 
  ^\-+\s+node${node} -> Record
      """


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
    def get_dict_from_str(self, template_str, cli_input):
        res = []
#        with open(template_file, 'r') as fd:
        with io.StringIO(template_str) as fd:
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

    def get_tup_from_str(self, template_str, cli_input):
        #with open(template_file, 'r') as fd:
        #    fsm = textfsm.TextFSM(fd)
        #fd = StringIO(template_str     )
        with io.StringIO(template_str) as fd:
            fsm = textfsm.TextFSM(fd)
        fsm_results = fsm.ParseText(cli_input)
        return (fsm.header, fsm_results)

if __name__=="__main__":
    ts = TextFSMExt()
    print(ts.get_dict('sh_mem.txt', input))
    print(ts.get_tup('sh_mem.txt', input))
    print(ts.get_dict_from_str(template, input))

             
