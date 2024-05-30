import requests

class ExampleAPIHandler:
    def __init__(self, **kwargs):
        self.args = kwargs
        self.api_key = self.args.get('api_key')

    def get_data(self, endpoint):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f'https://api.example.com/{endpoint}', headers=headers)
        response.raise_for_status()
        return response.json()
