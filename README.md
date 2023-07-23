# Text to Ankidroid Glossary Converter

This Python script converts a text file containing a glossary into a format suitable for [Ankidroid](https://apps.ankiweb.net/), a popular [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) flashcard app. The script reads the input text file where each line represents a word and its definition separated by a colon (':'), and then generates a CSV file for Ankidroid import.

## How to Use

1. Ensure you have Python installed on your system (Python 3.x recommended).

2. Clone this repository to your local machine or download the `txt_to_glossary.py` script.

3. Create a text file (`input_glossary.txt`) containing your glossary data in the following format:
```
Word1:Definition 1
Word2:Definition 2
Word3:Definition 3
...
```

4. Execute the Python script `txt_to_glossary.py` with the following command in the terminal or command prompt:

```Python
python txt_to_glossary.py
```
Make sure to replace `"input_glossary.txt"` with the path to your input text file.

5. The script will generate a CSV file (`output_glossary.csv`) with the glossary data in the correct format for Ankidroid import.

6. Import the generated CSV file into Ankidroid to create a deck with the words and definitions.

## Example

Suppose your `input_glossary.txt` file contains the following data:
```
Apple:A fruit that grows on trees and is often red or green.
Python:A high-level programming language known for its simplicity and readability.
GitHub:A web-based platform for version control and collaboration using Git.
```
After running the script, it will generate `output_glossary.csv` with the following content:
```
"Apple","A fruit that grows on trees and is often red or green."
"Python","A high-level programming language known for its simplicity and readability."
"GitHub","A web-based platform for version control and collaboration using Git."
```
You can then import `output_glossary.csv` into Ankidroid to create flashcards for each word and its definition.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this code as per the terms of the license.

## Contribution

If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

Happy learning and flashcard-ing with Ankidroid!
