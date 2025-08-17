import tkinter as tk
from tkinter import messagebox

from micro_apps.random_card.decks import Deck
from micro_apps.random_card.settings import *


def clear_global_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

def show_remaining_block(deck):
    remaining_cards = tk.Frame(master=frame, width=100, height=100, pady=10, padx=10, )
    remaining_cards_label_1 = tk.Label(master=remaining_cards, text="Осталось карт:", font=('Arial', 12))
    remaining_cards_label_1.grid(row = 0, column = 0, )
    remaining_cards_label_2 = tk.Label(master=remaining_cards, text=len(deck), font=('Arial', 15),)
    remaining_cards_label_2.grid(row = 1, column = 0, )
    remaining_cards.grid(row = 2, column = 0,  )

def show_current_block(card):
    color = 'red'
    if card.suit == '♠' or card.suit == '♣':
        color = 'black'
    
    pulled_card = tk.Frame(master=frame, width=100, height=100, bg='white', borderwidth=3, relief="ridge", pady=10)
    pulled_card.grid(row = 2, column = 1, )
    value_label = tk.Label(master=pulled_card, text=card.rank, font=('Arial', 30,), padx=normal_padding, bg='white', width=2, fg=color, )
    value_label.grid(sticky='', )
    suit_label = tk.Label(master=pulled_card, text=card.suit, font=('Arial', 40), padx=normal_padding, bg='white', fg=color, )
    suit_label.grid(sticky='')

def get_card(deck):
    if len(deck) == 0:
        messagebox.showinfo("Карты закончились!", "Вам нужно взять нувую колоду!")
    card = deck.get_card()
    show_remaining_block(deck)
    show_current_block(card)


def create_deck():
    clear_global_widgets()
    deck = Deck(radio_var.get())
    show_remaining_block(deck)

    pull_card_btn = tk.Button(master=frame, text="Взять карту", command = lambda: get_card(deck),  font=('Arial', 12),)
    pull_card_btn.grid(row = 1, column = 1, )

if __name__ == '__main__':
    window = tk.Tk()

    frame = tk.Frame(master=window,  )
    frame.pack(expand=True, fill=tk.BOTH)

    deck_type_label = tk.Label(master=frame, text=deck_type_text, padx=normal_padding)
    deck_type_label.grid(row = 0, column = 0)

    radio_var = tk.StringVar()
    radio_var.set(deck_36)
    deck_36_radio = tk.Radiobutton(master=frame, text=deck_36, variable=radio_var, value=deck_36)
    deck_36_radio.grid(row = 0, column = 1)
    deck_52_radio = tk.Radiobutton(master=frame, text=deck_52, variable=radio_var, value=deck_52)
    deck_52_radio.grid(row = 0, column = 2)

    create_deck_btn = tk.Button(master=frame, text=shuffle_card_text, command=create_deck)
    create_deck_btn.grid(row = 1, column = 0,  pady = normal_padding, padx = normal_padding)

    global_widgets = frame.winfo_children()

    window.title(app_title)
    window.geometry(window_size)
    window.mainloop()
