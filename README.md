![Python](https://img.shields.io/badge/Python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=plastic&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning%20%F0%9F%93%9A-green?style=plastic)
 🐼 Pandas Learning Repository

This repository contains my hands-on practice and learning of the **Pandas library in Python**.
Each file demonstrates a specific concept with examples for better understanding.

---

 📁 Project Structure

```id="pnd1"
PANDAS/
│
├── 1.Series.py                # Creating and working with Pandas Series
├── 2.Dataframe.py            # DataFrame basics
├── 3.Set_index.py            # Setting index
├── 4.reset_Index.py          # Resetting index
│
├── 5.Accessing.py            # Accessing data
├── 5.1.adding_ROW_Val.py     # Adding rows/values
├── 5.2.modify_row.py         # Modifying rows
│
├── 6.Operation.py            # Operations on data
├── 7.File_Convertion.py      # File conversions (CSV, etc.)
├── 8.Read_file.py            # Reading files
├── 9.Frame_dataSK.py         # DataFrame structure practice
│
├── 10.fun_on_DF.py           # Functions on DataFrame
├── 11.Iteration_data.py      # Iterating over data
├── 12.Statics.py             # Statistical operations
├── 13.concate.py             # Concatenation
├── 14.merge.py               # Merging DataFrames
│
├── employee.csv              # Sample dataset
├── .gitignore
└── README.md
```

---

 🧠 Topics Covered

* 📊 Pandas Series & DataFrames
* 🔑 Indexing & Resetting Index
* ➕ Adding & Modifying Data
* 🔍 Data Accessing Techniques
* ⚙️ Data Operations
* 📂 File Handling (CSV read/write)
* 🔁 Iteration in DataFrames
* 📈 Statistical Functions
* 🔗 Concatenation & Merging

---

 ⚙️ Setup Instructions

1. Install Pandas

```bash id="pd1"
pip install pandas
```

---

 2. Run Any File

```bash id="pd2"
python 1.Series.py
```

---

 📌 Example Usage

```python id="pd3"
import pandas as pd

data = {"Name": ["A", "B"], "Age": [20, 25]}
df = pd.DataFrame(data)

print(df)
```

---

 📊 Dataset

* `employee.csv` → Used for practicing file operations and DataFrame manipulation

---

 🎯 Learning Outcome

* Strong understanding of Pandas fundamentals
* Ability to manipulate and analyze data
* Hands-on experience with real-world data operations

---

 🚀 Future Improvements

* Add data visualization (Matplotlib / Seaborn)
* Add real-world datasets
* Build mini data analysis projects

---

 📜 License

This project is open-source and free to use.

