import re
import os

class Env(object):
    @classmethod
    def from_line(cls, line):
        pause_pattern = r"^(?P<pause># *)"
        path = re.sub(pause_pattern, "", line)
        split = path.split("/")
        name = split[4]
        paused = bool(re.match(pause_pattern, line))
        return cls(name, path, paused)

    def __init__(self, name, path, paused=False):
        self.name = name
        self.path = path
        self.paused = paused

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def to_string(self):
        return (self.paused * "# ") + self.path
