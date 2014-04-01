import os
import re
from envplus.env import Env
from envplus.helpers import OrderedDict, get_site_packages_dir

linebreak_pattern = re.compile(r"[\n\r]")

class PathFile(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.envs = self.load()

    def read_pathfile(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath) as f:
                return f.read()
        else: return ""

    def load(self):
        raw = self.read_pathfile()
        lines = [ x.strip()
            for x in re.split(linebreak_pattern, raw)
            if x.strip() ]
        env_list = map(Env.from_line, lines)
        env_names = [ env.name for env in env_list ]
        envs = OrderedDict(zip(env_names, env_list))
        return envs

    def add_env(self, envname):
        sp_dir = get_site_packages_dir(envname)
        if not sp_dir:
            raise Exception("Could not find virtualenv named {}".format(envname))
        if envname in self.envs: del self.envs[envname] 
        local_sp = os.path.split(self.filepath)[0]
        rel = os.path.relpath(sp_dir, local_sp)
        self.envs[envname] = Env(envname, rel)

    def check_env(self, envname):
        if not envname in self.envs:
            raise Exception("No virtualenv named {}".format(envname))

    def remove_env(self, envname):
        self.check_env(envname)
        del self.envs[envname]

    def pause_env(self, envname):
        self.check_env(envname)
        self.envs[envname].pause()        

    def resume_env(self, envname):
        self.check_env(envname)
        self.envs[envname].resume()        

    def to_string(self):
        lines = [ env.to_string() for env in self.envs.values() ]
        joined = "\n".join(lines)
        return joined + "\n"

    def save(self):
        with open(self.filepath, "w") as f:
            content = self.to_string()
            f.write(content)

    def ls(self):
        return [ key for key,env in self.envs.items()
            if not env.paused ]

    def ls_paused(self):
        return [ key for key,env in self.envs.items()
            if env.paused ]

    def get_binpaths(self):
        workon = os.environ["WORKON_HOME"]
        tmpl = os.path.join("{0}", "{1}", "bin")
        def to_binpath(envname):
            return tmpl.format(workon, envname)
        return map(to_binpath, self.ls())
