############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color 
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        return f'<MelonType code={self.code}>'

    def add_pairing(self, pairings):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairings)
        print(self.pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(self.code)

def make_melon_types():
    """Returns a list of current melon types."""

    # all_melon_types = []

    #instatiate the class MelonType 
    #call add_pairing to add pairings to instance 
    muskmelon = MelonType('musk', '1998', 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing(['mint'])

    casaba = MelonType('cas', '2003', 'orange', False, None, 'Casaba')
    casaba.add_pairing(['strawberry', 'mint'])

    crenshaw = MelonType('cren', '1996', 'green', False, None, 'Crenshaw')
    crenshaw.add_pairing(['proscuitto'])

    yellow_watermelon = MelonType('yw',
                                  '2013',
                                  'yellow',
                                  False, 
                                  True,
                                  'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])

    #return a list of objects of MelonType
    # all_melon_types.extend((muskmelon, casaba, crenshaw, yellow_watermelon))
    
    return [muskmelon, casaba, crenshaw, yellow_watermelon]

melon_list = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')

        for pairs in melon.pairings:
            print(f'-{pairs}')
        

print_pairing_info(melon_list)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    #create a dictionary - keys = codes, values = melon type instance for code
    #('yw', yellow_watermelon)
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon_dict.get(melon.code,melon)

    return melon_dict
    
print(make_melon_type_lookup(melon_list))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, 
                 harvested_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by

    def is_sellable(self):
    #Sellable vs Non-sellable (Behavior)
    # if shape and color rating > 5 AND not from field 3 
        if ((self.shape_rating > 5) 
            and (self.color_rating > 5) 
            and (self.harvested_field != 3)):  #then sellable 
           return True 
        
        return False  #else not sellable 
    
melon_1 = Melon('yw', 7, 10, 3, 'Shelia')
print(melon_1.is_sellable())

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



