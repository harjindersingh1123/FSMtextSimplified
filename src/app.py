from flask import Flask, jsonify, render_template

app = Flask("__main__")


@app.route('/')
def home():
    return render_template('index.html')

#POST /fsm data:{name}
@app.route('/fsm', methods=['POST'])
def process_fsm():
    # req_data = request.get_json()
    # new_store = {
    #     'name': req_data['name'],
    #     'items' : []
    # }
    # stores.append(new_store)
    return(jsonify({'message': 'this is return message from FSMtext'}))

app.run(port=5000)
