import random
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

APP_NAME = "ThermoScope"
AUTHOR = "Pavlo Rybydailo"

# ---------- Кольори та шрифти ----------
BG = "#1b1d2a"
CARD = "#262a3d"
BTN = "#343a52"
BTN_HOVER = "#434b68"
ACCENT = "#4f8cff"
ACCENT_HOVER = "#6aa0ff"
TEXT = "#eef0f7"
MUTED = "#9aa0b8"
FIELD = "#f7f8fb"
GRAD_TOP = "#161a33"
GRAD_BOTTOM = "#2b2f5e"
PANEL = "#262c58"

FONT_TITLE = ("Helvetica", 46, "bold")
FONT_H = ("Helvetica", 15, "bold")
FONT = ("Helvetica", 13)
FONT_BIG = ("Helvetica", 18, "bold")
FONT_MONO = ("Courier", 12)

current = {"lang": "en"}
LANG_NAMES = {"en": "English", "sk": "Slovenčina", "uk": "Українська"}

# ---------- Переклади ----------
T = {
    "en": {
        "tagline": "Temperature analysis & conversion",
        "start": "Start",
        "options_title": "Options",
        "language": "Language",
        "close": "Close",
        "about_title": "About",
        "about_text": ("Author: {author}\n\nWhat the program does:\n"
                       "1. Generates 50 random temperature values.\n"
                       "2. Sorts them and finds the minimum, maximum and mean.\n"
                       "3. Converts every value from °C to °F using F = C × 1.8 + 32.\n"
                       "4. Draws original and converted values on one chart for comparison."),
        "calc_title": "ThermoScope – Calculator",
        "h1": "1. Formula: °C → °F   (F = C × 1.8 + 32)",
        "enter": "Enter °C:",
        "convert": "Calculate",
        "result": "Result (°F):",
        "no_result": "—",
        "h2": "2. Array and operations",
        "gen": "Generate array (50)",
        "show": "Show array",
        "sort": "Sort",
        "stats": "Min / Max / Mean",
        "h3": "3. Chart: original vs converted",
        "draw": "Draw chart",
        "plot_title": "Original vs converted values",
        "plot_x": "Index (sorted)",
        "plot_y": "Value",
        "plot_orig": "Original (°C)",
        "plot_conv": "Converted (°F)",
        "hint": "Press “Generate array (50)” to start.",
        "generated": "Generated an array of {n} values.",
        "array_head": "Array (original values, °C):",
        "sorted_head": "Sorted from smallest to largest:",
        "stat_min": "Minimum:",
        "stat_max": "Maximum:",
        "stat_mean": "Mean:",
        "warn_title": "Warning",
        "error_title": "Error",
        "need_array": "Generate the array first.",
        "need_input": "Enter a number in the field first.",
        "bad_input": "Please enter a valid number, e.g. 25 or 36.6.",
    },
    "sk": {
        "tagline": "Analýza a prevod teplôt",
        "start": "Štart",
        "options_title": "Možnosti",
        "language": "Jazyk",
        "close": "Zavrieť",
        "about_title": "O programe",
        "about_text": ("Autor: {author}\n\nČo program robí:\n"
                       "1. Vygeneruje 50 náhodných teplotných hodnôt.\n"
                       "2. Zoradí ich a nájde minimum, maximum a priemer.\n"
                       "3. Prepočíta každú hodnotu z °C na °F podľa vzorca F = C × 1,8 + 32.\n"
                       "4. Zobrazí pôvodné a prepočítané hodnoty v jednom grafe na porovnanie."),
        "calc_title": "ThermoScope – Kalkulačka",
        "h1": "1. Vzorec: °C → °F   (F = C × 1,8 + 32)",
        "enter": "Zadajte °C:",
        "convert": "Vypočítať",
        "result": "Výsledok (°F):",
        "no_result": "—",
        "h2": "2. Pole a operácie",
        "gen": "Vygenerovať pole (50)",
        "show": "Zobraziť pole",
        "sort": "Zoradiť",
        "stats": "Min / Max / Priemer",
        "h3": "3. Graf: pôvodné a prepočítané",
        "draw": "Vykresliť graf",
        "plot_title": "Pôvodné a prepočítané hodnoty",
        "plot_x": "Index (zoradené)",
        "plot_y": "Hodnota",
        "plot_orig": "Pôvodné (°C)",
        "plot_conv": "Prepočítané (°F)",
        "hint": "Na začatie stlačte „Vygenerovať pole (50)“.",
        "generated": "Vygenerované pole z {n} hodnôt.",
        "array_head": "Pole (pôvodné hodnoty, °C):",
        "sorted_head": "Zoradené od najmenšej po najväčšiu:",
        "stat_min": "Minimum:",
        "stat_max": "Maximum:",
        "stat_mean": "Priemer:",
        "warn_title": "Upozornenie",
        "error_title": "Chyba",
        "need_array": "Najskôr vygenerujte pole.",
        "need_input": "Najskôr zadajte číslo do poľa.",
        "bad_input": "Zadajte správne číslo, napríklad 25 alebo 36,6.",
    },
    "uk": {
        "tagline": "Аналіз і перетворення температур",
        "start": "Старт",
        "options_title": "Опції",
        "language": "Мова",
        "close": "Закрити",
        "about_title": "Про програму",
        "about_text": ("Автор: {author}\n\nЩо робить програма:\n"
                       "1. Генерує 50 випадкових значень температури.\n"
                       "2. Сортує їх і знаходить мінімум, максимум та середнє.\n"
                       "3. Перераховує кожне значення з °C у °F за формулою F = C × 1,8 + 32.\n"
                       "4. Показує початкові та обчислені значення на одному графіку для порівняння."),
        "calc_title": "ThermoScope – Калькулятор",
        "h1": "1. Формула: °C → °F   (F = C × 1,8 + 32)",
        "enter": "Введіть °C:",
        "convert": "Порахувати",
        "result": "Результат (°F):",
        "no_result": "—",
        "h2": "2. Масив і операції",
        "gen": "Згенерувати масив (50)",
        "show": "Показати масив",
        "sort": "Відсортувати",
        "stats": "Мін / Макс / Середнє",
        "h3": "3. Графік: вихідні та обчислені",
        "draw": "Побудувати графік",
        "plot_title": "Вихідні та обчислені значення",
        "plot_x": "Індекс (відсортовано)",
        "plot_y": "Значення",
        "plot_orig": "Вихідні (°C)",
        "plot_conv": "Обчислені (°F)",
        "hint": "Натисніть «Згенерувати масив (50)», щоб почати.",
        "generated": "Згенеровано масив з {n} значень.",
        "array_head": "Масив (вихідні значення, °C):",
        "sorted_head": "Відсортовано від найменшого до найбільшого:",
        "stat_min": "Мінімум:",
        "stat_max": "Максимум:",
        "stat_mean": "Середнє:",
        "warn_title": "Увага",
        "error_title": "Помилка",
        "need_array": "Спочатку згенеруйте масив.",
        "need_input": "Спочатку введіть число в поле.",
        "bad_input": "Введіть коректне число, наприклад 25 або 36.6.",
    },
}


