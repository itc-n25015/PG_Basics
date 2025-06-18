import csv

with open("TWS.csv","w",newline="")as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["韓国アイドルグループ", "TWS(トゥアス)", "シニュ", "ドフン", "ヨンジェ", "ハンジン", "ジフン", "ギョンミン"])

