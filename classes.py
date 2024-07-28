#!/usr/bin/env python
# coding: utf-8

# ### Criando classes

import pyautogui
import pyperclip
import time

# ### Refatorando com classe

class Controlador():
    def __init__(self):
        pyautogui.PAUSE = 1
    def abrir_programa(self, nome_programa):
        pyautogui.press("win")
        pyautogui.write(nome_programa)
        pyautogui.press("enter")
    def escrever(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")
    def escrever_e_enter(self, texto):
        self.escrever(texto)
        pyautogui.press("enter")
        self.aguardar()
    def entrar_site(self, site, espera=3):
        self.escrever_e_enter(site)

    def aguardar(self, tempo=2):
        time.sleep(tempo)
    def clicar(self, pos_x, pos_y, botao="left"):
        self.aguardar()
        pyautogui.click(pos_x, pos_y, button=botao)
    def pegar_posicao(self):
        for i in range(5):
            print(f"pegando posicao em {5 - i} segundos")
            time.sleep(1)

        print(pyautogui.position())

    def extrair_link(self, pos_x, pos_y):
        self.clicar(pos_x, pos_y, botao="right")
        pyautogui.press("up")
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press("enter")
        texto = pyperclip.paste()
        print(texto)

    def trocar_janela(self):
        self.aguardar()
        pyautogui.hotkey("alt","tab")





robozinho = Controlador()

robozinho.abrir_programa('chrome')

robozinho.clicar(615, 605)

robozinho.entrar_site('https://www.youtube.com/')

robozinho.clicar(598, 139)

robozinho.escrever_e_enter('gojo vs sukuna')

robozinho.aguardar()

robozinho.extrair_link(639, 407)

robozinho.trocar_janela()


robozinho.clicar(447, 779)

robozinho.clicar(1220, 820)