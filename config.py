import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://blockchain_user:pass@localhost:5432/blockchain_db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = os.getenv('12345', '12345')
  SESSION_COOKIE_NAME = 'blockchain_user_session'
