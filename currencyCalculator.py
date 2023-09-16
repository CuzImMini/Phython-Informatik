import json
import tkinter
import requests


# Methode für API Zugriff
def getCurrencyConversion(currencyfrom, currencyto):
    # Abfrage API zu angegebener Währung
    if currencyfrom == 'EUR':
        request = requests.get('https://open.er-api.com/v6/latest/EUR')
    elif currencyfrom == 'USD':
        request = requests.get('https://open.er-api.com/v6/latest/USD')
    elif currencyfrom == 'TRY':
        request = requests.get('https://open.er-api.com/v6/latest/TRY')
    elif currencyfrom == 'CHF':
        request = requests.get('https://open.er-api.com/v6/latest/CHF')
    elif currencyfrom == 'JPY':
        request = requests.get('https://open.er-api.com/v6/latest/JPY')
    else:
        print("Fehler bei der API Anfrage!")
        return None

    # Konvertierung der API in JSON
    apijsondata = json.loads(request.content)
    # Abrufen des Umrechnungsfaktors für die angegebene Währung
    conversionmultiplier = apijsondata['rates'][currencyto]
    return conversionmultiplier


# Methode für API Prüfung
def checkAPI():
    # Abfrage API Code ob working
    request = requests.get('https://open.er-api.com/v6/latest/USD')
    if request.status_code == 200:
        return True
    else:
        return False


# Methode für Berechnung
def calculate():
    print('Berechnungen werden ausgeführt!')

    # Variablen von GUI
    currencyfromvalue = origin_currency_var.get()
    currencytovalue = target_currency_var.get()
    amount = amountEntry.get()

    # Konvertierung von Betrag in Zahl
    amount = float(amount)

    # Abrufen von Umrechnungsfaktor
    conversionmultiplier = getCurrencyConversion(currencyfromvalue, currencytovalue)

    # Löschen Ergebnis
    resultEntry.delete(0, tkinter.END)

    # Ergebnis einfügen#Einfügen Ergebnis
    if currencytovalue == 'EUR':
        resultEntry.insert(0, ' €')
    elif currencytovalue == 'USD':
        resultEntry.insert(0, ' $')
    elif currencytovalue == 'TRY':
        resultEntry.insert(0, ' ₺')
    elif currencytovalue == 'CHF':
        resultEntry.insert(0, ' CHF')
    elif currencytovalue == 'JPY':
        resultEntry.insert(0, ' ¥')

    resultEntry.insert(0, round(amount * conversionmultiplier, 2))


# Programm
print("Programm gestartet!")

# GUI
mainWindow = tkinter.Tk()
mainWindow.title('Währungsumrechner')
mainWindow.geometry("600x450")
mainWindow.resizable(False, False)

mainTitle = tkinter.Label(mainWindow, text='Bitte wählen Sie die Währungen aus und tragen Sie einen Wert ein!')
mainTitle.place(x=0, y=50, width=600)

subTitle = tkinter.Label(mainWindow, text='Zum umrechnen Enter drücken!')
subTitle.place(x=0, y=350, width=600)

# Währungsauswahl
origin_currency_var = tkinter.StringVar(mainWindow)
origin_currency_var.set('USD')
target_currency_var = tkinter.StringVar(mainWindow)
target_currency_var.set('EUR')

# Währungsauswahl von
origin_currency_label = tkinter.Label(mainWindow, text='Währung von:')
origin_currency_label.place(x=200, y=100, width=100)
origin_currency_picker = tkinter.OptionMenu(mainWindow, origin_currency_var, 'USD', 'EUR', 'TRY', 'CHF', 'JPY')
origin_currency_picker.place(x=300, y=100, width=100)

# Währungsauswahl nach
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

# Add a status indicator in the top right that turns green when the API is working
if checkAPI():
    statusIndicator = tkinter.Label(mainWindow, text='API bereit', bg='green')
else:
    statusIndicator = tkinter.Label(mainWindow, text='API Fehler', bg='red')
statusIndicator.place(x=500, y=0, width=100)

mainWindow.mainloop()
