from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)

rd = redis.Redis(host='localhost',port=6379,db=0, decode_responses=True)

#CREATE A POST ITEM 
@app.route('/items',methods=['POST'])

def create_item():
    data = request.json
    item_id = data.get('id')

    if not item_id:
        return jsonify({'error' : 'ID is required '}),400

    
    if rd.exists(data):
        return jsonify({'error': 'Data already exists'}),400
    
    #store the data item in redis as JSON string

    rd.set(item_id,json.dumps(data))
    return jsonify({'error':'Item created successfully'}),201


#READ THE ITEM BY (GET)

@app.route('/items/<item_id>',methods=['GET'])

def read_item(item_id):
    
    if not rd.exists(item_id):
        return jsonify({'error':'Could not found the data requested'}),404
    
    item = json.loads(rd.get(item_id))
    return jsonify(item),200


#UPDATE THE ITEM DATA (PUT)

@app.route('/items/<item_id>',methods=['GET'])

def update_item(item_id):
    
    if not rd.exists(item_id):
        return jsonify({'error':'Could not find the data searched'}), 404

    
    data = request.json

    rd.set(item_id,json.dumps(data))
    return jsonify({'message':'Data updated successfully'}),200


# Delete (DELETE) an item
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Check if the item exists
    if not rd.exists(item_id):
        return jsonify({'error': 'Item not found'}), 404

    # Delete the item from Redis
    rd.delete(item_id)
    return jsonify({'message': 'Item deleted successfully'}), 200



if __name__ == '__main__':
    app.run(debug=True)
