from src.reports_generator.PreAction.PreAction import PreAction
from src.reports_generator.Resource import Resource
from typing import Dict
import tkinter as tk
from tkinter import Tk, Button
global frame

class Filter(PreAction):
    def __init__(self, pre_action_struct):
        self.keys = pre_action_struct["keys"]
        self.resources = pre_action_struct["resources"]
        self.get_target(pre_action_struct["prompt"])
        self.targets = [self.target for _ in self.resources]

    def get_target(self, prompt):
        # Top level window
        frame = tk.Tk()
        frame.title(prompt)
        frame.geometry('400x200')

        inputtxt = tk.Text(frame,
                           height=5,
                           width=20)

        inputtxt.pack()
        def printInput():
            self.target = inputtxt.get(1.0, "end-1c")
            frame.destroy()
            return
        # Button Creation
        printButton = tk.Button(frame,
                                text="Ok",
                                command=printInput)
        printButton.pack()
        # Label Creation
        lbl = tk.Label(frame, text="")
        lbl.pack()
        frame.mainloop()


    def run(self, resources_dict: Dict[str, Resource]) -> Dict[str, Resource]:
        for resource_name, key, target in zip(self.resources, self.keys, self.targets):
            resource = resources_dict[resource_name]
            resource.df = resource.df[resource.df[key] == target]
            resources_dict[resource_name] = resource
        return resources_dict
