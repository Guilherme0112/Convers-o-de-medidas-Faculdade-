import tkinter as tk
from tkinter import messagebox

def show_distance_conversion():
    def calculate_distance_conversion():
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        value = distance_entry.get()

        if not value:
            messagebox.showerror("ERRO", "Por favor, insira um valor.")
            return

        try:
            value = float(value)
        except ValueError:
            messagebox.showerror("ERRO", "Por favor, insira um valor numérico.")
            return

        conversion_factors = {
            "Quilômetros": {"Metros": 1000, "Centímetros": 100000},
            "Metros": {"Quilômetros": 1/1000, "Centímetros": 100},
            "Centímetros": {"Quilômetros": 1/100000, "Metros": 1/100}
        }

        if from_unit == to_unit:
            result = value
        else:
            result = value * conversion_factors[from_unit][to_unit]

        result_label.config(text=f"Resultado: {result:.2f} {to_unit}")

    distance_window = tk.Toplevel(root)
    distance_window.title("Conversor de Distância")
    distance_window.geometry("400x400")

    units = ["Quilômetros", "Metros", "Centímetros"]

    from_unit_var = tk.StringVar(distance_window)
    from_unit_var.set("SELECIONE A UNIDADE:")
    from_unit_menu = tk.OptionMenu(distance_window, from_unit_var, *units)
    from_unit_menu.pack(pady=10)

    to_unit_var = tk.StringVar(distance_window)
    to_unit_var.set("CONVERTER PARA:")
    to_unit_menu = tk.OptionMenu(distance_window, to_unit_var, *units)
    to_unit_menu.pack(pady=10)

    distance_entry = tk.Entry(distance_window)
    distance_entry.pack(pady=10)

    calculate_button = tk.Button(distance_window, text="CONVERTER", command=calculate_distance_conversion)
    calculate_button.pack(pady=10)

    result_label = tk.Label(distance_window, text="")
    result_label.pack(pady=10)

    back_button = tk.Button(distance_window, text="VOLTAR", command=distance_window.destroy)
    back_button.pack(pady=10)

def show_temperature_conversion():
    def calculate_temperature_conversion():
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        value = temperature_entry.get()

        if not value:
            messagebox.showerror("ERRO", "Por favor, insira um valor.")
            return

        try:
            value = float(value)
        except ValueError:
            messagebox.showerror("ERRO", "Por favor, insira um valor numérico.")
            return

        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value + 459.67) * 5/9
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32

        result_label.config(text=f"Resultado: {result:.2f} {to_unit}")

    temperature_window = tk.Toplevel(root)
    temperature_window.title("CONVERSOR DE TEMPERATURA")
    temperature_window.geometry("400x400")

    units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_unit_var = tk.StringVar(temperature_window)
    from_unit_var.set("SELECIONE A UNIDADE:")
    from_unit_menu = tk.OptionMenu(temperature_window, from_unit_var, *units)
    from_unit_menu.pack(pady=10)

    to_unit_var = tk.StringVar(temperature_window)
    to_unit_var.set("CONVERTER PARA:")
    to_unit_menu = tk.OptionMenu(temperature_window, to_unit_var, *units)
    to_unit_menu.pack(pady=10)

    temperature_entry = tk.Entry(temperature_window)
    temperature_entry.pack(pady=10)

    calculate_button = tk.Button(temperature_window, text="CONVERTER", command=calculate_temperature_conversion)
    calculate_button.pack(pady=10)

    result_label = tk.Label(temperature_window, text="")
    result_label.pack(pady=10)

    back_button = tk.Button(temperature_window, text="VOLTAR", command=temperature_window.destroy)
    back_button.pack(pady=10)

