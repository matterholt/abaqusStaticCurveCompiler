"""
FEA request: a PPT sent by a designer requesting Validation 2 group to perform 
a Finite Element Analysis. The request explains what has change in the model, what analysis,
and other data pertaining to the counter measure.

The problem that wish to solve is that the data that is collected is static, and is rarely
looked at. Creating a database would help create summaries and see trends from previous models

This is a simple program asking user to type in data from FEA request
- check and test need to be implemented, 
- main focus was to understand python classes and to get data from PPT to json or csv
"""
import csv
import json


class CmData:
    cm_data = "FEA Request"

    def __init__ (self, name, base_model, part_changes, model_description,
                analysis_jobs, model_weight, job_date):
        self.name = name
        self.base_model = base_model
        self.part_changes = part_changes
        self.model_description = model_description
        self.analysis_jobs = analysis_jobs
        self.model_weight = model_weight
        self.date = job_date

    def add_json(self):
        """
        Compile the data as a json. 
        GOAL is to create a html template for data
        TODO append to file to add the Results Data, PASS or FAIL
        """
        model = {
            "name" : self.name,
            "date" : self.date,
            "Fea Request" : {
                "base_model" : self.base_model,
                "part_change" : self.part_changes,
                "model_description" : self.model_description,
                "analysis_jobs" : self.analysis_jobs,
                "model_weight" : self.model_weight,
            }
        }

        file_name = "json_data//" + self.name + ".json"
        with open (file_name, "w" ) as model_data:
            json.dump(model, model_data, indent=4)


    def add_csv(self):
        """
        compile data to a csv file, Excel is the main program for data, need to be universal and
        allow every one to access data
        - this file is going a sort of database that will have all Fea Request data in columns
        similar to how data is shared currently
        """
        #data_head = ["model name", "base model", "parts change", "description", "analysis", "weight(kg)","date" ]
        data_results = [self.name, self.base_model, self.part_changes, self.model_description,
                        self.analysis_jobs, self.model_weight, self.date]
        with open ('FEA_Request_data.csv', 'a', newline ='') as tracker_file:
            cm_writer = csv.writer(tracker_file, lineterminator = "\n")
            # TODO create check to see if file exist or not
            #cm_writer.writerow(data_head) ### currently used for first run, 
            cm_writer.writerow(data_results)

def add_cm():
    """
    input data from terminal.
    basic and quick and dirty but does the job
    TODO need to add checks for inputs
    """
    model_name = input("CM model name V__R__: \n")
    model_base = input("base model name V__R__: \n")
    model_part_change = input("List any part need update: \n")
    model_description = input("quick description of Counter Measure: \n")
    model_analysis = input("List analysis wise to validate: \n")
    model_weight = input("kg weight of the Counter Measure:\n")
    job_date = input("Date of submittion (yy-dd-mm): \n")
    
    FeaR_data = CmData(model_name, model_base, model_part_change, model_description, model_analysis, model_weight, job_date)

    FeaR_data.add_json()
    FeaR_data.add_csv()

    print("Data has been saved .....")