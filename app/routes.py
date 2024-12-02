from flask import Blueprint, request, jsonify
from app.models import Blockchain, Block

blockchain_bp = Blueprint('blockchain', __name__)

blockchain = None

def get_blockchain():
    global blockchain
    if blockchain is None:
        blockchain = Blockchain()
    return blockchain

@blockchain_bp.route('/chain', methods=['GET'])
def get_chain():
    blockchain = get_blockchain()
    chain = Block.query.all()
    chain_data = [{
        "index": block.index,
        "timestamp": block.timestamp,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "nonce": block.nonce,
        "hash": block.hash
    } for block in chain]
    return jsonify(chain_data), 200

@blockchain_bp.route('/mine', methods=['POST'])
def mine_block():
    blockchain = get_blockchain()
    data = request.json.get('data')
    if not data:
        return jsonify({'message': 'Data is required'}), 400
    blockchain.add_block(data)
    return jsonify({'message': 'Block added to the chain' },), 201
