# Unclosed File Handling in Python

This repository demonstrates a common error in Python: failing to close a file properly when an exception occurs.  Unclosed files can lead to resource leaks, particularly in long-running applications or when dealing with many files.

The `bug.py` file contains a function that attempts to write to a file but doesn't guarantee closure if an exception is raised. The `bugSolution.py` provides a corrected version using the `with` statement, ensuring the file is always closed, regardless of exceptions.

## How to reproduce the bug

1. Run `bug.py`.  Observe that if no exception is raised, the file is closed successfully.  However, if you uncomment the line that raises an exception, the file will remain open, resulting in a resource leak.

## Solution

The `bugSolution.py` shows the best practice for file handling using the `with` statement. This context manager ensures the file is always closed, preventing resource leaks.
