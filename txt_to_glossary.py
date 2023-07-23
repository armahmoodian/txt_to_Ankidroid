import csv


def txt_to_glossary(input_file, output_file):
    glossary_data = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            word, definition = line.strip().split(':')
            definition = definition.replace('\n', '')  # Remove newline characters from the definition
            glossary_data.append([word.strip(), definition.strip()])

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # Use csv.QUOTE_ALL option
        # writer.writerow(['Word', 'Definition'])
        writer.writerows(glossary_data)


if __name__ == "__main__":
    input_file_path = "input_glossary.txt"  # Replace with the path to your input text file
    output_file_path = "output_glossary.csv"  # The CSV file for Ankidroid

    txt_to_glossary(input_file_path, output_file_path)
    print("Conversion complete. Glossary saved to", output_file_path)