def show_currency_conversion():
    def calculate_currency_conversion():
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        value = currency_entry.get()

        if not value:
            messagebox.showerror("ERRO", "Por favor, insira um valor.")
            return

        try:
            value = float(value)
        except ValueError:
            messagebox.showerror("ERRO", "Por favor, insira um valor numérico.")
            return

        conversion_rates = {
            ("Real", "Dólar"): 0.19, #Cotação do dia 30/05/2024
            ("Real", "Euro"): 0.18,
            ("Dólar", "Real"): 5.20,
            ("Dólar", "Euro"): 0.92,
            ("Euro", "Real"): 5.64,
            ("Euro", "Dólar"): 1.08,
            ("Real", "Real"): 1.00,
            ("Dólar", "Dólar"): 1.00,
            ("Euro", "Euro"): 1.00
        }

        if (from_currency, to_currency) in conversion_rates:
            rate = conversion_rates[(from_currency, to_currency)]
            result = value * rate
        else:
            messagebox.showerror("ERRO", "Taxa de conversão não encontrada.")
            return

        result_label.config(text=f"Resultado: {result:.2f} {to_currency}")

    currency_window = tk.Toplevel(root)
    currency_window.title("Conversor de Moedas")
    currency_window.geometry("400x400")

    currencies = ["Real", "Dólar", "Euro"]

    from_currency_var = tk.StringVar(currency_window)
    from_currency_var.set("SELECIONE A MOEDA:")
    from_currency_menu = tk.OptionMenu(currency_window, from_currency_var, *currencies)
    from_currency_menu.pack(pady=10)

    to_currency_var = tk.StringVar(currency_window)
    to_currency_var.set("CONVERTER PARA:")
    to_currency_menu = tk.OptionMenu(currency_window, to_currency_var, *currencies)
    to_currency_menu.pack(pady=10)

    currency_entry = tk.Entry(currency_window)
    currency_entry.pack(pady=10)

    calculate_button = tk.Button(currency_window, text="CONVERTER", command=calculate_currency_conversion)
    calculate_button.pack(pady=10)

    result_label = tk.Label(currency_window, text="")
    result_label.pack(pady=10)

    back_button = tk.Button(currency_window, text="VOLTAR", command=currency_window.destroy)
    back_button.pack(pady=10)

def show_calculator():
    def calculate_operation():
        num1 = num1_entry.get()
        num2 = num2_entry.get()
        operation = operation_var.get()

        if not num1 or not num2:
            messagebox.showerror("ERRO", "Por favor, insira ambos os números.")
            return

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            messagebox.showerror("ERRO", "Por favor, insira valores numéricos válidos.")
            return

        if operation == "SOMA":
            result = num1 + num2
        elif operation == "SUBTRAÇÃO":
            result = num1 - num2
        elif operation == "MULTIPLICAÇÃO":
            result = num1 * num2
        elif operation == "DIVISÃO":
            if num2 == 0:
                messagebox.showerror("ERRO", "Divisão por zero não é permitida!")
                return
            result = num1 / num2

        result_label.config(text=f"Resultado: {result}")

    calculator_window = tk.Toplevel(root)
    calculator_window.title("CALCULADORA")
    calculator_window.geometry("400x400")

    num1_label = tk.Label(calculator_window, text="NÚMERO 1:")
    num1_label.pack(pady=5)
    num1_entry = tk.Entry(calculator_window)
    num1_entry.pack(pady=5)

    operation_label = tk.Label(calculator_window, text="OPERAÇÃO:")
    operation_label.pack(pady=5)
    operation_var = tk.StringVar(calculator_window)
    operation_var.set("SOMA")
    operation_menu = tk.OptionMenu(calculator_window, operation_var, "SOMA", "SUBTRAÇÃO", "MULTIPLICAÇÃO", "DIVISÃO")
    operation_menu.pack(pady=5)

    num2_label = tk.Label(calculator_window, text="NÚMERO 2:")
    num2_label.pack(pady=5)
    num2_entry = tk.Entry(calculator_window)
    num2_entry.pack(pady=5)

    calculate_button = tk.Button(calculator_window, text="CALCULAR", command=calculate_operation)
    calculate_button.pack(pady=10)

    result_label = tk.Label(calculator_window, text="")
    result_label.pack(pady=5)

    back_button = tk.Button(calculator_window, text="VOLTAR", command=calculator_window.destroy)
    back_button.pack(pady=10)

def confirm_exit():
    answer = messagebox.askyesno("Finalizar", "Tem certeza que deseja encerrar o programa?")
    if answer:
        root.destroy()

root = tk.Tk()
root.title("CONVERSOR E CALCULADORA PYTHON")
root.geometry("400x400")

menu = tk.Menu(root)
root.config(menu=menu)

conversion_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Converter Medidas", menu=conversion_menu)
conversion_menu.add_command(label="Distância", command=show_distance_conversion)
conversion_menu.add_command(label="Temperatura", command=show_temperature_conversion)
conversion_menu.add_command(label="Moedas", command=show_currency_conversion)

calculator_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Calculadora", menu=calculator_menu)
calculator_menu.add_command(label="Abrir", command=show_calculator)

menu.add_separator()

menu.add_command(label="Finalizar", command=confirm_exit)

root.mainloop()



