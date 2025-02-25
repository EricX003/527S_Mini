import random

random_seed = "e.xing"

if random_seed == "WASHU_ID":
    print("Error. Please change the default WASHUID to your own.")
    exit(1)

random.seed(random_seed)

# Read the contents of the file
input_file_path = 'websites_list.txt'
output_file_path = 'random_websites.txt'


# Read all lines from the input file
with open(input_file_path, 'r') as file:
    websites = file.readlines()


# Select 100 random websites
random_websites = random.sample(websites, 100)


# Write the selected websites to the output file
with open(output_file_path, 'w') as file:
    file.writelines(random_websites)

print(f"Random selection of 100 websites saved to {output_file_path}")
