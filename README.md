## **Introduction**

This repository contains three Python scripts developed for the analyses in Hasegawa, Inose, *et al., RNA,* 2024. Detailed instructions for each script are provided below.

## **Scripts Overview**

1. Extracting Genome Size, GC Content, and Gene Count from GenBank Files
   - Script: `Genome_size_analysis/extract_genome_info_2.py`
   - Function: This script extracts genome size, GC content, and gene count from GenBank Flat Files (GBFF) and saves the results in separate text files.
   
2. Filtering FASTA Sequences with Amino Acid Presence/Absence
   - Script: `phylogenetic_analysis_of_1019_bacteria/filter_sequences_5_3.py`
   - Function: This script filters sequences from a multiple sequence alignment (MSA) in FASTA format based on specified amino acid presence/absence conditions at specific alignment positions.
   
3. GCF ID Converter and Counter
   - Script: `phylogenetic_analysis_of_1019_bacteria/modify_text_lines_and_convert_GCF_list_to_numbers.py`
   - Function: This script processes a text file containing GCF IDs, extracts unique GCF IDs, counts their occurrences, and outputs the results in a summary file.

For further details, including features, usage instructions, and requirements, please refer to the individual sections for each script.

## **Extracting Genome Size, GC Content, and Gene Count from GenBank Files**

`Genome_size_analysis/extract_genome_info_2.py` extracts genome information from GenBank Flat Files (GBFF), including genome size, GC content, and the number of genes, and outputs the results into separate text files.

### **Features**

1. Parses each GBFF file listed in `1019_gbff_list.txt` to compute:
   - Genome Size: Total number of base pairs in the genome sequence.
   - GC Content: Percentage of bases that are either Guanine (G) or Cytosine (C).
   - Gene Count: Total number of genes annotated in the genome.
  
2. Output Files:
   - `1019_genome_size.txt`: Contains each genome’s identifier (GCF ID) and size.
   - `1019_gc_contents.txt`: Contains each genome’s GCF ID and GC content.
   - `1019_gene_number.txt`: Contains each genome’s GCF ID and gene count.

### **Usage**

1. Download the required GBFF files and place them in your working directory.
2. Prepare a list of GBFF file names in `1019_gbff_list.txt`. 
Note: An example input file might look like: `Genome_size_analysis/1019_gbff_list.txt`
3. Run the script.
4. Find the extracted data in the generated text files.

### **Requirements**

 - Python (3.9.7 or later)
 - Biopython (1.78 or later)

### **Reference**

