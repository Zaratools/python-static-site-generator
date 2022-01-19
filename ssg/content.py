import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        (_, fm, content) = self.__regex.split(string, 2)
        load(fm, FullLoader)
        return cls(metadata, content)


class Content:
    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

        @property
        def body(self):
            return self.data["content"]

        @property
        def type(self):
            if "type" in self.data:
                return self.data["type"]
            else:
                return None

        @type.setter
        def type(self, value):
            self.data["type"] = value

        def __getitem__(self, key):
            return self.data[key]

        def __iter__(self):
            return self.data.iterator

        def __len__(self):
            return self.data.length

        def __repr__(self):
            data = {}
            for (key, value) in self.data.items():
                if key != "content":
                    data[key] = value
            return str(data)
