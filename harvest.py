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
    
melon_type_dictionary = make_melon_type_lookup(melon_list)

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
    

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # harvested_melons = []
    #instantiate all melons 
    #self, melon_type, shape_rating, color_rating, harvested_field, harvested_by)
    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')

    #return a list of objects of class Melon
    return [melon_1, melon_2, melon_3, melon_4, melon_5,
            melon_6, melon_7, melon_8, melon_9]

harvested_melons = make_melons(melon_type_dictionary)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    #print info on each melon, sellable or not.
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvested_by} from " 
                      f"Field {melon.harvested_field} (CAN BE SOLD)")
        else: 
            print(f"Harvested by {melon.harvested_by} from "
                      f"Field {melon.harvested_field} (NOT SELLABLE)")


get_sellability_report(harvested_melons)

