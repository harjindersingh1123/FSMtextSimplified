import textfsm
import sys
import io

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

        with io.StringIO(template_str) as fd:
            fsm = textfsm.TextFSM(fd)
        fsm_results = fsm.ParseText(cli_input)
        return (fsm.header, fsm_results)

if __name__=="__main__":
    ts = TextFSMExt()
    print(ts.get_dict('sh_mem.txt', input))
    print(ts.get_tup('sh_mem.txt', input))
    print(ts.get_dict_from_str(template, input))

             
