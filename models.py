"""Present models for near-Earth objects and their close approaches.
      
References:
https://knowledge.udacity.com/questions/668488
https://knowledge.udacity.com/questions/591920
https://knowledge.udacity.com/questions/475561
https://knowledge.udacity.com/questions/610693
https://knowledge.udacity.com/questions/636566
https://knowledge.udacity.com/questions/596642
https://knowledge.udacity.com/questions/613891
Tasks section of project brief
https://github.com/udacity/nd303-c1-advanced-python-techniques-project-starter/blob/master**
"""
    
from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """
    A near-Earth object (NEO) encapsulates semantic and physical parameters
    about the object that passed close to Earth, such as its primary designation
    (required, unique), IAU name (optional), diameter in kilometers
    (optional - sometimes unknown), and whether it's marked as potentially 
    hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches,
    initialized to an empty collection, but eventually populated in
    the `NEODatabase` constructor and has a reference to CloseApproach objects.
    """
    
    def __init__(self, **info):
        """Create a new `NearEarthObject`.
        :param info: A dictionary of excess keyword arguments supplied 
        to the constructor.
            
        Assigns values for attributes `designation`, `name`, `diameter`, 
        and `hazardous`.  Added code to account for nulls/missing values 
        for diameter but left name able to be unassigned.
        """
    
        """Create an empty initial collection of linked approaches."""
        self.approaches = []
        
        """ Only used info.get where I could afford a null/none.
        Left designation at info() because that's a unique identifier to 
        all entries"""
        self.designation = info['pdes']
        self.name = info.get('name') or None
        self.diameter = info.get('diameter')
        if info['diameter']:
            self.diameter = float(info['diameter'])
        else:
            self.diameter = float('nan')       
        self.hazardous = info['pha'] == 'Y'
  
    @property
    def fullname(self):
        """Return a representation of the full name of this NEO.
        Fullname is the designation of the NEO + any assigned name 
        from the dataset. 
        """
        return f'{self.designation}," ",({self.name})' if self.name else f'{self.designation}'
                                                                                                                                               
    def __str__(self):
        """Return `str(self)` for a human readable string with attribute information"""
        if self.hazardous == "Y":
            return f'Near Earth Object {self.fullname} has a diameter of {self.diameter:.3f} kms and is potentially hazardous.'
        else: 
            return f'Near Earth Object {self.fullname} has a diameter of {self.diameter:.3f} kms and is not potentially hazardous.'
        
    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object.
        """
        return (f'NearEarthObject(designation = {self.designation!r}, name = {self.name!r},'
                f'diameter = {self.diameter:.3f}, hazardous = {self.hazardous!r})'
        )      
    
    def serialize(self):
         """Adding serialize method to support task 4 per project task notes"""
         return {
             'designation' : self.designation,
             'name' : self.name,
             'diameter' : self.diameter,
             'hazardous' : self.hazardous
         }
       
        
class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    
    The `CloseApproach` class represents a close approach to Earth by an NEO.
    Each has an approach datetime, a nominal approach distance, and a relative 
    approach velocity.
    """
 
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self._designation = info['des']
        self.time = info.get('cd')
        if self.time:
           self.time = cd_to_datetime(self.time)
        self.distance = info.get('dist')
        if not self.distance:
            self.distance = float('nan')
        self.velocity = info.get('v_rel')
        if not self.velocity:
            self.veloicty = float('nan')  
        self.neo = None
        
    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`.  Used to create a human readable string
        with attribute information.
        """
        return f"At {self.time_str}, '{self._designation}' closely approached Earth \
        at a distance of {self.distance:.2f} au at a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize(self):
        """Adding serialize method to support task 4 per project task notes"""
        return {
            'datetime_utc': datetime_to_str(self.time),
            'distance_au': self.distance,
            'velocity_km/s': self.velocity
        }
 