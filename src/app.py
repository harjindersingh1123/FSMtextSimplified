from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from textfsm_ext import TextFSMExt
#from flask_jwt import JWT, jwt_required

#jwt = JWT(authenticate, identity) # end point /auth
app = Flask('__name__')
api = Api(app)

import pdb

@app.route('/')
def home():
     return render_template('index.html')


class TextFSMDict(Resource):
    def post(self):
        cli  = request.form.get('input_data', None)
        template  = request.form.get('template_data', None)
        
        print(template)
        print(cli)

        ts = TextFSMExt()
        #out_data=ts.get_dict('sh_mem.txt', cli)
        out_data=ts.get_dict_from_str(template, cli)


        return (jsonify({'output': out_data}))

class TextFSMList(Resource):
    def post(self):
        cli  = request.form.get('input_data', None)
        template  = request.form.get('template_data', None)
        
        print(template)
        print(cli)

        ts = TextFSMExt()
        #out_data=ts.get_dict('sh_mem.txt', cli)
        out_data=ts.get_tup_from_str(template, cli)


        return (jsonify({'output': out_data}))

api.add_resource(TextFSMDict, '/dict')
api.add_resource(TextFSMList, '/list')

app.run(host='0.0.0.0', port = 5000, debug=True)
