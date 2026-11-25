# ThermoScope – Python (Programovacie techniky)

**Autor:** Pavlo Rybydailo, Smart technológie vo výrobe, FVT TUKE

Aplikácia so grafickým rozhraním (Tkinter) pre prácu s teplotnými údajmi.

## Čo program robí

1. Pracuje s údajmi o teplotách a zobrazuje ich v grafickom rozhraní.
2. Umožňuje zadať vstupnú hodnotu a zobraziť výsledok.
3. Zobrazuje grafy pôvodných a vypočítaných hodnôt.

## Spustenie

```bash
pip install -r requirements.txt
python main.py
```

## Vytvorenie .exe

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name ThermoScope main.py
```

Výsledok: `dist/ThermoScope.exe` (spustí sa aj bez Pythonu).
