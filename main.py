import math
# import Decimal

# Consider using Decimal() instead of float()

# lotWidth = float(50)
# frontSetback = float(15) 
# subdivSetback = float(1)

LOT_WIDTH = Decimal(50)
FRONT_SETBACK = Decimal(15)
SUBDIV_SETBACK = Decimal(1)

def typeSelection(s, selections):
	_s = s.lower()
	return Decimal(selections.get(_s, None))

def determineUnits(du_acre, lot_length, min_narrowness):
	# this is good to make sure
	# you get the right type in
	_du_acre = Decimal(du_acre) 
	
        zoneConstraint = Decimal(_du_acre / 43560) * (lot_length * LOT_WIDTH)
        realConstraint = (lot_length - FRONT_SETBACK) / Decimal(min_narrowness)
        
        return zoneConstraint, realConstraint
	
class Lot(object):
	def __init__(self, lot_length, typ_selection, z_selection):
		self.lot_length = lot_length
		self.typ_selection = typ_selection
		self.z_selection = z_seleciton
		
		self.min_narrowness = self.get_min_narrowness()
		self.unit_count = self.get_unit_count(z_selection)
	
	def get_min_narrowness(self):
		min_narrowness = typeSelection(self.typ_selection, 
						{'a': 15, 'b': 18, 
						'c': 25, 'd': 33}) 
		return min_narrowness + SUBDIV_SETBACK
		
	def get_unit_count(self, selection):
		du_acre = typeSelection(selection,
				{'r2': 17.4, 'r3': 30, 'r4': 50}) 
			
		# returns tuple, we want smaller one	
		return min(determineUnits(du_acre, self.lot_length, self.min_narrowness))
	
	def tabulate_geometric_contrains(self):
		subdiv_narrowness = self.lot_length / self.unit_count
		subdiv_area = subdiv_narrowness * LOT_WIDTH
		front_lot_area = (subdiv_narrowness + FRONT_SETBACK) * LOT_WIDTH
		total_FAR = float((self.unit_count * 500.00) / (self.lot_length * LOT_WIDTH) * 100.00)
		
		return subdiv_narrowness, subdiv_area, front_lot_area, total_far

if __name__ == "__main__":
	print "LOT:"
	lot_length = input("Length of lot to be subdivided? ")

	print ""
	print "TYPOLOGY: "
	print "Typology A"
	print "Typology B"
	print "Typology C"
	print "Typology D"
	typ_selection = input("Which building layout is pursued? ")

	print "ZONING:"
	print "R2"
	print "R3"
	print "R4"
	z_selection = input("Which category is the lot zoned under? ")

	lot = Lot(lot_length, typ_selection, z_selection)
	subdiv_narrowness, subdiv_area, front_lot_area, total_FAR = lot.tabulate_geometric_contrains()

	print "The lot yields {0} subdivisions that are {1} feet wide ({2} sq. ft),"\
			.format((lot.unit_count - 1), subdiv_narrowness, subdiv_area)
			
	print "in addition to {0} front subdivision that is {1} feet wide ({2} sq. ft)."\
			.format((subdiv_narrowness + 15), front_lot_area)

	print ""
	print "Total FAR is %f" % total_FAR



