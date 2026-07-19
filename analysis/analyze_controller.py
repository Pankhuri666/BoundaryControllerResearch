import csv
import glob

files = sorted(glob.glob("../scenarios_examples/05_ring_road_emulation_scenario/paper_controller_log_margin*.csv"))

print("=" * 70)
print("PAPER CONTROLLER ANALYSIS")
print("=" * 70)

for file in files:

    count = 0
    sum_error = 0.0
    max_error = 0.0
    correction_count = 0

    with open(file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:

            if row.get("ey") is None or row.get("uy") is None:
                continue

            if row["ey"] == "" or row["uy"] == "":
                continue

            try:
                ey = abs(float(row["ey"]))
                uy = abs(float(row["uy"]))
            except:
                continue

            count += 1
            sum_error += ey

            if ey > max_error:
                max_error = ey

            if uy > 0.01:
                correction_count += 1

    print("\n" + file.split("/")[-1])
    print("Samples:", count)
    print("Average lateral error:", round(sum_error / count, 4))
    print("Maximum lateral error:", round(max_error, 4))
    print("Controller corrections:", correction_count)

print("\nDone!")
