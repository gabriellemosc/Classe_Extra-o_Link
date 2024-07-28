Aqui está um exemplo de um README para o seu repositório no GitHub:

---

# Controlador de Automação com PyAutoGUI

Este repositório contém um script Python para automação de tarefas usando a biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/). O script automatiza a interação com o sistema operacional e um navegador para extrair links de páginas da web.

## Funcionalidades

- **Abrir Programa**: Inicia um programa especificado.
- **Escrever Texto**: Insere texto usando a área de transferência.
- **Escrever e Pressionar Enter**: Insere texto e pressiona Enter.
- **Entrar em Site**: Acessa um site no navegador.
- **Aguardar**: Faz uma pausa por um período especificado.
- **Clicar**: Clica em uma posição específica na tela.
- **Pegar Posição**: Obtém a posição atual do cursor do mouse.
- **Extrair Link**: Copia um link da área de contexto do navegador.
- **Trocar Janela**: Alterna entre janelas abertas.

## Como Usar

1. **Instale as dependências**:
   Certifique-se de que você tem o Python instalado e, em seguida, instale as bibliotecas necessárias:
   ```bash
   pip install pyautogui pyperclip
   ```

2. **Execute o Script**:
   Execute o script para iniciar a automação. O script abre o navegador, faz uma busca no YouTube e extrai um link de um vídeo específico.
   ```bash
   python seu_script.py
   ```

## Código

Aqui está um exemplo do código principal:

```python
import pyautogui
import pyperclip
import time

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
        for _ in range(8):
            pyautogui.press('up')
        pyautogui.press("enter")
        texto = pyperclip.paste()
        print(texto)

    def trocar_janela(self):
        self.aguardar()
        pyautogui.hotkey("alt", "tab")

# Exemplo de uso
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
```

## Observações

- O script assume que o navegador e os programas são iniciados e controlados em uma resolução de tela padrão. Ajustes podem ser necessários para diferentes resoluções ou configurações de sistema.
- Certifique-se de que o foco está na janela correta ao executar as ações de clique e digitação.
