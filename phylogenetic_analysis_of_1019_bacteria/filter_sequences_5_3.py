# filter_sequences_5_3.py

def filter_sequences(input_filename, output_filename, conditions):
    print("Conditions for filtering:")
    print("Presence:")
    for part in conditions['presence']:
        print(part)
    print("Absence:")
    for part in conditions['absence']:
        print(part)
        
    num_output_sequences = 0  # Initialize counter for output sequences
    
    with open(input_filename) as fasta_file:
        sequences = fasta_file.read().split(">")[1:]
        with open(output_filename, "w") as output_file:
            for sequence in sequences:
                lines = sequence.split("\n")
                header = lines[0].split(' ', 1)[0]
                seq = "".join(lines[1:])
                
                # Check presence conditions if provided
                if conditions['presence']:
                    presence_conditions_met = False
                    for group in conditions['presence']:
                        if all(seq[int(position) - 1] == amino_acid.upper() for position, amino_acid in group):
                            presence_conditions_met = True
                            break
                else:
                    presence_conditions_met = True  # If no presence conditions provided, always met
                
                # Check absence conditions if provided
                if conditions['absence']:
                    absence_conditions_met = all(
                        all(seq[int(position) - 1] != amino_acid.upper() for position, amino_acid in condition) 
                        for condition in conditions['absence']
                    )
                else:
                    absence_conditions_met = True  # If no absence conditions provided, always met
                
                if presence_conditions_met and absence_conditions_met:
                    output_file.write(">" + header + "\n")
                    output_file.write(seq + "\n")
                    num_output_sequences += 1  # Increment counter for output sequences

    return num_output_sequences  # Return the number of output sequences

def parse_conditions(condition_str):
    conditions = []
    if condition_str:
        groups = condition_str.split('or')
        for group in groups:
            conditions.append([tuple(condition.strip().split()) for condition in group.split('and')])
    return conditions

# Input file name
input_filename = input("Enter the input file name: ")

# Output file name
output_filename = input("Enter the output file name: ")

# Specify conditions for presence
conditions_input = input("Enter conditions for presence (e.g., '43K and 44A or 45B and 46C'): ")
presence_conditions = parse_conditions(conditions_input)

# Specify conditions for absence
absence_conditions_input = input("Enter conditions for absence (e.g., '73K and 74A or 75B and 76C'): ")
absence_conditions = parse_conditions(absence_conditions_input)

conditions = {'presence': presence_conditions, 'absence': absence_conditions}

# Filter sequences and get the number of output sequences
num_output_sequences = filter_sequences(input_filename, output_filename, conditions)

print(f"Filtered sequences saved successfully in {output_filename}.")
print(f"Number of output sequences: {num_output_sequences}")
