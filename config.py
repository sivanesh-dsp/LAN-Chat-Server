import socket 
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    try:
        # Using Google's public DNS server as the destination
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception as e:
        local_ip = 'Unable to get IP Address'
        print(f"Error: {e}")

    TESTING = os.getenv('TESTING')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = local_ip
    ##print(socket.gethostbyname(socket.gethostname()))