This script uses the SeqIO module from Biopython (https://biopython.org/wiki/SeqIO) for parsing GenBank files.

## **Filtering FASTA Sequences with Amino Acid Presence/Absence**

`phylogenetic_analysis_of_1019_bacteria/filter_sequences_5_3.py` filters sequences from a multiple sequence alignment (MSA) in FASTA format based on specified amino acid conditions. It allows users to specify amino acid requirements at certain alignment positions, with the option to enforce the presence or absence of these amino acids within sequences.

### **Features**

1. This script filters sequences based on:
   - Presence Conditions: Defines amino acids that must be present at specific alignment positions within the sequence. 
   - Absence Conditions: Defines amino acids that must not appear at specified alignment positions.

2. Output files and details:
   - Sequences meeting the conditions are saved in an output FASTA file.
   - Displays the number of sequences that meet the filtering criteria.

### **Usage**

1. Input and output files:
   - Provide the name of the input FASTA file when prompted. *Note: The input file must be aligned using MSA to ensure positions are consistent across sequences. An example input file might look like:
`phylogenetic_analysis_of_1019_bacteria/mafft-linsi_2440_CSP_seq.fasta`*
   - Specify the name of the output file where filtered sequences will be saved.

4. Specify conditions:
   - Presence Conditions (optional): Specify the amino acids and positions that should be present in the sequence. Use `and` to combine conditions within a group and `or` to separate groups, e.g., `43 K and 44 A or 45 B and 46 C`. *Note: Be sure to put a space between the position of the aligned sequence and the amino acid residue.*
   - Absence Conditions (optional): Specify the amino acids and positions that should not be present, using the same format as presence conditions, e.g., `73 K and 74 A or 75 B and 76 C`.

5. Run the script:
   - When you run the script, you’ll be prompted to enter the input file name, output file name, and filtering conditions.
   - Filtered sequences will be saved in the specified output file, and the number of sequences meeting the criteria will be displayed.

### **Requirements**

   - Python (3.9.7 or later)

### **Example**

   - If the input file `test2input.fasta` contains the following sequences:

```plaintext
>GCF_000203835.1_WP_003978336.1 cold-shock protein [Streptomyces coelicolor A3(2)]
-M------------------------ASGTVKWFNSEKGFGFIAQDG--GGPDVFAHYSN
INAQG--YREL-QEGQAVTFDITQG-QKGPQAE--NITP-A-------------------
----------------
>GCF_000006965.1_WP_003537120.1 cold-shock protein [Sinorhizobium meliloti]
-M------------------------NSGTVKWFNSTKGFGFIQPDD--GATDVFVHASA
VERAG--MRSL-VEGQKVTYDIVRD-TKSGKSSADNLRA-A-------------------
----------------
>GCF_000005845.2_NP_415156.1 511145|Escherichia coli str. K-12 substr. MG1655|transcription antiterminator and regulator of RNA stability CspE
------------------MS-----KIKGNVKWFNESKGFGFITPED--GSKDVFVHFSA
IQTNG--FKTL-AEGQRVEFEITNG-AKGPSAA--NVIA-L-------------------
----------------
>GCF_000005845.2_NP_415401.1 511145|Escherichia coli str. K-12 substr. MG1655|DNA replication inhibitor CspD
-M------------------------EKGTVKWFNNAKGFGFICPEG--GGEDIFAHYST
IQMDG--YRTL-KAGQSVQFDVHQG-PKGNHAS--VIVP-V-E-VEA-AVA---------
----------------
>GCF_000005845.2_NP_415509.1 511145|Escherichia coli str. K-12 substr. MG1655|CspA family protein CspH
-M----------------SR-----KMTGIVKTFDRKSGKGFIIPSD--GRKEVQVHISA
FTPRD--AEVL-IPGLRVEFCRVNG-LRGPTAA--NVYL-S-------------------
----------------
```

   - Given the following filtering conditions:

```plaintext
Enter the input file name: test2input.fasta
Enter the output file name: test2output.fasta
Enter conditions for presence (e.g., '43K and 44A or 45B and 46C'): 2 M and 27 A or 2 M and 27 N
Enter conditions for absence (e.g., '73K and 74A or 75B and 76C'): 2 A
```

   - The script will display:

```plaintext
Conditions for filtering:
Presence:
[('2', 'M'), ('27', 'A')]
[('2', 'M'), ('27', 'N')]
Absence:
[('2', 'A')]
Filtered sequences saved successfully in test2output.fasta.
Number of output sequences: 2
```

  - The output file will contain:

```plaintext
>GCF_000203835.1_WP_003978336.1
-M------------------------ASGTVKWFNSEKGFGFIAQDG--GGPDVFAHYSNINAQG--YREL-QEGQAVTFDITQG-QKGPQAE--NITP-A-----------------------------------
>GCF_000006965.1_WP_003537120.1
-M------------------------NSGTVKWFNSTKGFGFIQPDD--GATDVFVHASAVERAG--MRSL-VEGQKVTYDIVRD-TKSGKSSADNLRA-A-----------------------------------
```

## **GCF ID Converter and Counter**

`phylogenetic_analysis_of_1019_bacteria/modify_text_lines_and_convert_GCF_list_to_numbers.py` processes a text file containing lines with GCF IDs and converts them into a list of unique GCF IDs along with the count of each ID’s occurrences. 

### **Features**

1. GCF ID extraction:
   - The script reads each line of the input file and identifies lines beginning with `>`.
   - It extracts the GCF ID (first two segments of each line) and counts the occurrences of each unique GCF ID.

2. Output file:
   - The processed GCF IDs and their counts are saved in the specified output file in the format: `GCF_ID, count`.

### **Usage**

1. Input and output files:
   - Provide the name of the input file when prompted. Each line in this file should contain GCF IDs in the format `>GCF_XXXXXX_...`.
   - Specify the name of the output file where the counted GCF IDs will be saved.

2. Run the script:
   - Enter the input and output file names as prompted.
   - The script will process the input, count occurrences of each unique GCF ID, and save the results in the output file.

3. Output details:
   - The output file will contain each unique GCF ID along with its count in the format `>GCF_ID, count`.
   - The script will also display each GCF ID and its count in the console.

### **Requirements**

   - Python (3.9.7 or later)

### **Example**

   - If the input file contains the following lines:

```plaintext
>GCF_000001
>GCF_000002
>GCF_000001
>GCF_000003
>GCF_000001
>GCF_000002
```

   - The output file will contain:

```plaintext
>GCF_000001, 3
>GCF_000002, 2
>GCF_000003, 1
```
