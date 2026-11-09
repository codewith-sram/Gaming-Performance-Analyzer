
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

import pandas as pd
import joblib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DATA_FILE = "gaming_stats.csv"
MODEL_FILE = "gaming_model.pkl"
PREDICTION_FILE = "day41_predictions.csv"


class GamingPerformanceAnalyzer:

    def __init__(self, root):
        self.root = root
        self.root.title("Gaming Performance Analyzer")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        self.root.configure(bg="#171923")

        self.create_interface()

    def create_interface(self):
        header = tk.Frame(self.root, bg="#171923")
        header.pack(fill="x", pady=25)

        tk.Label(
            header,
            text="GAMING PERFORMANCE ANALYZER",
            font=("Arial", 22, "bold"),
            bg="#171923",
            fg="white"
        ).pack()

        tk.Label(
            header,
            text="Complete Gaming Statistics and ML Dashboard",
            font=("Arial", 11),
            bg="#171923",
            fg="#b8c1d9"
        ).pack(pady=5)

        main_frame = tk.Frame(self.root, bg="#171923")
        main_frame.pack(expand=True)

        buttons = [
            ("Add New Match", self.add_match),
            ("View Statistics", self.show_statistics),
            ("Match History", self.show_match_history),
            ("Predict Kills", self.predict_kills),
            ("Performance Charts", self.show_charts),
            ("Prediction History", self.show_prediction_history),
            ("Export Gaming Report", self.export_report),
            ("About Project", self.show_about),
            ("Exit Application", self.root.destroy)
        ]

        for index, (label, command) in enumerate(buttons):
            button = tk.Button(
                main_frame,
                text=label,
                command=command,
                font=("Arial", 11, "bold"),
                width=28,
                pady=12,
                bg="#344b75",
                fg="white",
                activebackground="#4b6595",
                activeforeground="white",
                relief="flat",
                cursor="hand2"
            )
            button.grid(
                row=index // 2,
                column=index % 2,
                padx=15,
                pady=10
            )

        self.status = tk.Label(
            self.root,
            text="Application Ready",
            font=("Arial", 10),
            bg="#171923",
            fg="#8de0b1"
        )
        self.status.pack(side="bottom", pady=18)

    def add_match(self):
        window = tk.Toplevel(self.root)
        window.title("Add New Match")
        window.geometry("400x350")
        window.configure(bg="#171923")
        window.resizable(False, False)

        tk.Label(
            window,
            text="ENTER MATCH DETAILS",
            font=("Arial", 17, "bold"),
            bg="#171923",
            fg="white"
        ).pack(pady=20)

        entries = {}

        for field, example in [
            ("Kills", "12"),
            ("Deaths", "4"),
            ("Assists", "6")
        ]:
            tk.Label(
                window,
                text=field,
                font=("Arial", 11, "bold"),
                bg="#171923",
                fg="white"
            ).pack(pady=(8, 3))

            entry = tk.Entry(
                window,
                font=("Arial", 12),
                justify="center"
            )
            entry.pack()
            entry.insert(0, example)
            entries[field] = entry

        def save_match():
            try:
                kills = int(entries["Kills"].get())
                deaths = int(entries["Deaths"].get())
                assists = int(entries["Assists"].get())

                if min(kills, deaths, assists) < 0:
                    messagebox.showerror(
                        "Invalid Input",
                        "Values cannot be negative.",
                        parent=window
                    )
                    return

                new_match = pd.DataFrame([{
                    "Kills": kills,
                    "Deaths": deaths,
                    "Assists": assists
                }])

                if os.path.exists(DATA_FILE):
                    existing_data = pd.read_csv(DATA_FILE)

                    required = ["Kills", "Deaths", "Assists"]

                    if not all(col in existing_data.columns for col in required):
                        messagebox.showerror(
                            "Invalid Dataset",
                            "Required columns are missing from gaming_stats.csv.",
                            parent=window
                        )
                        return

                    updated_data = pd.concat(
                        [existing_data, new_match],
                        ignore_index=True
                    )
                else:
                    updated_data = new_match

                updated_data.to_csv(DATA_FILE, index=False)

                self.status.config(text="New match saved successfully!")

                messagebox.showinfo(
                    "Success",
                    f"Match saved!\n\n"
                    f"Kills: {kills}\n"
                    f"Deaths: {deaths}\n"
                    f"Assists: {assists}",
                    parent=window
                )

                window.destroy()

            except ValueError:
                messagebox.showerror(
                    "Invalid Input",
                    "Enter whole numbers only.",
                    parent=window
                )
            except Exception as error:
                messagebox.showerror(
                    "Save Error",
                    str(error),
                    parent=window
                )

        tk.Button(
            window,
            text="SAVE MATCH",
            command=save_match,
            font=("Arial", 11, "bold"),
            bg="#287a50",
            fg="white",
            width=20,
            pady=9
        ).pack(pady=20)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            messagebox.showerror(
                "Missing Dataset",
                f"{DATA_FILE} was not found in the project folder."
            )
            return None

        try:
            data = pd.read_csv(DATA_FILE)
            required = ["Kills", "Deaths", "Assists"]

            if not all(column in data.columns for column in required):
                messagebox.showerror(
                    "Invalid Dataset",
                    "Dataset must contain Kills, Deaths and Assists."
                )
                return None

            for column in required:
                data[column] = pd.to_numeric(
                    data[column], errors="coerce"
                )

            data = data.dropna(subset=required).reset_index(drop=True)

            if data.empty:
                messagebox.showwarning(
                    "No Data",
                    "No valid match records were found."
                )
                return None

            return data

        except Exception as error:
            messagebox.showerror("Dataset Error", str(error))
            return None

    def show_statistics(self):
        data = self.load_data()
        if data is None:
            return

        total_kills = data["Kills"].sum()
        total_deaths = data["Deaths"].sum()
        total_assists = data["Assists"].sum()

        kd_ratio = (
            f"{total_kills / total_deaths:.2f}"
            if total_deaths > 0 else "Undefined (zero deaths)"
        )

        report = (
            f"Total Matches: {len(data)}\n"
            f"Total Kills: {total_kills:g}\n"
            f"Total Deaths: {total_deaths:g}\n"
            f"Total Assists: {total_assists:g}\n\n"
            f"Average Kills: {data['Kills'].mean():.2f}\n"
            f"Average Deaths: {data['Deaths'].mean():.2f}\n"
            f"Average Assists: {data['Assists'].mean():.2f}\n"
            f"Overall K/D Ratio: {kd_ratio}"
        )

        messagebox.showinfo("Gaming Statistics", report)
        self.status.config(text="Statistics displayed")

    def show_table(self, title, data):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("850x450")

        frame = tk.Frame(window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = list(data.columns)

        table = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        vertical_scroll = ttk.Scrollbar(
            frame, orient="vertical", command=table.yview
        )
        horizontal_scroll = ttk.Scrollbar(
            frame, orient="horizontal", command=table.xview
        )

        table.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        for column in columns:
            table.heading(column, text=column)
            table.column(column, width=120, anchor="center")

        for _, row in data.iterrows():
            table.insert("", "end", values=list(row))

        table.pack(side="left", fill="both", expand=True)
        vertical_scroll.pack(side="right", fill="y")
        horizontal_scroll.pack(side="bottom", fill="x")

    def show_match_history(self):
        data = self.load_data()
        if data is None:
            return

        data.insert(0, "Match_Number", range(1, len(data) + 1))
        self.show_table("Gaming Match History", data)
        self.status.config(text="Match history displayed")

    def predict_kills(self):
        if not os.path.exists(MODEL_FILE):
            messagebox.showerror(
                "Missing Model",
                f"{MODEL_FILE} was not found. Run Day 33 first."
            )
            return

        deaths = simpledialog.askinteger(
            "Match Details", "Enter expected deaths:",
            parent=self.root, minvalue=0
        )
        if deaths is None:
            return

        assists = simpledialog.askinteger(
            "Match Details", "Enter expected assists:",
            parent=self.root, minvalue=0
        )
        if assists is None:
            return

        try:
            model = joblib.load(MODEL_FILE)

            inputs = pd.DataFrame(
                [{"Deaths": deaths, "Assists": assists}]
            )

            prediction = float(model.predict(inputs)[0])

            messagebox.showinfo(
                "Kill Prediction",
                f"Deaths: {deaths}\n"
                f"Assists: {assists}\n"
                f"Estimated Kills: {prediction:.2f}"
            )

            save = messagebox.askyesno(
                "Save Prediction",
                "Do you want to save this prediction?"
            )

            if save:
                result = pd.DataFrame([{
                    "Deaths": deaths,
                    "Assists": assists,
                    "Predicted_Kills": round(prediction, 2)
                }])

                if os.path.exists(PREDICTION_FILE):
                    result.to_csv(
                        PREDICTION_FILE,
                        mode="a",
                        header=False,
                        index=False
                    )
                else:
                    result.to_csv(PREDICTION_FILE, index=False)

                messagebox.showinfo(
                    "Saved", "Prediction saved successfully."
                )

            self.status.config(text="Prediction completed")

        except Exception as error:
            messagebox.showerror("Prediction Error", str(error))

    def show_prediction_history(self):
        if not os.path.exists(PREDICTION_FILE):
            messagebox.showinfo(
                "No History", "No Day 41 predictions found yet."
            )
            return

        try:
            data = pd.read_csv(PREDICTION_FILE)

            if data.empty:
                messagebox.showinfo(
                    "No History", "Prediction history is empty."
                )
                return

            self.show_table("Prediction History", data)
            self.status.config(text="Prediction history displayed")

        except Exception as error:
            messagebox.showerror("History Error", str(error))

    def show_charts(self):
        data = self.load_data()
        if data is None:
            return

        window = tk.Toplevel(self.root)
        window.title("Gaming Performance Dashboard")
        window.geometry("950x700")

        figure, axes = plt.subplots(2, 1, figsize=(9, 6))
        matches = range(1, len(data) + 1)

        axes[0].plot(
            matches, data["Kills"], marker="o", label="Kills"
        )
        axes[0].plot(
            matches, data["Deaths"], marker="s", label="Deaths"
        )
        axes[0].plot(
            matches, data["Assists"], marker="^", label="Assists"
        )

        axes[0].set_title("Match Performance")
        axes[0].set_xlabel("Match Number")
        axes[0].set_ylabel("Count")
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)

        categories = ["Kills", "Deaths", "Assists"]
        averages = [
            data["Kills"].mean(),
            data["Deaths"].mean(),
            data["Assists"].mean()
        ]

        axes[1].bar(categories, averages)
        axes[1].set_title("Average Performance")
        axes[1].set_ylabel("Average Count")
        axes[1].grid(axis="y", alpha=0.3)

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both", expand=True
        )

        def close_chart():
            plt.close(figure)
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", close_chart)
        self.status.config(text="Charts displayed")

    def export_report(self):
        data = self.load_data()
        if data is None:
            return

        filename = filedialog.asksaveasfilename(
            parent=self.root,
            defaultextension=".csv",
            initialfile="day41_gaming_report.csv",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not filename:
            return

        try:
            data.to_csv(filename, index=False)
            messagebox.showinfo(
                "Export Complete",
                f"Report saved to:\n{filename}"
            )
            self.status.config(text="Report exported")

        except Exception as error:
            messagebox.showerror("Export Error", str(error))

    def show_about(self):
        messagebox.showinfo(
            "About Project",
            "Gaming Performance Analyzer\n\n"
            "A Python-based gaming statistics and machine learning project.\n\n"
            "Technologies:\n"
            "- Python\n"
            "- Pandas\n"
            "- Matplotlib\n"
            "- Scikit-learn\n"
            "- Joblib\n"
            "- Tkinter"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GamingPerformanceAnalyzer(root)
    root.mainloop()
