# BMI Calculator

## Description
A simple Python-based BMI (Body Mass Index) Calculator that calculates a person's BMI using their weight and height and provides the corresponding BMI category.

## Features
- Accepts weight and height from the user
- Validates that the entered values are positive numbers
- Calculates BMI using the standard formula
- Displays the BMI result
- Handles invalid numeric input
- Provides a simple command-line interface

## Technologies Used
- Python 3
- Python standard library

## Requirements
- Python 3.x installed on your computer

## BMI Formula
BMI is calculated using:

BMI = weight (kg) / height (m)^2

## How to Run
1. Install Python 3.x.
2. Open PowerShell or Command Prompt.
3. Navigate to the project folder.
4. Run the Python file:

```bash
python bmi_calculator.py
```

Replace `bmi_calculator.py` with the actual Python filename if it is different.

## Usage
Enter your weight and height when prompted. The program validates the input and calculates your BMI.

## BMI Categories
For adults, BMI is commonly interpreted as:

| BMI | Category |
| --- | --- |
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obesity |

These categories are general reference ranges and are not a medical diagnosis.

## Project Structure
```text
BMI calculator/
├── bmi_calculator.py
├── README.md
└── assistant.py
```

## Future Improvements
- Add a graphical user interface (GUI)
- Add support for height in centimeters/feet and inches
- Store calculation history

## Author
M.Sreeram