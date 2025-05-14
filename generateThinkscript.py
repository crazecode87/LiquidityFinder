import os
import pandas as pd

def csv_to_thinkscript(csv_path, output_path):
    df = pd.read_csv(csv_path)
    
    level_values = df[df.columns[0]].dropna().tolist()

    thinkscript_lines = ["declare upper;"]
    
    for i, value in enumerate(level_values):
        plot_name = f"plot level{i+1}"
        thinkscript_lines.append(f"{plot_name} = {value};")

    thinkscript_code = "\n".join(thinkscript_lines)

    with open(output_path, "w") as f:
        f.write(thinkscript_code)

    print(f"ThinkScript saved to {output_path}")

levels_folder = "levels"
for filename in os.listdir(levels_folder):
    if filename.endswith(".csv"):
        csv_file_path = os.path.join(levels_folder, filename)
        ts_filename = filename.replace(".csv", ".ts")
        output_ts_path = os.path.join("thinkscript", ts_filename)
        os.makedirs("thinkscript", exist_ok=True)
        csv_to_thinkscript(csv_file_path, output_ts_path)