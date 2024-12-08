def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write("This will always be written to the file")
            #raise Exception("Simulating an error") #uncomment to trigger exception
    except Exception as e:
        print(f"An error occurred: {e}")

# Example demonstrating the use of the 'with' statement
function_with_closed_file("my_file.txt")
