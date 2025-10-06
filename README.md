# Quiz Simulator

A Python-based interactive quiz simulator designed for educational purposes, supporting both single-choice and multiple-choice questions across different courses and topics.

## 🎯 Features

- **Multi-Course Support**: Organize quizzes by course codes (e.g., HE5091, SC2002)
- **Topic-Based Organization**: Each course can have multiple topics/lectures
- **Question Type Support**: 
  - Single-choice questions
  - Multiple-choice questions (select multiple correct answers)
- **Interactive Experience**: 
  - Colorful console interface
  - Randomized answer order for each question
  - Immediate feedback with explanations
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📁 Project Structure

```
Quiz-Simulator/
├── scripts/
│   └── main.py          # Main application file
├── materials/           # Quiz content organized by course
│   ├── he5091/         # HE5091 Principles of Economics
│   │   ├── lecture1.json
│   │   ├── lecture2.json
│   │   ├── lecture3.json
│   │   ├── lecture4.json
│   │   ├── lecture5.json
│   │   └── lecture6.json
│   └── sc2002/         # SC2002 Database course
│       └── database_quiz.json
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd Quiz-Simulator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the quiz simulator**
   ```bash
   cd scripts
   python main.py
   ```

## 🎮 How to Use

1. **Start the Application**: Run `python main.py` from the scripts directory
2. **Select Course**: Choose from available courses (e.g., HE5091, SC2002)
3. **Select Topic**: Choose a specific topic/lecture from the selected course
4. **Answer Questions**: 
   - For single-choice: Enter one letter (A, B, C, D)
   - For multiple-choice: Enter letters separated by commas (A,B,C)
5. **Review Results**: Get immediate feedback with explanations for each question

## 📝 Question Format

Questions are stored in JSON format with the following structure:

### Single-Choice Question
```json
{
  "id": 1,
  "question": "What is a database?",
  "options": {
    "A": "A website that displays data.",
    "B": "Software to manage data.",
    "C": "A collection of organized data.",
    "D": "A computer with storage."
  },
  "correct": "C",
  "type": "single",
  "explanation": "A database is a collection of data specifically organized..."
}
```

### Multiple-Choice Question
```json
{
  "id": 2,
  "question": "Which are database management systems?",
  "options": {
    "A": "MySQL",
    "B": "PostgreSQL", 
    "C": "Microsoft Word",
    "D": "Oracle"
  },
  "correct": ["A", "B", "D"],
  "type": "multiple",
  "explanation": "MySQL, PostgreSQL, and Oracle are all database management systems..."
}
```

## 🛠️ Adding New Content

### Adding a New Course

1. Create a new folder in `materials/` with the course code (e.g., `materials/cs101/`)
2. Add JSON files for each topic/lecture

### Adding Questions to Existing Course

1. Navigate to the appropriate course folder
2. Edit the existing JSON file or create a new one
3. Follow the question format shown above

### Required Fields

- `id`: Unique identifier for the question
- `question`: The question text
- `options`: Dictionary of answer options (A, B, C, D, etc.)
- `correct`: Single answer (string) or multiple answers (array)
- `type`: "single" or "multiple"
- `explanation`: Explanation of the correct answer

## 🎨 Features

### Visual Elements
- **Colorful Interface**: Uses colorama for colored console output
- **Clear Question Numbering**: Easy to track progress
- **Answer Shuffling**: Options are randomized for each question
- **Immediate Feedback**: Instant results with explanations

### Error Handling
- Invalid file detection
- JSON parsing error handling
- Input validation for answer selection
- Graceful handling of missing files

## 🔧 Dependencies

- **colorama**: For cross-platform colored terminal text output

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Add your questions or improvements
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/new-feature`)
6. Create a Pull Request

## 📚 Course Information

### HE5091 - Principles of Economics
Contains lecture materials covering fundamental economic concepts and principles.

### SC2002 - Database Systems
Contains questions related to database design, ER diagrams, normalization, and SQL.

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: colorama**
   ```bash
   pip install colorama
   ```

2. **File not found errors**
   - Ensure you're running the script from the `scripts/` directory
   - Check that the materials folder exists and contains the course files

3. **JSON decode errors**
   - Verify that all JSON files are properly formatted
   - Use a JSON validator to check file syntax

## 📄 License

This project is intended for educational purposes. Please ensure you have appropriate permissions for any course materials included.

## 🔮 Future Enhancements

- [ ] Score tracking and statistics
- [ ] Timed quizzes
- [ ] Question difficulty levels
- [ ] Export results to file
- [ ] Web-based interface
- [ ] Question bank management system
- [ ] User accounts and progress tracking

---

Made with ❤️ for educational excellence