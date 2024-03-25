from Bio import SeqIO

def extract_genome_info(gbff_file):
    genome_size = None
    gc_content = None
    num_genes = None

    with open(gbff_file, "r") as handle:
        records = SeqIO.parse(handle, "genbank")
        for record in records:
            # Extract genome size
            genome_size = len(record.seq)
            
            # Calculate GC content
            gc_count = sum(record.seq.count(base) for base in ["G", "C"])
            gc_content = (gc_count / len(record.seq)) * 100

            # Extract the number of genes
            num_genes = len([feature for feature in record.features if feature.type == "gene"])

            # Assuming the first record is sufficient; you can modify this if needed
            break

    return genome_size, gc_content, num_genes

# Read the list of GBFF file names from "1019_gbff_list.txt"
with open("1019_gbff_list.txt", "r") as gbff_list_file:
    gbff_file_names = gbff_list_file.read().splitlines()

# Initialize lists to store results
gcf_ids = []
genome_sizes = []
gc_contents = []
num_genes_list = []

# Iterate through the GBFF file names and extract genome info
for gbff_file_name in gbff_file_names:
    gcf_id = gbff_file_name.split("_")[0] + "_" + gbff_file_name.split("_")[1]  
    genome_size, gc_content, num_genes = extract_genome_info(gbff_file_name)
    
    # Append results to lists
    gcf_ids.append(gcf_id)
    genome_sizes.append(genome_size)
    gc_contents.append(gc_content)
    num_genes_list.append(num_genes)

# Write results to separate text files
with open("1019_genome_size.txt", "w") as genome_size_file:
    for gcf_id, size in zip(gcf_ids, genome_sizes):
        genome_size_file.write(f"{gcf_id},{size}\n")

with open("1019_gc_contents.txt", "w") as gc_content_file:
    for gcf_id, gc_content in zip(gcf_ids, gc_contents):
        gc_content_file.write(f"{gcf_id},{gc_content:.2f}%\n")

with open("1019_gene_number.txt", "w") as gene_number_file:
    for gcf_id, num_genes in zip(gcf_ids, num_genes_list):
        gene_number_file.write(f"{gcf_id},{num_genes}\n")

print("Results saved successfully.")
