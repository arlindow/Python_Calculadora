import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")

        # Variáveis
        self.visor_var = tk.StringVar()
        self.visor_var.set("")

        # Visor
        visor = tk.Entry(self.root, textvariable=self.visor_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right')
        visor.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in botoes:
            tk.Button(self.root, text=text, font=('Arial', 18), command=lambda t=text: self.botao_clicado(t)).grid(row=row, column=column)

    def botao_clicado(self, valor):
        if valor == 'C':
            self.visor_var.set("")  # Limpar visor
        elif valor == '=':
            try:
                resultado = eval(self.visor_var.get())
                self.visor_var.set(str(resultado))
            except Exception as e:
                self.visor_var.set("Erro")
        else:
            self.visor_var.set(self.visor_var.get() + valor)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()


