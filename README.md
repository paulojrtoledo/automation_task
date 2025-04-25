# Product Registration Automation

This project automates the process of registering products on a website using Python and PyAutoGUI. It opens a browser, logs into the system, and fills out a form with data from a CSV file.

---

## Features

- Opens the system login page in Chrome
- Logs in automatically
- Reads product data from a `.csv` file
- Fills out and submits the registration form for each product

---

## Technologies Used

- Python 3
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)

---

## File Structure

- `main.py` → The automation script
- `produtos.csv` → Data file containing product information

---

## CSV File Format

The script expects a `produtos.csv` file with the following columns:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs`

Example of the CSV file content:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
12345,Brand A,Product X,Electronics,199.99,100.00,No observations
67890,Brand B,Product Y,Automotive,299.99,150.00,Check stock
