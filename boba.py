from tkinter import font
import PySimpleGUI as sg


consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"


#TODAS PALAVRAS COM X NO MEIO

muitoespecial = {
    "o" : "u",
    "e" : "i",
    "l" : "w",
    "u" : "w",
}

phonetics_solo = {
    "b": "be",
    "c": "se",
    "d": "de",
    "e": "e",
    "f": "ɛfi",
    "g": "ʒe",
    "h": "aga",
    "i": "i",
    "j": "ʒɔtə",
    "k": "ka",
    "l": "ɛli",
    "m": "emi",
    "n": "eni",
    "o": "ɔ",
    "p": "pe",
    "q": "ke",
    "r": "ɛr̄i",
    "s": "ɛsi",
    "t": "te",
    "u": "u",
    "v": "ve",
    "w": "dablju",
    "x": "ʃis",
    "y": "ipsilõw",
    "z": "ze",
}

convertion = {
    "sa" : "za",
    "se" : "ze",
    "si" : "zi",
    "so" : "zo",
    "su" : "zu",
    "j" : "ʒ",
    "sc" : "s",
    "sç" : "s",
    "aix" : "ajʃ",
    "eix" : "ejʃ",
    "oux" : "owʃ",
    "enx" : "ẽʃ",
    "ge" : "ʒe",
    "gi" : "ʒi",
    "ce" : "se",
    "ci" : "si",
    "x" : "ks",
    "gui" : "gi",
    "xc" : "s",
    "qui" : "ki",
    "gue" : "ge",
    "que" : "ke",
    "am" : "ɐm",
    "an" : "ɐn",
    "é" : "ɛ",
    "ch" : "ʃ",
    "xa" : "ʃa",
    "xe" : "ʃe",
    "xi" : "ʃi",
    "xo" : "ʃo",
    "xu" : "ʃu",
    "ó" : "ɔ",
    "lh" : "λ",
    "di" : "dʒ",
    "nh" : "ɲ",
    "c" : "k",
    "ss" : "s",
    "rr" : "r̄",
    "on" : "õ",
    "om" : "õ",
    "um" : "ũ",
    "un" : "ũ",
    "ô" : "o",
    "oi" : "oj",
    "ui" : "uj",
    "ai" : "aj",
    "en" : "ẽ",
    "ú" : "u",
    "í" : "i",
    "çe" : "se",
    "ça" : "sa",
    "çu" : "su",
    "ei" : "ej",
    "ç" : "s"

}

font= ("Arial", 40)

layout = [[sg.Text("Frase que deseja transcrever:", font=font, size=(30, 1), text_color="black")], 
[sg.Input(key="input", font=("Arial", 25))], [sg.Button("Traduzir", key="TRADUZIR", font=("Arial", 15))],
[sg.Text("Frase Transcrita:", font=("Helvetica", 20), text_color="black")],
[sg.Text(key="resultado", font=font, text_color="black", visible=False)],

]

window = sg.Window("Transcritor Fonético", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif "TRADUZIR":
        new_string = values["input"].lower()

        if len(new_string) > 0:

            for case in muitoespecial: #esse for aqui é só pras ultimas letras que sao demonia (e, l, i, u, w)

                if new_string[0] == "s":
                    new_string[0] == "s"
                    break

                elif new_string[-2] not in consonants and new_string[-1] == "o":
                    new_string = new_string[:-1] + "w"
                    break

                elif new_string[-1] == "u" and new_string [-2] not in vowels:
                    new_string[-1] == "u"
                    break

                elif new_string[-1] == "o":
                    new_string = new_string[:-1] + "u"
                    break
                
                elif new_string[-1] == case:
                    new_string = new_string[:-1] + muitoespecial[case]
                    break
                
            for case in phonetics_solo: #isso aqui é pra traduzir as letras sozinhas
                if new_string.replace(" ", "") == case:
                    new_string = phonetics_solo[case]

            for case in convertion: #isso aqui é a conversao final
                if case in new_string:
                    print("antes da conversao:", new_string, case)
                    new_string = new_string.replace(case, convertion[case])
                    print("depois da conversao:",new_string, case)
         
        window["resultado"].Update(new_string, visible=True)

            
        

window.close()
