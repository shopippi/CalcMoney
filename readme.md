## Japanese Currency Conversion Program

## Overview
This program extracts numeric values from a given string and formats large numbers into an easily understood form.

## Function

### `format_large_number(number)`
This function formats a large number in an easy-to-understand format.
- Less than 10,000: Display as it is in units of "yen".
- 10,000 to 100 million: Divide by 10,000 and add the unit of "10,000,000 yen".
- More than 100 million: Divide by 100 million and add the unit of "100 million yen

### `parse_amount(text)`
Function to extract a numeric value from a given string.
- Remove commas and extract numbers using regular expressions

## Example.
```python
import re

def format_large_number(number):.
    ## example ```python import re

def parse_amount(text): # Omit...
    # Omit...

# Example: convert "1000 thousand yen" to number
input_text = "1000 thousand yen"
parsed_amount = parse_amount(input_text)

if parsed_amount is not None: if formatted_amount = format_amount = format_amount(input_text)
    formatted_amount = format_large_number(parsed_amount)
    print(formatted_amount)
else: if parsed_amount is not None
    print("Invalid input")
