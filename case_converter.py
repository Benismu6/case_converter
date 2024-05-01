
    
""" def convert_to_snake_case(pascal_or_camel_cased_string):
        snake_cased_char_list = []
        for char in pascal_or_camel_cased_string:
            if char.isupper():
                converted_character = '_' + char.lower()
                snake_cased_char_list.append(converted_character)
            else:
                snake_cased_char_list.append(char)
        snake_cased_string = ''.join(snake_cased_char_list)
        clean_snake_cased_string = snake_cased_string.strip('_')

        return clean_snake_cased_string """
    #NOTE; the above block of code does the same job as the comprehension list below


def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Converts a string from PascalCase or camelCase to snake_case.

    Args:
        pascal_or_camel_cased_string (str): The input string in PascalCase or camelCase.

    Returns:
        str: The input string converted to snake_case.
    """
    # Initialize an empty list to store characters
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Prepend underscore and convert to lowercase if character is uppercase
        else char  # Keep character unchanged if not uppercase
        for char in pascal_or_camel_cased_string  # Iterate through each character in the input string
    ]

    # Join the characters into a string and remove leading and trailing underscores
    return ''.join(snake_cased_char_list).strip('_')

def main():
    """
    Main function to demonstrate the conversion of a sample string.
    """
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()
