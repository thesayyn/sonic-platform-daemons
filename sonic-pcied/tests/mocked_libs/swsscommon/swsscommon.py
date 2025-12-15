'''
    Mock implementation of swsscommon package for unit testing
'''

STATE_DB = ''

# Table name constants
CFG_PORT_TABLE_NAME = 'PORT'
APP_PORT_TABLE_NAME = 'PORT_TABLE'
STATE_PORT_TABLE_NAME = 'PORT_TABLE'
STATE_HW_MUX_CABLE_TABLE_NAME = 'HW_MUX_CABLE_TABLE'

# Command constants
SET_COMMAND = 'SET'
DEL_COMMAND = 'DEL'


class Select:
    OBJECT = 1
    TIMEOUT = 2
    ERROR = 3

    def __init__(self):
        self.selectables = []

    def addSelectable(self, selectable):
        self.selectables.append(selectable)

    def removeSelectable(self, selectable):
        if selectable in self.selectables:
            self.selectables.remove(selectable)

    def select(self, timeout=-1):
        return (self.TIMEOUT, None)


def CastSelectableToRedisSelectObj(selectable):
    return selectable


class Table:
    def __init__(self, db, table_name):
        self.table_name = table_name
        self.mock_dict = {}

    def _del(self, key):
        del self.mock_dict[key]
        pass

    def set(self, key, fvs):
        self.mock_dict[key] = fvs.fv_dict
        pass

    def get(self, key):
        if key in self.mock_dict:
            return self.mock_dict[key]
        return None

    def get_size(self):
        return (len(self.mock_dict))

    def getKeys(self):
        return list(self.mock_dict.keys())


class FieldValuePairs:
    def __init__(self, tuple_list=None):
        self.fv_dict = {}
        if tuple_list and isinstance(tuple_list, list) and len(tuple_list) > 0 and isinstance(tuple_list[0], tuple):
            self.fv_dict = dict(tuple_list)

    def __setitem__(self, key, kv_tuple):
        self.fv_dict[kv_tuple[0]] = kv_tuple[1]

    def __getitem__(self, key):
        return self.fv_dict[key]

    def __len__(self):
        return len(self.fv_dict)

    def __iter__(self):
        return iter(self.fv_dict.items())

    def __eq__(self, other):
        if not isinstance(other, FieldValuePairs):
            return NotImplemented
        return self.fv_dict == other.fv_dict

    def __repr__(self):
        return repr(self.fv_dict)

    def __str__(self):
        return repr(self.fv_dict)


class WarmStart:
    def __init__(self):
        pass

    @staticmethod
    def initialize(name, db_id):
        pass

    @staticmethod
    def checkWarmStart(name, db_id):
        return False

    @staticmethod
    def isWarmStart():
        return False

    @staticmethod
    def isFastBoot():
        return False


class ConfigDBConnector:
    pass


class SonicDBConfig:
    pass


class SonicV2Connector:
    pass
