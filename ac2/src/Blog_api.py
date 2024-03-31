# blog.py
import requests

class Blog:
    def get(self):
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()
    
    def get_by_user_id(self, userId: str):
        e = f"https://jsonplaceholder.typicode.com/posts/{userId}"
        response = requests.get(e)
        return response.json()
    
    
    
