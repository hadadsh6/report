import json
import pandas as pd
from pandas import DataFrame
import time
from src.reports_generator import Action, Take, Resource, Map
from typing import List, Dict, Any
from pathlib import Path

valid_actions = {"take": Take, "map": Map}  # , "search": Search]


class ReportsGenerator:
    def __init__(self, report_json_path: str = None, resources: List[Resource] = None):
        self.report: Dict[str, Any] = {}
        self.actions: List[Action] = []
        self.report_df: DataFrame = DataFrame()

        if report_json_path is None:
            raise IOError("What kind off report did you want to create?")

        report_json_path: Path = Path(report_json_path)
        with report_json_path.open('r', encoding='utf-8') as f:
            report_json = json.loads(f.read())

        self.resources: Dict[str, DataFrame] = {}
        for resource in resources:
            resource.fillna('N/A')
            self.resources[resource.name] = resource
        # self.resources['report'] = self.report_df

        self.validify_report_json(report_json)

    def validify_report_json(self, report_json):
        for action_json in report_json["Actions"]:
            if action_json["Name"] not in valid_actions:
                raise IOError(f"Not a valid action name! {action_json['Name']} is not valid!")
            action = valid_actions[action_json["Name"]]
            self.actions.append(action(action_json["Args"], self.resources))

    def run_actions(self):
        for action in self.actions:
            self.report = action.run(self.report)

    def create_report_excel(self) -> None:
        """

        :return:
        """

        self.run_actions()
        results_path = ReportsGenerator.get_path_to_put_results_in()
        self.report_df = DataFrame(self.report)
        self.report_df.to_excel(results_path)
        print(f"Successfully created results summary on: {results_path}")

    @staticmethod
    def get_path_to_put_results_in() -> Path:
        folder_path = input(
            "Please enter path to put summary excel on: (Example: C:\\Users\\USER\\Documents) \n>>")
        folder_path = folder_path.strip('"')
        folder_path = Path(folder_path)
        if not folder_path.exists():
            raise IOError("Folder doesn't exist!")
        if not folder_path.is_dir():
            raise IOError("Path isn't a folder!!")
        return folder_path.joinpath(Path(f"summary{time.asctime().replace(':', '_').replace(' ', '_')}.xlsx"))
