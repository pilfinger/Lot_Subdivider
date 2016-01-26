import math

lotWidth = float(50)
frontSetback = float(15) 
subdivSetback = float(1)

def typeSelection(s):
	if s == 1:
		return 15
	elif s == 2:
		return 18
	elif s == 3:
		return 25
	elif s == 4:
		return 33
	else:
		return None

def determineUnits(z):
    if z == 2:
        duAcre = float(17.4)
    if z == 3:
        duAcre = float(30)
    if z == 4:
        duAcre = float(50)
        
    zoneConstraint = int((lotLength * lotWidth)*float(duAcre / 43560))
    realConstraint = int((lotLength - frontSetback) / minNarrowness)
    if realConstraint < zoneConstraint:
        return realConstraint
    else:
        return zoneConstraint

print "LOT:\n"
lotLength = input("Length of lot to be subdivided? ")

print "\nTYPOLOGY:\n"
print "1. Typology A"
print "2. Typology B"
print "3. Typology C"
print "4. Typology D\n"
minNarrowness = typeSelection(input("Which building layout is pursued? ")) + subdivSetback

print "\nZONING:\n"
print "2. R2"
print "3. R3"
print "4. R4\n"
unitCount = determineUnits(input("Which category is the lot zoned under? "))

subdivNarrowness = lotLength / unitCount
subdivArea = subdivNarrowness * lotWidth
frontLotArea = (subdivNarrowness + frontSetback) * lotWidth
totalFAR = float((unitCount * 500.00) / (lotLength * lotWidth) * 100.00)

print "\nThe lot yields %d subdivisions that are %f feet wide (%d sq. ft)," % ((unitCount - 1), subdivNarrowness, subdivArea)
print "in addition to 1 front subdivision that is %f feet wide (%d sq. ft)." % ((subdivNarrowness + 15), frontLotArea)

print "\nTotal FAR is %f" % totalFAR



