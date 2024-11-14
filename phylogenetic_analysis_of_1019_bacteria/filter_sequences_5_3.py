# filter_sequences_5_3.py

def filter_sequences(input_filename, output_filename, conditions):
    print("Conditions for filtering:")
    print("Presence:")
    for part in conditions['presence']:
        print(part)
    print("Absence:")
    for part in conditions['absence']:
        print(part)
        
    num_output_sequences = 0 
    
    with open(input_filename) as fasta_file:
        sequences = fasta_file.read().split(">")[1:]
        with open(output_filename, "w") as output_file:
            for sequence in sequences:
                lines = sequence.split("\n")
                header = lines[0].split(' ', 1)[0]
                seq = "".join(lines[1:])
                
                if conditions['presence']:
                    presence_conditions_met = False
                    for group in conditions['presence']:
                        if all(seq[int(position) - 1] == amino_acid.upper() for position, amino_acid in group):
                            presence_conditions_met = True
                            break
                else:
                    presence_conditions_met = True 
                
                if conditions['absence']:
                    absence_conditions_met = all(
                        all(seq[int(position) - 1] != amino_acid.upper() for position, amino_acid in condition) 
                        for condition in conditions['absence']
                    )
                else:
                    absence_conditions_met = True 
                
                if presence_conditions_met and absence_conditions_met:
                    output_file.write(">" + header + "\n")
                    output_file.write(seq + "\n")
                    num_output_sequences += 1 

    return num_output_sequences 

def parse_conditions(condition_str):
    conditions = []
    if condition_str:
        groups = condition_str.split('or')
        for group in groups:
            conditions.append([tuple(condition.strip().split()) for condition in group.split('and')])
    return conditions

input_filename = input("Enter the input file name: ")

output_filename = input("Enter the output file name: ")

conditions_input = input("Enter conditions for presence (e.g., '43 K and 44 A or 45 B and 46 C'): ")
presence_conditions = parse_conditions(conditions_input)

absence_conditions_input = input("Enter conditions for absence (e.g., '73 K and 74 A or 75 B and 76 C'): ")
absence_conditions = parse_conditions(absence_conditions_input)

conditions = {'presence': presence_conditions, 'absence': absence_conditions}

num_output_sequences = filter_sequences(input_filename, output_filename, conditions)

print(f"Filtered sequences saved successfully in {output_filename}.")
print(f"Number of output sequences: {num_output_sequences}")
