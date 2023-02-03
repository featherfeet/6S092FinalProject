#!/usr/bin/env python3

import csv

csv_reader = csv.DictReader(open("Mini_Circuits_LNAs.csv"))

for row in csv_reader:
    f_low = float(0.0 if row["F Low (MHz)"] == "DC" else row["F Low (MHz)"])
    f_high = float(row["F High (MHz)"])
    noise_factor = float(row["NF (dB) Typ."])
    intermodulation = float(row["Out. IP3 (dBm) Typ."])
    if 436 > f_low and 436 < f_high:
        print(row["Model Number"])
        print(f"\t - noise factor = {noise_factor}")
        print(f"\t - intermodulation = {intermodulation}")