def tr(key, **kw):
    text = T[current["lang"]].get(key) or T["en"][key]
    return text.format(**kw) if kw else text


# ---------- Допоміжне для кольорів і малювання ----------
def lerp(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rrect(c, x1, y1, x2, y2, r, **kw):
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
           x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2,
           x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


def draw_gradient(c, w, h, top, bottom, tag):
    c.delete(tag)
    for y in range(0, h, 3):
        c.create_rectangle(0, y, w, y + 3, fill=lerp(top, bottom, y / h),
                           outline="", tags=tag)
    c.tag_lower(tag)


def fade_in(win, steps=8):
    """Плавна поява вікна (працює на macOS і Windows)."""
    try:
        win.attributes("-alpha", 0.0)
    except tk.TclError:
        return

    def step(i):
        try:
            win.attributes("-alpha", i / steps)
        except tk.TclError:
            return
        if i < steps:
            win.after(18, step, i + 1)

    step(1)


# ---------- Закруглена кнопка з анімацією ----------
class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, bg_parent, primary=False,
                 font=FONT, padx=18, pady=8, radius=14, fixed=None):
        super().__init__(parent, bg=bg_parent, highlightthickness=0, bd=0,
                         cursor="hand2")
        self.text = text
        self.command = command
        self.font = font
        self.padx, self.pady, self.radius = padx, pady, radius
        self.fixed = fixed
        self.base = ACCENT if primary else BTN
        self.hover = ACCENT_HOVER if primary else BTN_HOVER
        self.cur = self.base
        self._job = None
        self.size_to_text()
        self.bind("<Button-1>", lambda e: self.command() if self.command else None)
        self.bind("<Enter>", lambda e: self.animate(self.hover))
        self.bind("<Leave>", lambda e: self.animate(self.base))

    def size_to_text(self):
        if self.fixed:
            w, h = self.fixed
        else:
            f = tkfont.Font(font=self.font)
            w = f.measure(self.text) + 2 * self.padx
            h = f.metrics("linespace") + 2 * self.pady
        self.w, self.h = w, h
        self.config(width=w, height=h)
        self.draw()

    def draw(self):
        self.delete("all")
        rrect(self, 1, 1, self.w - 1, self.h - 1, self.radius,
              fill=self.cur, outline="")
        self.create_text(self.w / 2, self.h / 2, text=self.text,
                         fill="white", font=self.font)

    def set_text(self, text):
        self.text = text
        self.size_to_text()

    def set_colors(self, base, hover):
        self.base, self.hover = base, hover
        self.cur = base
        self.draw()

    def set_bg(self, color):
        self.config(bg=color)

    def animate(self, target, steps=8):
        if self._job:
            self.after_cancel(self._job)
        start = self.cur

        def step(i):
            self.cur = lerp(start, target, i / steps)
            self.draw()
            self._job = self.after(16, step, i + 1) if i < steps else None

        step(1)


