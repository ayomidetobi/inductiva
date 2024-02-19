"""Project module"""

from typing import Any, Dict, Optional
import os

import inductiva


class Project:
    """Project Class"""

    def __init__(self, name: str, tags: Optional[Dict[str, Any]] = None):
        self.name = name
        self.tags = tags
        self._working_dir = inductiva.get_output_dir()+"/"+name
        self._input_dir = self._working_dir+"/input"
        self._output_dir = self._working_dir+"/output"
        
        if not os.path.exists(self._input_dir):
            os.makedirs(self._input_dir)
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

