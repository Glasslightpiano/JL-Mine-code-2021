in_extent = '13504037.67475 2886377.84559, 13513808.55492 2891071.97427'

First_step = in_extent.replace(',', '')

Mlist = First_step.split(' ')

Algebra = Mlist[1]

Mlist[1] = Mlist[2]

Mlist.insert(2, Algebra)

del Mlist[3]

Correct_extent = ",".join(Mlist) + " [EPSG:3857]"

print(Correct_extent)