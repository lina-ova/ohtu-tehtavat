from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        
        parsed_content=toml.loads(content, _dict=dict)
        needed_info=parsed_content['tool']['poetry']

        name=needed_info['name']
        description=needed_info['description']
        dependencies=list(needed_info['dependencies'])
        dev_dep=list(needed_info['dev-dependencies'])


        #deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dep)
