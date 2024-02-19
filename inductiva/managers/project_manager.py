"""Project Manager Module"""

import json
from typing import Any, Dict, Optional
import inductiva
import glob
import ast

from inductiva.project.project import Project


class ProjectManager:
    """Project Manager Class"""

    active_project = None

    def __init__(self):
        # json_files = glob.glob(f"{inductiva.get_output_dir()}/*.json")
        # print(json_files)

        self._all_projects = []
        self.active_project = None

        # for file in json_files:
        #     project_name = file.split("/")[-1].split(".")[0]

        #     with open(file, "r", encoding="utf-8") as f:
        #         line = f.readline()
        #         print(type(line))
        #         tags = json.loads(line)

        #     project = Project(project_name, tags)

        #     self._all_projects.append(project)

        #     print(self._all_projects)

    def create_project(self,
                       name: str,
                       tags: Optional[Dict[str, Any]] = None,
                       make_active: bool = None):
        """Create a new project"""
        project = Project(name, tags)
        self._all_projects.append(project)
        if make_active:
            self.active_project = project
            print(f"Active project is now {project.name}")
        return project

    def set_active_project(self, project: Project):
        """Set the active project"""
        self.active_project = project
        if project:
            print(f"Active project is now {project.name}")
        else:
            print("Active project is now None")
