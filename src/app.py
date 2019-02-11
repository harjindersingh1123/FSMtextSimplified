from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
#from flask_jwt import JWT, jwt_required

#jwt = JWT(authenticate, identity) # end point /auth
app = Flask('__name__')
api = Api(app)

import pdb

@app.route('/')
def home():
     return render_template('index.html')


class TextFSMDict(Resource):
    # @jwt_required()
    # def get(self, name):
    #     # for item in items:
    #     #     if item['name'] == name:
    #     #         return (item)
    #     item = next(filter(lambda x: x['name'] == name, items), None)
    #     return ({'item': item}, 200 if item else 404)

    def post(self):
        template  = request.args.get('template_data', None)
        cli  = request.args.get('input_data', None)
       # pdb.set_trace()
        print(template)
        print(cli)
        # if next(filter(lambda x: x['name'] == name, items), None):
        #     return({'message', ' item {} is already exists'.format(name)}, 400)
        # data = request.get_json()
        # item = {'name': name, 'price':data['price']}
        # items.append(item)
        return (jsonify({'template': template, 'cli_input': cli}))

api.add_resource(TextFSMDict, '/dict')
app.run(host='0.0.0.0', port = 5000, debug=True)
