
![logo](https://github.com/user-attachments/assets/34933587-e0c2-4866-9b44-46bb981e9f94)

# UD Ingot2ore Calculator

A desktop GUI tool for the game **Space Engineers**, created for the **Upside Down Universe (UDU)** server. This tool calculates how much ore is needed to produce a desired amount of ingots, factoring in refinery type and yield module bonuses.

---

## 🚀 Features

- 🧱 Supports a wide range of ores: Iron, Gold, Platinum, Uranium, Thorium, etc.
- 🏭 Select between:
  - Refinery
  - Basic Refinery
- 🔧 Choose Yield Module bonus level (0 to 8)
- 📊 Calculates:
  - Ore Mass (kg)
  - Ore Volume (L)
  - Ore Units per kg

---

## 💾 Download

The latest compiled `.exe` version is available on the [Releases](../../releases) page.

To run from source:

```bash
git clone https://github.com/yourusername/Ingot2Ore.git
cd Ingot2Ore
python ingot2ore_calculator.py
```

> 💡 Requires Python 3.x. No external packages required—uses only Tkinter.

---

## 📈 How It Works

Each ore has defined:

- `mass` → Mass of ingot in kilograms  
- `volume` → Volume per kg of ore  
- `yield` → Refining efficiency per refinery type  

### Formula used

```
Ore Required (kg) = (Ingot Amount × Ingot Mass) / (Base Refinery Yield × Module Yield Bonus)
```

### Example

To refine 100 Iron Ingots using a Refinery with 4 yield modules:

- Ingot Mass = 1.43 kg  
- Base Yield = 1.0  
- Module Bonus (4 points) = 1.41  

```
Ore Mass = (100 × 1.43) / (1.0 × 1.41) ≈ 101.42 kg
```

---

## 🧪 Supported Ores

- Iron  
- Nickel  
- Silicon  
- Cobalt  
- Magnesium  
- Silver  
- Gold  
- Uranium  
- Platinum  
- Scrap Metal  
- Titanium  
- Thorium  

---

## 🖼️ Screenshots

![image](https://github.com/user-attachments/assets/e373e30f-b282-46e5-b94d-fb6271f23238)


---

## 🧑‍💻 Contributing

Feel free to fork the repo and submit a pull request! Ideas and improvements are welcome.

---


## 🎮 Designed for Space Engineers

This tool is especially helpful for:

- Planning refinery logistics  
- Mining efficiency calculations  

---

## 📦 Release Info

When releasing:

- Upload the compiled `.exe` to the Releases section  
- Include version notes and changelog  

Created with 💙 for Space Engineers players by ReyHades.

