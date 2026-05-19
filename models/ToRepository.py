import os
import base64
import requests

from dotenv import load_dotenv
load_dotenv()

class ManipulateRepository:
    def __init__ (self, username):
        self._username = username
        self._api_base_url = 'https://api.github.com'
        self._access_token = os.getenv("GITHUB_TOKEN")

        if not self._access_token:
            raise ValueError("GITHUB_TOKEN not found!")

        self._headers =  {'Authorization' : 'Bearer '+ self._access_token, 'X-GitHub-Api-Version' : '2022-11-28', 'Accept': 'application/vnd.github+json'}

    def create_repo(self, repo_name):

        if not isinstance (repo_name, str):
            raise TypeError("repo_name must be str!")
        
        url = f'{self._api_base_url}/user/repos'
        data = {

            'name' : repo_name,
            'description' : "What is the most used language by some of the principals tech organizations",
            'private' : False

        }
        try:
            request = requests.post(url, json= data, headers=self._headers)

            request.raise_for_status()

            print(f"Repository was created successfully!")
  
        except requests.exceptions.RequestException as e:

            print(f"Error: {e}")
        

    @staticmethod
    def __to_base64 (path):

        if not isinstance (path, str):
            raise TypeError('path must be str!')
        
        try:

            with open (path, "rb") as file:
                file_content = file.read()
        
        except FileNotFoundError:

            print("File not found!")
            return None
        
        file_64 = base64.b64encode(file_content)

        return (file_64)
    
    def put_repo (self, repo_name, file_path, github_path):

        url = f"{self._api_base_url}/repos/{self._username}/{repo_name}/contents/{github_path}"
        
        content = self.__to_base64(file_path)

        if content is None:
            return

        content = content.decode('utf-8')

        data = {

            'message' : 'Success!',
            'content' : content

        }

        try:
            response = requests.put(url, json= data, headers= self._headers)

            response.raise_for_status()

            print("Committed Successfully!")

        except requests.exceptions.RequestException as e:

            print(f"Error: {e}")