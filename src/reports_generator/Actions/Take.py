from src.reports_generator.Actions.Action import Action


class Take(Action):
    def __init__(self, action_struct, resources):
        self.name = 'take'
        self.resource = resources[action_struct['resource']]
        self.tag = action_struct['tag']
        self.fields = action_struct['fields']
        self.query = action_struct['where']
        if len(self.tag) != len(self.fields):
            raise IOError(f"Fields and tags are not of an equal length!!")

    def filter_according_to_query(self):
        for condition in self.query:
            if condition == '==':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] == condition[2]]
            elif condition == '>=':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] >= condition[2]]
            elif condition == '=<':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] <= condition[2]]
            elif condition == '<':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] < condition[2]]
            elif condition == '>':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] > condition[2]]
            elif condition == '!=':
                self.resource.df = self.resource.df[self.resource.df[condition[0]] != condition[2]]

    def run(self, report_dict: dict):
        self.resource.df.fillna('N/A')
        self.filter_according_to_query()
        for field, tag in zip(self.fields, self.tag):
            report_dict[tag] = list(self.resource.df[field])
        return report_dict
