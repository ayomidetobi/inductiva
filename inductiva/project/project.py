"""Project module"""

import json
from typing import Any, Dict, Optional
import os

import inductiva


class Project:
    """Project Class"""

    def __init__(self, name: str, tags: Optional[Dict[str, Any]] = None):
        self.name = name
        self.tags = tags
        self.tasks = {}
        self._working_dir = inductiva.get_output_dir() + "/" + name
        self._input_dir = self._working_dir + "/input"
        self._output_dir = self._working_dir + "/output"

        self.tags = tags or {}

        full_json = {"tags": self.tags}

        if not os.path.exists(self._input_dir):
            os.makedirs(self._input_dir)
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

        with open(self._working_dir + "/" + name + '.json',
                  'w',
                  encoding="utf-8") as file:
            json.dump(full_json, file)
            file.write('\n')
        print(f"Project {name} created")
        print(f"Working directory: {self._working_dir}")

    def get_metadata_file(self):
        """Returns the metadata file"""
        return self.name +"/"+self.name+ ".json"
