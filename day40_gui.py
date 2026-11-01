
import os
import tkinter as tk
from tkinter import ttk, messagebox

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DATA_FILE = "gaming_stats.csv"
PREDICTION_FILE = "day39_predictions.csv"


class GamingAnalyzerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gaming Performance Analyzer - Day 40")
        self.root.geometry("850x600")
        self.root.minsize(700, 500)
        self.root.configure(bg="#171923")

        self.create_interface()

    def create_interface(self):
        title = tk.Label(
            self.root,
            text="GAMING PERFORMANCE ANALYZER",
            font=("Arial", 21, "bold"),
            bg="#171923",
            fg="white"
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Match History and Performance Dashboard",
            font=("Arial", 11),
            bg="#171923",
            fg="#b8c1d9"
        )
        subtitle.pack(pady=(0, 25))

        button_frame = tk.Frame(self.root, bg="#171923")
        button_frame.pack(pady=10)

        buttons = [
            ("View Gaming Statistics", self.show_statistics),
            ("View Match History", self.show_match_history),
            ("Performance Charts", self.show_charts),
            ("Prediction History", self.show_prediction_history),
            ("Exit Application", self.root.destroy)
        ]

        for label, command in buttons:
            button = tk.Button(
                button_frame,
                text=label,
                command=command,
                font=("Arial", 11, "bold"),
                width=30,
                pady=10,
                bg="#344b75",
                fg="white",
                activebackground="#4b6595",
                activeforeground="white",
                relief="flat",
                cursor="hand2"
            )
            button.pack(pady=6)

        self.status = tk.Label(
            self.root,
            text="Application Ready",
            font=("Arial", 10),
            bg="#171923",
            fg="#8de0b1"
        )
        self.status.pack(side="bottom", pady=18)

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            messagebox.showerror(
                "Missing File",
                f"{DATA_FILE} was not found."
            )
            return None

        try:
            data = pd.read_csv(DATA_FILE)

            required = ["Kills", "Deaths", "Assists"]

            if not all(column in data.columns for column in required):
                messagebox.showerror(
                    "Invalid Dataset",
                    "Your dataset must contain Kills, Deaths and Assists."
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
            messagebox.showerror("File Error", str(error))
            return None

    def show_statistics(self):
        data = self.load_data()

        if data is None:
            return

        total_kills = data["Kills"].sum()
        total_deaths = data["Deaths"].sum()
        total_assists = data["Assists"].sum()

        if total_deaths > 0:
            kd_ratio = f"{total_kills / total_deaths:.2f}"
        else:
            kd_ratio = "Undefined (zero deaths)"

        report = (
            f"Total Matches: {len(data)}\n\n"
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
        window.configure(bg="#171923")

        heading = tk.Label(
            window,
            text=title,
            font=("Arial", 16, "bold"),
            bg="#171923",
            fg="white"
        )
        heading.pack(pady=15)

        frame = tk.Frame(window)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

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
            values = [
                round(value, 2) if isinstance(value, float) else value
                for value in row.tolist()
            ]
            table.insert("", "end", values=values)

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

    def show_prediction_history(self):
        if not os.path.exists(PREDICTION_FILE):
            messagebox.showinfo(
                "No History",
                "No saved prediction history found.\n"
                "Save a prediction using your Day 39 application first."
            )
            return

        try:
            data = pd.read_csv(PREDICTION_FILE)

            if data.empty:
                messagebox.showinfo(
                    "No History",
                    "The prediction history file is empty."
                )
                return

            self.show_table("Prediction History", data)
            self.status.config(text="Prediction history displayed")

        except Exception as error:
            messagebox.showerror("File Error", str(error))

    def show_charts(self):
        data = self.load_data()

        if data is None:
            return

        window = tk.Toplevel(self.root)
        window.title("Gaming Performance Charts")
        window.geometry("950x700")
        window.configure(bg="white")

        figure, axes = plt.subplots(2, 1, figsize=(9, 6))

        matches = range(1, len(data) + 1)

        # Chart 1: Match-by-match performance
        axes[0].plot(
            matches, data["Kills"],
            marker="o", label="Kills"
        )
        axes[0].plot(
            matches, data["Deaths"],
            marker="s", label="Deaths"
        )
        axes[0].plot(
            matches, data["Assists"],
            marker="^", label="Assists"
        )

        axes[0].set_title("Match Performance Comparison")
        axes[0].set_xlabel("Match Number")
        axes[0].set_ylabel("Count")
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)

        # Chart 2: Average performance
        categories = ["Kills", "Deaths", "Assists"]
        averages = [
            data["Kills"].mean(),
            data["Deaths"].mean(),
            data["Assists"].mean()
        ]

        axes[1].bar(categories, averages)
        axes[1].set_title("Average Gaming Performance")
        axes[1].set_ylabel("Average Count")
        axes[1].grid(axis="y", alpha=0.3)

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(
            figure, master=window
        )
        canvas.draw()
        canvas.get_tk_widget().pack(
            fill="both", expand=True, padx=10, pady=10
        )

        def close_chart():
            plt.close(figure)
            window.destroy()

        window.protocol("WM_DELETE_WINDOW", close_chart)
        self.status.config(text="Performance charts displayed")


if __name__ == "__main__":
    root = tk.Tk()
    app = GamingAnalyzerApp(root)
    root.mainloop()
