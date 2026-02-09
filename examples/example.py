from CarbPhreeqcPy import IPhreeqc

p = IPhreeqc()
p.LoadDatabase(r'carbfix.dat')

p.RunString(
    """
    SOLUTION 1 # 1 kg of pure water
    
    REACTION 1 # add the following substances (moles) to water
    	NaCl 0.5
        CO2 0.1
    
    REACTION_TEMPERATURE # increase temperature to 30 C
        30
    
    SELECTED_OUTPUT # Define which parameters are returned with "GetSelectedOutputArray"
      -reset false
      -pH true
      -saturation_indices Calcite
      -high_precision true
    """
    )
    
print(p.GetSelectedOutputArray())