def make_button(parent, text, command, primary=False, font=FONT,
                padx=16, pady=8, bg=CARD):
    return RoundedButton(parent, text, command, bg_parent=bg, primary=primary,
                         font=font, padx=padx, pady=pady)


def make_card(parent):
    return tk.Frame(parent, bg=CARD)


# ---------- Логіка ----------
def generate_values(n=50, low=20.0, high=100.0):
    return [round(random.uniform(low, high), 2) for _ in range(n)]


def sort_values(values):
    return sorted(values)


def get_min(values):
    return min(values)


def get_max(values):
    return max(values)


def get_mean(values):
    return sum(values) / len(values)


def formula(x):
    """Перевід °C у °F: F = C·1.8 + 32. Замініть на формулу з Mendix, якщо треба."""
    return x * 1.8 + 32


# ---------- Вікно розрахунків ----------
class CalcWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app.root, bg=BG)
        self.geometry("920x820")
        self.values = []
        self.result = None
        self.view = None
        self.plot_on = False

        c1 = make_card(self)
        c1.pack(fill="x", padx=20, pady=(20, 8))
        self.h1 = tk.Label(c1, font=FONT_H, bg=CARD, fg=TEXT, anchor="w")
        self.h1.pack(fill="x", padx=18, pady=(14, 6))
        row = tk.Frame(c1, bg=CARD)
        row.pack(fill="x", padx=18, pady=(0, 14))
        self.l_enter = tk.Label(row, font=FONT, bg=CARD, fg=TEXT)
        self.l_enter.pack(side="left")
        self.entry = tk.Entry(row, width=10, font=FONT, bg=FIELD, fg="black",
                              insertbackground="black", relief="flat")
        self.entry.pack(side="left", padx=10, ipady=5)
        self.btn_calc = make_button(row, "", self.calc_formula)
        self.btn_calc.pack(side="left", padx=4)
        self.result_label = tk.Label(row, font=FONT_BIG, bg=CARD, fg=TEXT)
        self.result_label.pack(side="left", padx=18)

        c2 = make_card(self)
        c2.pack(fill="x", padx=20, pady=8)
        self.h2 = tk.Label(c2, font=FONT_H, bg=CARD, fg=TEXT, anchor="w")
        self.h2.pack(fill="x", padx=18, pady=(14, 6))
        btns = tk.Frame(c2, bg=CARD)
        btns.pack(fill="x", padx=18)
        self.btn_gen = make_button(btns, "", self.make_array)
        self.btn_gen.pack(side="left", padx=(0, 6))
        self.btn_show = make_button(btns, "", self.show_array)
        self.btn_show.pack(side="left", padx=6)
        self.btn_sort = make_button(btns, "", self.do_sort)
        self.btn_sort.pack(side="left", padx=6)
        self.btn_stats = make_button(btns, "", self.do_stats)
        self.btn_stats.pack(side="left", padx=6)
        self.text = tk.Text(c2, height=7, font=FONT_MONO, bg=FIELD, fg="black",
                            relief="flat", wrap="word", padx=10, pady=8)
        self.text.pack(fill="x", padx=18, pady=14)

        c3 = make_card(self)
        c3.pack(fill="both", expand=True, padx=20, pady=(8, 20))
        head = tk.Frame(c3, bg=CARD)
        head.pack(fill="x", padx=18, pady=(14, 6))
        self.h3 = tk.Label(head, font=FONT_H, bg=CARD, fg=TEXT)
        self.h3.pack(side="left")
        self.btn_plot = make_button(head, "", self.draw_plot)
        self.btn_plot.pack(side="right")
        self.fig, self.ax = plt.subplots(figsize=(7, 3.2), facecolor=FIELD)
        self.canvas = FigureCanvasTkAgg(self.fig, master=c3)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=18, pady=(0, 16))

        self.apply_texts()
        fade_in(self)

    def apply_texts(self):
        self.title(tr("calc_title"))
        self.h1.config(text=tr("h1"))
        self.l_enter.config(text=tr("enter"))
        self.btn_calc.set_text(tr("convert"))
        self.h2.config(text=tr("h2"))
        self.btn_gen.set_text(tr("gen"))
        self.btn_show.set_text(tr("show"))
        self.btn_sort.set_text(tr("sort"))
        self.btn_stats.set_text(tr("stats"))
        self.h3.config(text=tr("h3"))
        self.btn_plot.set_text(tr("draw"))
        self.render_result()
        self.render_text()
        if self.plot_on:
            self.draw_plot(silent=True)

    def render_result(self):
        if self.result is None:
            self.result_label.config(text=f"{tr('result')} {tr('no_result')}")
        else:
            self.result_label.config(text=f"{tr('result')} {self.result:.2f}")

    def render_text(self):
        if self.view is None:
            out = tr("hint")
        elif self.view == "generated":
            out = (tr("generated", n=len(self.values)) + "\n\n" +
                   tr("array_head") + "\n" + ", ".join(map(str, self.values)))
        elif self.view == "array":
            out = tr("array_head") + "\n" + ", ".join(map(str, self.values))
        elif self.view == "sorted":
            out = (tr("sorted_head") + "\n" +
                   ", ".join(map(str, sort_values(self.values))))
        else:
            out = "\n".join([
                f"{tr('stat_min'):<12}{get_min(self.values):.2f}",
                f"{tr('stat_max'):<12}{get_max(self.values):.2f}",
                f"{tr('stat_mean'):<12}{get_mean(self.values):.2f}",
            ])
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", out)
        self.text.config(state="disabled")

    def need_array(self):
        if not self.values:
            messagebox.showwarning(tr("warn_title"), tr("need_array"), parent=self)
            return False
        return True

    def calc_formula(self):
        raw = self.entry.get().strip().replace(",", ".")
        if not raw:
            messagebox.showwarning(tr("warn_title"), tr("need_input"), parent=self)
            return
        try:
            x = float(raw)
        except ValueError:
            messagebox.showerror(tr("error_title"), tr("bad_input"), parent=self)
            return
        self.result = formula(x)
        self.render_result()

    def make_array(self):
        self.values = generate_values(50)
        self.view = "generated"
        self.render_text()

    def show_array(self):
        if self.need_array():
            self.view = "array"
            self.render_text()

    def do_sort(self):
        if self.need_array():
            self.view = "sorted"
            self.render_text()

    def do_stats(self):
        if self.need_array():
            self.view = "stats"
            self.render_text()

    def draw_plot(self, silent=False):
        if not self.values:
            if not silent:
                self.need_array()
            return
        self.plot_on = True
        sv = sort_values(self.values)
        calc = [formula(v) for v in sv]
        x = range(len(sv))
        self.ax.clear()
        self.ax.plot(x, sv, marker="o", color="#3b6fd8", label=tr("plot_orig"))
        self.ax.plot(x, calc, marker="s", color="#e8743b", label=tr("plot_conv"))
        self.ax.set_title(tr("plot_title"))
        self.ax.set_xlabel(tr("plot_x"))
        self.ax.set_ylabel(tr("plot_y"))
        self.ax.grid(True)
        self.ax.legend()
        self.fig.tight_layout()
        self.canvas.draw()


