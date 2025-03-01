class App(object):
    def __init__(self, master, dataframes):
        self.master = master
        self.master.title("Stock Market Simulation")
        
        self.dataframes = dataframes
        
        for i, (name, df) in enumerate(self.dataframes.items()):
            button = tk.Button(master, text = f'Show Plot for {name}',
                               command = lambda n = name, d = df: self.show_plot_window(n,d))
            button.pack(pady = 5)



    def show_plot_window(self, df_name, df):
        plot_window = tk.Toplevel(self.master)
        plot_window.title(f'Live Plot - {df_name}')
        
        fig, ax = plt.subplots(figsize = (5,4))
        canvas = FigureCanvasTKAgg(fig, master = plot_window)
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        current_index = 1
        

    def update_plot():
        nonlocal current_index

        ax.clear()
        sub_df = df.iloc[:current_index]
        ax.plot(sub)
