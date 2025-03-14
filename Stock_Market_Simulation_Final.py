import pandas as pd
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class StockMarketSimulation:
    def __init__(self):
        # Load stock data
        self.stock1 = pd.read_csv(r"C:\Users\tommy\Downloads\Stock Market Dataset\Stocks\wrd_us.txt", sep=',')
        self.stock2 = pd.read_csv(r"C:\Users\tommy\Downloads\Stock Market Dataset\Stocks\watt_us.txt", sep=',')
        self.stock3 = pd.read_csv(r"C:\Users\tommy\Downloads\Stock Market Dataset\Stocks\wbc_us.txt", sep=',')

        # The current "day index" – how many rows are visible
        self.day_index = 1

        # Create the main window
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title("Stock Market Simulation")

        # This will hold references to each graph so we can update them all
        self.graphs = []  # each item will be (df, ax, canvas)

        # Setup the GUI components
        self.setup_widgets()

    def setup_widgets(self):
        """
        Build the main GUI: greeting section, 'Next Day' button, 
        and 3 side-by-side frames each containing a line chart.
        """

        # --- Greeting section ---
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)

        label_name = tk.Label(frame_input, text="Enter your name:")
        label_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_name = tk.Entry(frame_input)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        frame_button = tk.Frame(self.root)
        frame_button.pack()

        button_greet = tk.Button(frame_button, text="Greet", command=self.greet_user)
        button_greet.pack(padx=5, pady=5)

        # --- Next Day button (updates *all* graphs) ---
        next_day_btn = tk.Button(self.root, text="Next Day", command=self.next_day_for_all)
        next_day_btn.pack(pady=10)

        # --- Frame to hold 3 charts side by side ---
        charts_frame = tk.Frame(self.root)
        charts_frame.pack(fill=tk.BOTH, expand=True)

        # Create a chart for each stock
        # We'll create 3 sub-frames, each holding one chart
        frame1 = tk.Frame(charts_frame)
        frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_chart(self.stock1, frame1, title="Stock 1")

        frame2 = tk.Frame(charts_frame)
        frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_chart(self.stock2, frame2, title="Stock 2")

        frame3 = tk.Frame(charts_frame)
        frame3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.create_chart(self.stock3, frame3, title="Stock 3")

        # Initially plot only the first day (row 0) for each DataFrame
        self.update_all_plots()

    def greet_user(self):
        username = self.entry_name.get()
        if username.strip():
            messagebox.showinfo("Greet", f"Hello, {username}!")
        else:
            messagebox.showwarning("Greet", "Please enter a name.")

    def create_chart(self, df, parent_frame, title="Stock"):
        """
        Create a matplotlib Figure/Axes in 'parent_frame' for the given DataFrame 'df'.
        Store references so we can update the plot later.
        """
        fig, ax = plt.subplots(figsize=(5, 3))

        # Embed the figure in the given parent_frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Append references so we can update them on next_day
        self.graphs.append((df, ax, canvas, title))

    def update_all_plots(self):
        """
        For each (df, ax, canvas, title) in self.graphs,
        plot data up to self.day_index.
        """
        for df, ax, canvas, title in self.graphs:
            ax.clear()

            # Slice the DataFrame up to 'day_index'
            partial_df = df.iloc[:self.day_index]

            # Plot whichever columns you prefer, e.g., 'Open' and 'Close'
            # Make sure these columns exist in each CSV
            # If you only have 'Close' or other columns, adjust accordingly
            if {'Open', 'Close'}.issubset(partial_df.columns):
                partial_df[['Open', 'Close']].plot(ax=ax)
            else:
                # If 'Open'/'Close' don't exist, just plot everything numeric
                partial_df.plot(ax=ax)

            ax.set_title(f"{title} (up to day {self.day_index})")
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")

            canvas.draw()

    def next_day_for_all(self):
        """
        Increment the day_index and update all plots,
        as long as we haven't exceeded the max rows.
        """
        # Check if we can advance further (based on the largest DataFrame length).
        # If you want them all to stop at the smallest data set's length, 
        # you can get the min length instead.
        max_len = max(len(item[0]) for item in self.graphs)

        if self.day_index < max_len:
            self.day_index += 1
            self.update_all_plots()
        else:
            print("No more days to show for at least one of the stocks.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = StockMarketSimulation()
    app.run()