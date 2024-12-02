from time import time
import hashlib
import json
from app import db

class Block(db.Model):
    __tablename__ = 'blocks'
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Float, nullable=False)
    data = db.Column(db.Text, nullable=False)
    previous_hash = db.Column(db.String(64), nullable=False)
    nonce = db.Column(db.Integer, nullable=False)
    hash = db.Column(db.String(64), nullable=False)

    def __init__(self, index, timestamp, data, previous_hash, nonce=0, hash_value=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = hash_value or self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty = 2

    def __init__(self):
        if not Block.query.all():
            self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time(), "Genesis Block", "0")
        db.session.add(genesis_block)
        db.session.commit()

    def add_block(self, data):
        previous_block = Block.query.order_by(Block.index.desc()).first()
        new_block = Block(len(Block.query.all()), time(), data, previous_block.hash)
        new_block = self.proof_of_work(new_block)
        db.session.add(new_block)
        db.session.commit()

    def proof_of_work(self, block):
        block.nonce = 0
        while not block.hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block
