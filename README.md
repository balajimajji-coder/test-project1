"# test-project1"

A simple Python desktop application built with Tkinter that allows a user to enter their name and receive a greeting.

## Features

- Simple graphical user interface (GUI)
- Name input field
- Submit button
- Input validation
  - Name cannot be empty
  - Name must be at least 2 characters long
  - Name can only contain letters and spaces
- Displays validation errors and success messages

## Project Structure

```text
my-name-app/
│
├── main.py
├── name_ui.py
├── validators.py
└── README.md
```

## Files

### main.py

Application entry point.

```python
from name_ui import launch_ui

def main():
    launch_ui()

if __name__ == "__main__":
    main()
```

### name_ui.py

Contains the Tkinter user interface and interaction logic.

### validators.py

Contains validation logic for user input.

## Requirements

- Python 3.9 or later
- Tkinter (included with standard Python installation)

## Running the Application

Clone the repository:

```bash
git clone <repository-url>
cd my-name-app
```

Run the application:

```bash
python main.py
```

## Validation Rules

| Rule | Example |
|--------|---------|
| Cannot be empty | ❌ "" |
| Minimum 2 characters | ❌ "J" |
| Letters and spaces only | ❌ "John123" |
| Valid name | ✅ "John Smith" |

## Example

Input:

```text
John Smith
```

Output:

```text
Hello, John Smith!
```

## Future Enhancements

- Real-time validation
- Unit tests
- 
