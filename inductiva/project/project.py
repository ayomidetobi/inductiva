"""Project module"""

import json
from typing import Any, Dict, Optional
import os

import inductiva


class Project:
    """Project Class"""

    def __init__(self, name: str, tags: Optional[Dict[str, Any]] = None):
        self.name = name
        self.name_metadata = name + ".json"
        self.tags = tags
        self.tasks = {}

        self.working_dir = inductiva.get_output_dir() + "/" + name
        self.input_dir = self.working_dir + "/input/"
        self.output_dir = self.working_dir + "/output/"

        self.metadata_dir = self.working_dir + "/" + name + '.json'

        self.tags = tags or {}

        full_json = {"tags": self.tags}

        if not os.path.exists(self.input_dir):
            os.makedirs(self.input_dir)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        with open(self.metadata_dir, 'w', encoding="utf-8") as file:
            json.dump(full_json, file)
            file.write('\n')
        print(f"Project {name} created")
        print(f"Working directory: {self.working_dir}")

    def __enter__(self):
        inductiva.set_active_project(self)
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        inductiva.set_active_project(None)

    def end_project(self):
        inductiva.set_active_project(None)

    def add_tag(self, key: str, value: Any):
        """Add a tag to the project"""
        #read tags from file, update tags with the new tag and write to file again
