import os
import requests
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

class DataRepository:
    def __init__ (self,owner):
        self._owner = owner
        self._api_base_url = 'https://api.github.com'
        self._access_token = os.getenv("GITHUB_TOKEN")
        self._headers =  {'Authorization' : 'Bearer '+ self._access_token, 'X-GitHub-Api-Version' : '2022-11-28'}
    
    #3 etapas: Coleta -> transformação -> publicação?

    def list_repos (self):

        repos_list = []
        page = 1

        while True:
            try:

                url = f"{self._api_base_url}/users/{self._owner}/repos?page={page}"
                request = requests.get(url, headers=self._headers)

                if len(request.json()) == 0:
                    break 

                repos_list.append(request.json())
                page += 1

            except:

                repos_list.append(None)
        
        return repos_list
    
    @staticmethod
    def collect_content (repos_list, content):

        if not isinstance(content, str):
            raise TypeError("Content must be str!")
        
        repo_content_list = []

        for pages in repos_list:
            for repo in pages:
                repo_content_list.append(repo[content])
        
        return repo_content_list
    
    def create_data_frame (self):
        repos_list = self.list_repos()
        names_list = self.collect_content(repos_list, 'name')
        languages_list = self.collect_content(repos_list, 'language')

        repo_data = {

            'Repository Name' : names_list,
            'Language' : languages_list

        }

        data = pd.DataFrame(repo_data)

        return data


    
