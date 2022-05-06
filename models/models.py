import collections.abc
import copy
import pickle

DB = {
    "api": {
        "site": {
        }
    }
}


def update(dictionary, data):
    for k, v in data.items():
        if isinstance(v, collections.abc.Mapping):
            dictionary[k] = update(dictionary.get(k, {}), v)
        else:
            dictionary[k] = v
    return dictionary


class SimpleDB:

    def __init__(self, dump_file_name="db"):
        self.dump_file_name = dump_file_name
        self.schema = DB
        self.DB = copy.deepcopy(self.schema)
        self.root = self.__root_unwrapper()

    def __root_unwrapper(self):
        root = None
        for k in self.DB.keys():
            root = k
        return root

    def update_data(self, data):
        return update(self.DB, data)

    def dump(self):
        f = open(self.dump_file_name, "wb")
        pickle.dump(self, f)
        f.close()

    @classmethod
    def load(cls, dump_path):
        obj = pickle.load(dump_path)
        obj.self.dump_file_name = dump_path
        return obj
