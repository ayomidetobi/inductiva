"""Project Manager Module"""

import json
import inductiva
import glob
import ast

from inductiva.project.project import Project

class ProjectManager:
    """Project Manager Class"""

    active_project = None

    def __init__(self):
        
        json_files = glob.glob(f"{inductiva.get_output_dir()}/*.json")
        print(json_files)

        self._all_projects = []

        for file in json_files:
            project_name = file.split("/")[-1].split(".")[0]

            with open(file, "r", encoding="utf-8") as f:
                line = f.readline()
                print(type(line))
                tags = json.loads(line)

            project = Project(project_name, tags)
            
            self._all_projects.append(project)

            print(self._all_projects)