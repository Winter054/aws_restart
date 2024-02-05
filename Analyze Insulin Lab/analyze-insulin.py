'''
Human insulin is a 51-amino acid peptide hormone with a molecular weight of 5808 Da (Dalton is an atomic mass unit). 
It is composed of an A-chain (21 amino acids) and a B-chain (30 amino acids), which are linked by two disulfide bonds.
'''
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin ="malwmrllpllallalwgpdpaaa"
bInsulin ="fvnqhlcgshlvealylvcgergffytpkt"
aInsulin ="giveqcctsicslyqlenycn"
cInsulin ="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
# print(insulin)

'''Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)
print("The sequence of human insulin, chain a: " + aInsulin)
'''

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) molecular weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acids (use lambda function to count for aawt in each aa)
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})
# print(aaCountInsulin)

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))


molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

'''For improvements I have to use more precise aawt with more decimal, or use Biopython library. This will make less error%'''