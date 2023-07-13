import requests
from tkinter import *


def get_quotation():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    request_dic = request.json()

    dolar_quotation = request_dic['USDBRL']['bid']
    euro_quotation = request_dic['EURBRL']['bid']
    btc_quotation = request_dic['BTCBRL']['bid']

    text = f'''
    Dolar: {dolar_quotation}
    Euro: {euro_quotation}
    BTC: {btc_quotation}'''

    quotation_text["text"] = text


window = Tk()
window.title('Current currency quote')
window.geometry("400x400")

orientation_text = Label(window, text="Click on the button to display the currency quote")
orientation_text.grid(column=0, row=0, padx=10, pady=10)

button_click = Button(window, text="Get quotes Dolar/Euro/BTC", command=get_quotation)
button_click.grid(column=0, row=1, padx=10, pady=10)

quotation_text = Label(window, text='')
quotation_text.grid(column=0, row=2, padx=10, pady=10)


window.mainloop()