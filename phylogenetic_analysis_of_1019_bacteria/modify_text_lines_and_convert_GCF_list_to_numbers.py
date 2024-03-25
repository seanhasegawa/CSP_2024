# modify_text_lines_and_convert_GCF_list_to_numbers.py

def modify_text_lines_and_convert_GCF_list_to_numbers(input_file, output_file2):
    # Open the file for reading
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    # Process each line and extract the GCF ID
    gcf_counts = {}
    for line in lines:
        if line.startswith(">"):
            gcf_id = '_'.join(line.strip().split('_')[:2])  # Extract GCF ID from the line
            if gcf_id in gcf_counts:
                gcf_counts[gcf_id] += 1
            else:
                gcf_counts[gcf_id] = 1

    # Write the GCF IDs and their counts to a new file
    with open(output_file2, "w") as output_file:
        for gcf_id, count in gcf_counts.items():
            output_file.write(f"{gcf_id}, {count}\n")

    return gcf_counts

if __name__ == "__main__":
    input_file = input("The name of the input file: ")  # Replace with the actual path of your input file
    output_file2 = input("The name of the output file for GCF conversion: ")  # Replace with the desired path for the output file

    # Convert GCF list to GCF numbers
    gcf_counts = modify_text_lines_and_convert_GCF_list_to_numbers(input_file, output_file2)
    print(f"GCF list converted to GCF numbers saved successfully in {output_file2}.")

    # Print GCF IDs and their counts
    for gcf_id, count in gcf_counts.items():
        print(f"{gcf_id}, {count}")