# ---------- Опції ----------
class OptionsWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app.root, bg=BG)
        self.app = app
        self.geometry("420x440")
        self.resizable(False, False)
        self.head = tk.Label(self, font=FONT_H, bg=BG, fg=TEXT)
        self.head.pack(pady=(30, 10))
        self.lang_head = tk.Label(self, font=FONT, bg=BG, fg=MUTED)
        self.lang_head.pack(pady=(10, 6))
        self.lang_btns = {}
        for code, name in LANG_NAMES.items():
            b = RoundedButton(self, name, lambda c=code: app.set_language(c),
                              bg_parent=BG, font=FONT, padx=30, pady=10, radius=12)
            b.pack(pady=5)
            self.lang_btns[code] = b
        self.close_btn = make_button(self, "", self.destroy, bg=BG)
        self.close_btn.pack(pady=24)
        self.apply_texts()
        fade_in(self)

    def apply_texts(self):
        self.title(tr("options_title"))
        self.head.config(text=tr("options_title"))
        self.lang_head.config(text=tr("language"))
        for code, b in self.lang_btns.items():
            on = code == current["lang"]
            b.set_colors(ACCENT if on else BTN, ACCENT_HOVER if on else BTN_HOVER)
        self.close_btn.set_text(tr("close"))


# ---------- Про програму ----------
class HelpWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app.root, bg=BG)
        self.geometry("560x460")
        self.resizable(False, False)
        self.head = tk.Label(self, font=FONT_H, bg=BG, fg=TEXT)
        self.head.pack(pady=(30, 10))
        self.body = tk.Label(self, font=FONT, bg=BG, fg=TEXT,
                             justify="left", wraplength=480)
        self.body.pack(padx=30, pady=10)
        self.close_btn = make_button(self, "", self.destroy, bg=BG)
        self.close_btn.pack(pady=20)
        self.apply_texts()
        fade_in(self)

    def apply_texts(self):
        self.title(tr("about_title"))
        self.head.config(text=f"{APP_NAME} – {tr('about_title')}")
        self.body.config(text=tr("about_text", author=AUTHOR))
        self.close_btn.set_text(tr("close"))


