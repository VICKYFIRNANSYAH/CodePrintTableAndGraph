# 📊 CodePrintTableAndGraph

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![PyQtGraph](https://img.shields.io/badge/PyQtGraph-Data%20Visualization-green)
![CSV](https://img.shields.io/badge/Data-CSV-orange)
![License](https://img.shields.io/github/license/YOUR_USERNAME/YOUR_REPOSITORY)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPOSITORY)

**CodePrintTableAndGraph** is a Python-based data visualization project that reads data from a **CSV file**, prints the data in a formatted **table in the terminal**, and displays several **interactive graphs** using **PyQtGraph**.

This project is useful for learning **data processing, visualization, and Python GUI applications**.

---

# 🚀 Features

- 📄 Reads dataset from a **CSV file**
- 🖨 Prints formatted tables in the **terminal**
- 📊 Displays multiple **data visualizations**
- 🖥 Interactive **GUI window**
- 📈 Supports **bar charts and scatter plots**

---

# 📂 Project Structure

```
CodePrintTableAndGraph
│
├── CodePrintTableAndGraph.py
├── data_dummy.csv
└── README.md
```

---

# 📊 Data Visualizations

The application generates three types of graphs.

## 1️⃣ Number of Apps per Category

A **bar chart** showing the number of applications in each category.

Purpose:
- Analyze the distribution of apps across categories.

---

## 2️⃣ Rating Distribution

A **bar chart** showing the number of applications grouped by rating level.

Purpose:
- Observe rating trends among apps.

---

## 3️⃣ Downloads vs Release Year

A **scatter plot** showing the relationship between:

- **Release Year**
- **Number of Downloads**

Purpose:
- Analyze popularity trends of apps over time.

---

# 🖥 Example Terminal Output

The program prints a formatted preview of the dataset:

```
+-----------+-----------+-------------+
| Kategori  | Rating    | Download    |
+-----------+-----------+-------------+
| Game      | High      | 5000000     |
| Education | Medium    | 1000000     |
| Finance   | High      | 2500000     |
+-----------+-----------+-------------+
```

---

# ⚙️ Technologies Used

- **Python**
- **Pandas**
- **PyQtGraph**
- **Qt (PyQt5 backend)**

---

# 📦 Installation

Clone this repository:

```bash
git clone https://github.com/VICKYFIRNANSYAH/CodePrintTableAndGraph.git
cd YOUR_REPOSITORY
```

Install required libraries:

```bash
pip install pandas pyqtgraph pyqt5
```

---

# ▶️ Running the Program

Run the script using:

```bash
python CodePrintTableAndGraph.py
```

The program will:

1. Load the dataset from `data_dummy.csv`
2. Print a formatted table in the terminal
3. Display interactive charts in a GUI window

---

# 📌 Dataset Requirements

The CSV file should contain the following columns:

```
Kategori
Rating_Level
Tahun_Rilis
Jumlah_Download
```

Example:

```
Kategori,Rating_Level,Tahun_Rilis,Jumlah_Download
Game,High,2021,5000000
Education,Medium,2020,1000000
Finance,High,2019,2500000
```

---

# 🎯 Use Cases

This project can be used for:

- Learning **Python data visualization**
- Practicing **Pandas data analysis**
- Studying **PyQtGraph GUI development**
- Academic assignments related to **data analytics**

---

# 👨‍💻 Author

**Muhammad Vicky Firnansyah**

Fields of interest:

- Artificial Intelligence  
- Machine Learning  
- Data Analysis  
- Computer Vision  
- Full Stack Development  

---

# 📄 License

This project is released under the **MIT License**.
