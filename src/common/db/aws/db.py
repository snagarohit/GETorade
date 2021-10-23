from pynamodb.models import Model
from pynamodb.attributes import JSONAttribute, UnicodeAttribute

import os

# Initialize this class in your logical "App" or "API"
# Example:
#   Initialize:
#       >>> app = App('MyAppName', 'Users/Verified')
#   # Here, 'MyAppName' is the project scope (generally API name / logical product name)
#           'Users/Verified' is a prefix for keys inside the project scope.
class App:
    app = None
    table = None

    def __init__(self, app, table) -> None:
        self.app = app
        self.table = table

# This works like a dictionary
# Example:
#   Initialize:
#       >>> verifiedUsers = SimpleDatabase(app)
#
#   Store data:
#       >>> verifiedUsers['foo@example.com'] = {'fName': "John", "lNmae": "Doe", "age": 34}
#   # Stored data is in table at "Users/Verified/foo@example.com" as "{'fName': "John", "lNmae": "Doe", "age": 34}"
#
#   Retrieve data:
#       >>> verifiedUsers['Verified/foo@example.com']
#       {'fName': "John", "lNmae": "Doe", "age": 34}
#
#   Delete data:
#       >>> del verifiedUsers['Verified/foo@example.com']
class SimpleDatabase:
    app = None

    def __getitem__(self, key):
        try:
            return next(__KVModel.query(self.app.app, __KVModel.key == self.app.table + "/" + key)).value
        except StopIteration:
            return None

    def __setitem__(self, key, value):
        __KVModel(self.app.app, key = self.app.table + "/" + key, value = value).save()

    def __delitem__(self, key):
        __KVModel(self.app.app, key = self.app.table + "/" + key).delete()

    def __init__(self, app: App) -> None:
        self.app = app


# Internal #
class __KVModel(Model):
    class Meta:
        table_name = os.environ['PB_DB_TABLE_NAME']
        region = os.environ['PB_DB_TABLE_REGION']

    namespace = UnicodeAttribute(hash_key = True)
    key = UnicodeAttribute(range_key = True)
    value = JSONAttribute()