# ---------- Головне меню ----------
class App:
    def __init__(self, root):
        self.root = root
        root.geometry("720x600")
        root.minsize(600, 520)
        self.calc_w = None
        self.options_w = None
        self.help_w = None

        self.cv = tk.Canvas(root, highlightthickness=0, bd=0, bg=GRAD_BOTTOM)
        self.cv.pack(fill="both", expand=True)

        self.title_id = self.cv.create_text(0, 0, text=APP_NAME, font=FONT_TITLE, fill=TEXT)
        self.tag_id = self.cv.create_text(0, 0, text="", font=("Helvetica", 15), fill=MUTED)

        self.start_btn = RoundedButton(self.cv, "", self.open_calc, bg_parent=PANEL,
                                       primary=True, font=FONT_BIG, padx=50, pady=14, radius=24)
        self.start_win = self.cv.create_window(0, 0, window=self.start_btn)

        icon_bg = lerp(GRAD_TOP, GRAD_BOTTOM, 0.92)
        self.opt_btn = RoundedButton(self.cv, "⚙", self.open_options, bg_parent=icon_bg,
                                     font=("Helvetica", 22), fixed=(56, 56), radius=16)
        self.opt_win = self.cv.create_window(0, 0, window=self.opt_btn, anchor="center")

        self.help_btn = RoundedButton(self.cv, "?", self.open_help, bg_parent=icon_bg,
                                      font=("Helvetica", 22, "bold"), fixed=(56, 56), radius=16)
        self.help_win = self.cv.create_window(0, 0, window=self.help_btn, anchor="center")

        self.cv.bind("<Configure>", lambda e: self.layout())
        self.apply_texts()

    def layout(self):
        w, h = self.cv.winfo_width(), self.cv.winfo_height()
        if w < 2:
            return
        draw_gradient(self.cv, w, h, GRAD_TOP, GRAD_BOTTOM, "bg")
        self.cv.delete("panel")
        rrect(self.cv, w * 0.12, h * 0.12, w * 0.88, h * 0.78, 30,
              fill=PANEL, outline="", tags="panel")
        self.cv.tag_raise("panel", "bg")
        self.cv.coords(self.title_id, w / 2, h * 0.30)
        self.cv.coords(self.tag_id, w / 2, h * 0.30 + 52)
        self.cv.coords(self.start_win, w / 2, h * 0.58)
        self.cv.coords(self.opt_win, 60, h - 60)
        self.cv.coords(self.help_win, w - 60, h - 60)

    def apply_texts(self):
        self.root.title(APP_NAME)
        self.cv.itemconfig(self.tag_id, text=tr("tagline"))
        self.start_btn.set_text(tr("start"))

    def _open(self, attr, factory):
        win = getattr(self, attr)
        if win is not None and win.winfo_exists():
            win.lift()
            return
        setattr(self, attr, factory(self))

    def open_calc(self):
        self._open("calc_w", CalcWindow)

    def open_options(self):
        self._open("options_w", OptionsWindow)

    def open_help(self):
        self._open("help_w", HelpWindow)

    def set_language(self, code):
        current["lang"] = code
        self.apply_texts()
        for w in (self.calc_w, self.options_w, self.help_w):
            if w is not None and w.winfo_exists():
                w.apply_texts()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()