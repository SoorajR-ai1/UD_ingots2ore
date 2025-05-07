import tkinter as tk
from tkinter import ttk

# Ore properties: ingot_mass (kg), volume_per_kg_ore (L), refinery_yields (percent)
ore_data = {
    'Iron':      {'mass': 1.43, 'volume': 0.37, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Nickel':    {'mass': 2.5,  'volume': 0.37, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Silicon':   {'mass': 1.43, 'volume': 0.37, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Cobalt':    {'mass': 3.333,'volume': 0.37, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Magnesium': {'mass': 143,  'volume': 0.37, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Silver':    {'mass': 10,   'volume': 0.37, 'yield': {'Refinery': 1}},
    'Gold':      {'mass': 100,  'volume': 0.37, 'yield': {'Refinery': 1}},
    'Uranium':   {'mass': 100,  'volume': 0.37, 'yield': {'Refinery': 1}},
    'Platinum':  {'mass': 200,  'volume': 0.37, 'yield': {'Refinery': 1}},
    'Scrap Metal': {'mass': 1.25,'volume': 0.25, 'yield': {'Refinery': 1, 'Basic Refinery': 0.7}},
    'Titanium':  {'mass': 3.333,'volume': 250,  'yield': {'Refinery': 1}},
    'Thorium':   {'mass': 100,  'volume': 250,  'yield': {'Refinery': 1}}
}

module_yield = {
    0: 1.00,
    1: 1.09,
    2: 1.19,
    3: 1.30,
    4: 1.41,
    5: 1.54,
    6: 1.68,
    7: 1.83,
    8: 2.00
}

class OreCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Engineers Ingot to Ore Calculator")

        # Dropdowns
        self.refinery_var = tk.StringVar(value='Refinery')
        self.module_var = tk.IntVar(value=0)

        ttk.Label(root, text="Refinery Type:").grid(row=0, column=0, sticky='w')
        ttk.OptionMenu(root, self.refinery_var, 'Refinery', 'Refinery', 'Basic Refinery').grid(row=0, column=1)

        ttk.Label(root, text="Module Points:").grid(row=0, column=2, sticky='w')
        ttk.OptionMenu(root, self.module_var, 0, *range(0, 9)).grid(row=0, column=3)

        # Table headers
        headers = [' Ingot Type ', ' Amount ', ' Ore Mass (kg) ', ' Ore Volume (L) ', ' 1kg Ore Units ']
        for i, h in enumerate(headers):
            ttk.Label(root, text=h, font=('Segoe UI', 10, 'bold')).grid(row=2, column=i)

        self.entries = []
        for i, ore in enumerate(ore_data.keys()):
            ttk.Label(root, text=ore).grid(row=i+3, column=0, sticky='w')
            qty_entry = ttk.Entry(root, width=10)
            qty_entry.grid(row=i+3, column=1)
            self.entries.append((ore, qty_entry))

        ttk.Button(root, text="Calculate", command=self.calculate).grid(row=len(ore_data)+3, column=1, pady=10)
        self.output_labels = []

    def calculate(self):
        for label_row in self.output_labels:
            for lbl in label_row:
                lbl.destroy()
        self.output_labels.clear()

        refinery = self.refinery_var.get()
        module_bonus = module_yield[self.module_var.get()]

        for i, (ore, entry) in enumerate(self.entries):
            try:
                qty = float(entry.get())
            except:
                qty = 0
            if qty <= 0:
                continue

            data = ore_data[ore]
            base_yield = data['yield'].get(refinery)
            if base_yield is None:
                values = [tk.Label(self.root, text="N/A") for _ in range(3)]
            else:
                total_yield = base_yield * module_bonus
                ore_required_kg = qty * data['mass'] / total_yield
                volume_l = ore_required_kg * data['volume']
                ore_units = ore_required_kg

                values = [
                    tk.Label(self.root, text=f"{ore_required_kg:.2f}"),
                    tk.Label(self.root, text=f"{volume_l:.2f}"),
                    tk.Label(self.root, text=f"{ore_units:.2f}")
                ]

            for j, lbl in enumerate(values):
                lbl.grid(row=i+3, column=j+2)
            self.output_labels.append(values)


if __name__ == '__main__':
    root = tk.Tk()
    app = OreCalculatorApp(root)
    root.mainloop()
