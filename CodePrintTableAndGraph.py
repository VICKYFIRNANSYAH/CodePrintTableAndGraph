import sys
import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
import os

# ===============================
# FUNGSI CETAK TABEL DENGAN GARIS
# ===============================
def print_table(df, max_rows=5):
    df = df.head(max_rows)

    # Hitung lebar kolom
    col_widths = []
    for col in df.columns:
        max_len = max(df[col].astype(str).map(len).max(), len(col))
        col_widths.append(max_len + 2)

    # Garis tabel
    line = "+" + "+".join("-" * w for w in col_widths) + "+"
    print(line)

    # Header
    header = "|".join(str(col).center(w) for col, w in zip(df.columns, col_widths))
    print("|" + header + "|")
    print(line)

    # Isi tabel
    for _, row in df.iterrows():
        row_str = "|".join(str(val).ljust(w) for val, w in zip(row, col_widths))
        print("|" + row_str + "|")

    print(line)


# ===============================
# BACA CSV
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data_dummy.csv")

if not os.path.exists(csv_path):
    print("File CSV tidak ditemukan!")
    sys.exit()

df = pd.read_csv(csv_path)

print("\nData Aplikasi Play Store:")
print_table(df)   # ← pakai fungsi baru


# ===============================
# APLIKASI QT
# ===============================
app = QtWidgets.QApplication(sys.argv)

win = pg.GraphicsLayoutWidget(title="Data Aplikasi Play Store")
win.resize(900, 600)
win.show()

# ===============================
# 1️⃣ Grafik Jumlah Aplikasi per Kategori
# ===============================
kategori_count = df["Kategori"].value_counts()

plot1 = win.addPlot(title="Jumlah Aplikasi per Kategori")
x1 = list(range(len(kategori_count)))

bar1 = pg.BarGraphItem(x=x1, height=kategori_count.values, width=0.6)
plot1.addItem(bar1)

ticks1 = [(i, str(v)) for i, v in enumerate(kategori_count.index)]
plot1.getAxis('bottom').setTicks([ticks1])

plot1.setLabel('left', 'Jumlah Aplikasi')
plot1.setLabel('bottom', 'Kategori')

win.nextRow()

# ===============================
# 2️⃣ Grafik Distribusi Rating
# ===============================
rating_count = df["Rating_Level"].value_counts().sort_index()

plot2 = win.addPlot(title="Distribusi Rating")
x2 = list(range(len(rating_count)))

bar2 = pg.BarGraphItem(x=x2, height=rating_count.values, width=0.6)
plot2.addItem(bar2)

ticks2 = [(i, str(v)) for i, v in enumerate(rating_count.index)]
plot2.getAxis('bottom').setTicks([ticks2])

plot2.setLabel('left', 'Jumlah Aplikasi')
plot2.setLabel('bottom', 'Rating')

win.nextRow()

# ===============================
# 3️⃣ Scatter Tahun vs Download
# ===============================
plot3 = win.addPlot(title="Download vs Tahun Rilis")

scatter = pg.ScatterPlotItem(
    x=df["Tahun_Rilis"],
    y=df["Jumlah_Download"],
    pen=pg.mkPen(None),
    brush=pg.mkBrush(0, 0, 255, 120),
    size=8
)

plot3.addItem(scatter)
plot3.setLabel('left', 'Jumlah Download')
plot3.setLabel('bottom', 'Tahun Rilis')
plot3.showGrid(x=True, y=True)

sys.exit(app.exec())