import os

def modify_file_content(filename, new_filename):
    """
    Reads a file, modifies its content, and writes the modified content to a new file.
    Handles potential errors during file operations.

    Args:
        filename (str): The name of the file to read.
        new_filename (str): The name of the file to write the modified content to.

    Returns:
        bool: True if the file was successfully read and written, False otherwise.
    """
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.readlines()  # Read the file content into a list of lines

        # Modify the content (example: add line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        # Attempt to open the new file in write mode
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)  # Write the modified content to the new file

        print(f"Successfully wrote modified content to {new_filename}")
        return True  # Indicate success

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File '{filename}' not found.")
        return False  # Indicate failure

    except IOError as e:
        # Handle other input/output errors (e.g., file cannot be read, disk error)
        print(f"IOError: An error occurred while reading or writing the file: {e}")
        return False  # Indicate failure

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return False  # Indicate failure

def get_valid_filename():
    """
    Prompts the user to enter a filename and validates that the file exists and can be read.

    Returns:
        str: The valid filename entered by the user.  Returns an empty string "" if no valid file is found.
    """
    while True:
        filename = input("Enter the name of the file to read: ")
        if not filename:
            print("Error: Filename cannot be empty. Please enter a valid filename or 'quit' to exit.")
            continue

        if filename.lower() == 'quit':
            print("Exiting program.")
            return ""  # Return empty string to indicate quitting

        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist. Please check the filename and try again.")
            continue

        if not os.path.isfile(filename):
            print(f"Error: '{filename}' is not a file.  Please enter a filename, not a directory.")
            continue

        try:
            # Check if the file can be opened for reading
            with open(filename, 'r') as f:
                pass #  We don't need to do anything with the file, just test if we can open it
            return filename  # Return the filename if it exists and can be opened
        except IOError:
            print(f"Error: File '{filename}' cannot be read. Please check file permissions.")
            continue  # Go back to the beginning of the loop

def main():
    """
    Main function to coordinate the file reading, modification, and writing process.
    """
    input_filename = get_valid_filename()  # Get a valid filename from the user
    if not input_filename:
        return  # Exit if no valid filename was provided (user entered 'quit')

    output_filename = "modified_" + input_filename  # Create a new filename for the output

    # Call the function to modify the file and handle any errors
    if modify_file_content(input_filename, output_filename):
        print(f"File '{input_filename}' successfully processed. Modified content written to '{output_filename}'.")
    else:
        print(f"File processing failed for '{input_filename}'.") # print message


if __name__ == "__main__":
    main()  # Execute the main function when the script is run
