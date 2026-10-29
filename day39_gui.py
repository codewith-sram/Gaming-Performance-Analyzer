import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

import pandas as pd
import joblib

DATA_FILE = "gaming_stats.csv"
MODEL_FILE = "gaming_model.pkl"


class GamingAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gaming Performance Analyzer")
        self.root.geometry("700x520")
        self.root.minsize(600, 450)

        self.root.configure(bg="#171923")

        title = tk.Label(
            root,
            text="GAMING PERFORMANCE ANALYZER",
            font=("Arial", 19, "bold"),
            bg="#171923",
            fg="white"
        )
        title.pack(pady=(25, 8))

        subtitle = tk.Label(
            root,
            text="Your gaming statistics and prediction dashboard",
            font=("Arial", 10),
            bg="#171923",
            fg="#b8c1d9"
        )
        subtitle.pack(pady=(0, 20))

        button_frame = tk.Frame(root, bg="#171923")
        button_frame.pack(pady=10)

        buttons = [
            ("View Gaming Statistics", self.show_statistics),
            ("Predict Kills", self.predict_kills),
            ("Export Gaming Report", self.export_report),
            ("Open Day 38 Dashboard", self.open_dashboard),
            ("Exit Application", self.root.destroy)
        ]

        for label, command in buttons:
            button = tk.Button(
                button_frame,
                text=label,
                command=command,
                font=("Arial", 11, "bold"),
                width=28,
                pady=9,
                bg="#344b75",
                fg="white",
                activebackground="#4b6595",
                activeforeground="white",
                relief="flat",
                cursor="hand2"
            )
            button.pack(pady=6)

        self.status = tk.Label(
            root,
            text="Ready",
            font=("Arial", 9),
            bg="#171923",
            fg="#8de0b1"
        )
        self.status.pack(side="bottom", pady=15)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            messagebox.showerror(
                "Missing Dataset",
                f"{DATA_FILE} was not found.\n"
                "Place it in your project folder."
            )
            return None

        try:
            data = pd.read_csv(DATA_FILE)
            required = ["Kills", "Deaths", "Assists"]

            if not all(column in data.columns for column in required):
                messagebox.showerror(
                    "Invalid Dataset",
                    "The CSV must contain Kills, Deaths and Assists."
                )
                return None

            for column in required:
                data[column] = pd.to_numeric(
                    data[column], errors="coerce"
                )

            data = data.dropna(subset=required)

            if data.empty:
                messagebox.showwarning(
                    "No Data",
                    "The dataset contains no valid match records."
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

        if total_deaths:
            kd_text = f"{total_kills / total_deaths:.2f}"
        else:
            kd_text = "Undefined (zero deaths)"

        report = (
            f"Total Matches: {len(data)}\n"
            f"Total Kills: {total_kills:g}\n"
            f"Total Deaths: {total_deaths:g}\n"
            f"Total Assists: {total_assists:g}\n\n"
            f"Average Kills: {data['Kills'].mean():.2f}\n"
            f"Average Deaths: {data['Deaths'].mean():.2f}\n"
            f"Average Assists: {data['Assists'].mean():.2f}\n"
            f"Overall K/D Ratio: {kd_text}"
        )

        messagebox.showinfo("Gaming Statistics", report)
        self.status.config(text="Statistics displayed")

    def predict_kills(self):
        if not os.path.exists(MODEL_FILE):
            messagebox.showerror(
                "Missing Model",
                f"{MODEL_FILE} was not found.\n"
                "Run your Day 33 program first."
            )
            return

        deaths = simpledialog.askinteger(
            "Match Details",
            "Enter expected deaths:",
            parent=self.root,
            minvalue=0
        )

        if deaths is None:
            return

        assists = simpledialog.askinteger(
            "Match Details",
            "Enter expected assists:",
            parent=self.root,
            minvalue=0
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
                f"Expected deaths: {deaths}\n"
                f"Expected assists: {assists}\n\n"
                f"Estimated kills: {prediction:.2f}"
            )

            save = messagebox.askyesno(
                "Save Prediction",
                "Would you like to save this prediction?"
            )

            if save:
                result = pd.DataFrame([{
                    "Deaths": deaths,
                    "Assists": assists,
                    "Predicted_Kills": round(prediction, 2)
                }])

                filename = "day39_predictions.csv"

                if os.path.exists(filename):
                    result.to_csv(
                        filename,
                        mode="a",
                        header=False,
                        index=False
                    )
                else:
                    result.to_csv(filename, index=False)

                messagebox.showinfo(
                    "Saved",
                    f"Prediction saved to {filename}"
                )

            self.status.config(text="Prediction completed")

        except Exception as error:
            messagebox.showerror(
                "Prediction Error",
                f"Could not make prediction:\n{error}"
            )

    def export_report(self):
        data = self.load_data()

        if data is None:
            return

        filename = filedialog.asksaveasfilename(
            parent=self.root,
            title="Save Gaming Report",
            defaultextension=".csv",
            initialfile="day39_gaming_report.csv",
            filetypes=[("CSV files", "*.csv")]
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

    def open_dashboard(self):
        filename = "day38_performance_dashboard.png"

        if not os.path.exists(filename):
            messagebox.showwarning(
                "Dashboard Not Found",
                "Run day38.py first to create the dashboard image."
            )
            return

        try:
            os.startfile(os.path.abspath(filename))
            self.status.config(text="Dashboard opened")
        except Exception as error:
            messagebox.showerror(
                "Open Error",
                f"Could not open the dashboard:\n{error}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = GamingAnalyzerApp(root)
    root.mainloop()