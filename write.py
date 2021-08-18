"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

References:
https://knowledge.udacity.com/questions/640052
Tasks section of project brief
https://github.com/udacity/nd303-c1-advanced-python-techniques-project-starter/blob/master**
https://stackoverflow.com/questions/20347766/pythonically-add-header-to-a-csv-file
"""

import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer = writer.writeheader()
        
        writer.writerow({
            for row in results:
            datetime_utc = datetime_to_str(row.time),
            distance_au = row.distance,
            velocity_km_s = row.velocity,
            designation = row._designation,
            name = row.neo.name,
            diameter_km = row.neo.diameter,
            potentially_hazardous = str(row.neo.hazardous)
        })
            

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    dict_list = list()
    
    for row in results:
        dict_list = {
            'datetime_utc': datetime_to_str(row.time),
            'distance_au': row.distance,
            'velocity_km_s': row.velocity,
            'neo': {
                'designation': row._designation,
                'name': row.neo.name,
                'diameter_km': row.neo.diameter,
                'potentially_hazardous': row.neo.hazardous
            }
        }
        dict_list.append(dict_list)
    
    with open(filename, 'w') as jfile:
        jfile_json.write(json.dumps(dict_list, indent='\t'))
        
