from CarbPhreeqcPy import IPhreeqc

p = IPhreeqc()
p.LoadDatabase(r'carbfix.dat')

p.RunString(
    """
    SOLUTION 1
    
    REACTION 1
    	NaCl 0.5
        CO2 0.1
    
    REACTION_TEMPERATURE
        30
    
    SELECTED_OUTPUT
      -reset false
      -pH true
      -high_precision true
    """
    )
    
print(p.GetSelectedOutputArray())
