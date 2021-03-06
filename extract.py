"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.


References:
https://knowledge.udacity.com/questions/461587
https://knowledge.udacity.com/questions/668488
https://knowledge.udacity.com/questions/604931
https://knowledge.udacity.com/questions/536453
https://github.com/udacity/nd303-c1-advanced-python-techniques-project-starter/blob/master**
Tasks section of project brief
"""

import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    
    """
    neos = []
    
    with open(neo_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for neo in reader:
            neos.append(NearEarthObject(
                pdes = neo['pdes'],
                name = neo['name'],
                diameter = neo['diameter'],
                pha = neo['pha'],
            ))
  
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    
    with open(cad_json_path, 'r') as jinfile:
        reader = json.load(jinfile)
        for approach in reader['data']:
            approach = dict(zip(reader['fields'],approach))
            approaches.append(CloseApproach(
                des = approach['des'],
                cd = approach['cd'],
                dist = float(approach['dist']),
                v_rel = float(approach['v_rel']),
            ))
            
    return approaches
