import camelot
import pandas as pd

pdf = camelot.read_pdf("keppel-corporation-limited-annual-report-2018.pdf")

for table in pdf:

    table.to_excel("output2.xlsx")


