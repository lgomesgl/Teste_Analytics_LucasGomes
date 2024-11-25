# Quod-ps

## Project Overview

The first part involves creating a sales-related database with the following columns:ID, Date, Product, Category, Quantity, Price. The data period should range from 01/01/2023 to 12/31/2023. After creating the database, clean the data and save it as a file named data_clean.csv (inside the data folder). Additionally, create new columns, such as total sales. This step was carried out in the notebook clean_and_analyse_data. Subsequently, create a new notebook (exploratory_analysis) to perform the Exploratory Data Analysis (EDA) on the sales database. The SQL part is located in the /src/sql folder, in the consultas.sql file. A report in Markdown format was also created.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- [Git](https://git-scm.com/)
- [Python (version 3.8 or later)](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/)

---

## Setup Instructions

### Step 1: Clone the Repository
Open your terminal and run the following command:

```bash
git clone https://github.com/lgomesgl/Teste_Analytics_LucasGomes.git
cd Teste_Analytics_LucasGomes
```

### Step 2: Create a Virtual Environment and activate

- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

- On Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook
```bash
jupyter notebook
```

## Folders Structure
Quod-ps/
│
├── .ipynb_checkpoints/       
├── data/                     # Directory for datasets
├── src/                      
│   ├── notebooks/            # Jupyter notebooks 
│   ├── sql/                  # SQL scripts
│
├── relatorio_insights.md     # Insights and reports
├── .gitignore               
├── README.md                 