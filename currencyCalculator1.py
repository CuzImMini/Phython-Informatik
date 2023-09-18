import tkinter


# Methode für API Zugriff
def getCurrencyConversion(currencyfrom, currencyto):

        if currencyfrom == 'EUR':
            if currencyto == 'EUR':
                return 1
            elif currencyto == 'USD':
                return 1.22
            elif currencyto == 'TRY':
                return 10.26
            elif currencyto == 'CHF':
                return 1.08
            elif currencyto == 'JPY':
                return 126.66
        elif currencyfrom == 'USD':
            if currencyto == 'EUR':
                return 0.82
            elif currencyto == 'USD':
                return 1
            elif currencyto == 'TRY':
                return 8.43
            elif currencyto == 'CHF':
                return 0.89
            elif currencyto == 'JPY':
                return 104.59
        elif currencyfrom == 'TRY':
            if currencyto == 'EUR':
                return 0.097
            elif currencyto == 'USD':
                return 0.12
            elif currencyto == 'TRY':
                return 1
            elif currencyto == 'CHF':
                return 0.11
            elif currencyto == 'JPY':
                return 13.06
        elif currencyfrom == 'CHF':
            if currencyto == 'EUR':
                return 0.92
            elif currencyto == 'USD':
                return 1.12
            elif currencyto == 'TRY':
                return 9.19
            elif currencyto == 'CHF':
                return 1
            elif currencyto == 'JPY':
                return 116.99
        elif currencyfrom == 'JPY':
            if currencyto == 'EUR':
                return 0.0079
            elif currencyto == 'USD':
                return 0.0096
            elif currencyto == 'TRY':
                return 0.076
            elif currencyto == 'CHF':
                return 0.0085
            elif currencyto == 'JPY':
                return 1
        else:
            print("Fehler bei der API Anfrage!")


# Methode für Berechnung
def calculate():
    print('Berechnungen werden ausgeführt!')

    # Variablen von GUI
    origin_currency_value = origin_currency_var.get()
    target_currency_value = target_currency_var.get()
    amount = amountEntry.get()

    # Konvertierung von Betrag in Zahl
    amount = float(amount)

    # Abrufen von Umrechnungsfaktor
    conversionmultiplier = getCurrencyConversion(origin_currency_value, target_currency_value)

    # Löschen Ergebnis
    resultEntry.delete(0, tkinter.END)
    resultEntry.insert(0, round(amount * conversionmultiplier, 2))


# Programm
print("Programm gestartet! mit Startwährung: ")

# GUI
mainWindow = tkinter.Tk()

mainWindow.title('Währungsumrechner')
mainWindow.geometry("600x450")

mainTitle = tkinter.Label(mainWindow, text='Bitte wählen Sie die Währungen aus und tragen Sie einen Wert ein!')
mainTitle.place(x=0, y=50, width=600)

subTitle = tkinter.Label(mainWindow, text='Zum umrechnen Enter drücken!')
subTitle.place(x=0, y=350, width=600)

# Währungsauswahl-Variabeln
origin_currency_var = tkinter.StringVar(mainWindow)
origin_currency_var.set('USD')
target_currency_var = tkinter.StringVar(mainWindow)
target_currency_var.set('EUR')

# Startwährung Switcher
origin_currency_label = tkinter.Label(mainWindow, text='Währung von:')
origin_currency_label.place(x=200, y=100, width=100)
origin_currency_picker = tkinter.OptionMenu(mainWindow, origin_currency_var, 'USD', 'EUR', 'TRY', 'CHF', 'JPY')
origin_currency_picker.place(x=300, y=100, width=100)

# Zielwährung Switcher
target_currency_label = tkinter.Label(mainWindow, text='Währung nach:')
target_currency_label.place(x=200, y=150, width=100)
target_currency_picker = tkinter.OptionMenu(mainWindow, target_currency_var, 'EUR', 'USD', 'TRY', 'CHF', 'JPY')
target_currency_picker.place(x=300, y=150, width=100)

# Betrag
amountLabel = tkinter.Label(mainWindow, text='Betrag:')
amountLabel.place(x=200, y=250, width=100)
amountEntry = tkinter.Entry(mainWindow)
amountEntry.place(x=300, y=250, width=100)

# Ergebnis
resultLabel = tkinter.Label(mainWindow, text='Ergebnis:')
resultLabel.place(x=200, y=300, width=100)
resultEntry = tkinter.Entry(mainWindow)
resultEntry.place(x=300, y=300, width=100)

# Berechne, wenn Enter gedrückt wird
mainWindow.bind('<Return>', lambda event=None: calculate())


# Initialisierung Programmfenster
mainWindow.mainloop()
