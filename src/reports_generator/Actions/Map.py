from src.reports_generator.Actions.Action import Action
import numpy as np

class Map(Action):

    def __init__(self, action_struct, resources):
        self.functions = {"take": Map.take, "sum": Map.sum}
        self.name = 'map'

        self.key = action_struct['key']
        self.key_resource = resources[self.key['resource']]
        self.key_columns = self.key['columns']

        self.func = self.functions[action_struct.get('func', "take")]

        self.target = action_struct['target']
        self.tag = action_struct['tag']
        self.target_resource = resources[self.target["resource"]]
        self.target_keys = self.target['keys']
        self.target_columns = self.target['columns']

        # self.validify_mapping()

    def run(self, report_dict: dict):

        for row in self.key_resource.df.iterrows():
            for key, target_key in zip(self.key_columns, self.target_keys):
                target = self.target_resource.df[self.target_resource.df[target_key] == row[1][key]]
                for column, tag in zip(self.target_columns, self.tag):
                    report_dict.setdefault(tag, []).append(self.func(target, column))

        return report_dict

    def validify_mapping(self):
        if len(self.tag) != len(self.target_columns):
            raise IOError(f"Fields and tags are not of an equal length!!")
        Map.validify_columns(self.target_columns, self.target_resource)
        Map.validify_columns(self.target_keys, self.target_resource)
        Map.validify_columns(self.key_columns, self.key_resource)

    @staticmethod
    def validify_columns(cols, resource):
        if any([field not in list(resource.df.columns) for field in cols]):
            raise IOError(
                f"Not a valid action! check if {cols} are in your resource file")

    @staticmethod
    def take(values, column):
        value = 'N/A'
        if len(values) > 0:
            value = str([str(x) for x in list(values[column].values)]).strip('[]')
            if len(value) == 1:
                value = str(value[0]).strip('\'\'')
        return value

    @staticmethod
    def sum(values, column):
        value = 0
        if len(values) > 0:
            value = np.sum(values[column].values)
        return value
