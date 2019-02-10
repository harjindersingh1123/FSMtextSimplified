from flask import Flask, jsonify, request, render_template

app = Flask("__main__")


@app.route('/')
def home():
	return render_template('index.html')

#POST /fsm data:{name}
@app.route('/fsm', methods=['POST'])
# req_data = request.get_json()
# new_store = {
#     'name': req_data['name'],
#     'items' : []
# }
# stores.append(new_store)
def process_fsm():
	req_data = request.get_json()
	#new_store = { 'name': req_data['input_data'],  'template': req_data['template_data'] }
	print("Testing.........")#req_data)
	#value1= req_data.get('input_data')
	print( 'input'+ str(request.form.get('input_data')))
	print( 'template' + str(request.form.get('template_data')))
	return jsonify({'message': 'this is return message from FSMtext again:'+str(req_data)})

app.run(host='0.0.0.0', port = 5000, debug=True)
