# BMI Calculator

A simple Python BMI calculator that asks the user for their weight and height, then calculates the Body Mass Index (BMI) and classifies it into a health category.

## Features
- Validates that weight and height are positive numbers
- Handles invalid input gracefully
- Calculates BMI using the formula:
  BMI = weight / (height x height)
- Displays the BMI result and category:
  - Underweight
  - Normal
  - Overweight
  - Obese

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Run:

```bash
python "bmi calculator.py"
```

## Example
```text
===== BMI Calculator =====
Enter your weight in kg: 70
Enter your height in meters: 1.75

===== Result =====
BMI: 22.86
Category: Normal
```

## Requirements
- Python 3.x installed on the system

## File
- `bmi calculator.py` - main BMI calculator script
