# AutoClicker
**`OBS: O aplicativo ainda está em desenvolvimento e sofrerá alterações significativas.`**<br><br>
Um autoclicker simples e eficiente feito em **Python** utilizando principalmente **PySide6** e **pynput**. O aplicativo oferece duas funcionalidades principais:

1. **AutoClicker para Mouse**: Realiza cliques contínuos na tela com uma taxa configurável por segundo.
2. **AutoClicker para Teclado**: Pressiona uma ou duas teclas alternadas em uma taxa de cliques também configurável.

## 💻 Funcionalidades
- **Modo de clique do mouse**: Configure a taxa de cliques por segundo e uma tecla (bind) para ativação/desativação.
- **Modo de clique do teclado**: Pressione uma ou duas teclas de forma automática, com taxa ajustável, e controle o funcionamento por meio de uma bind.
- **Interface intuitiva**: Fácil de usar e personalizar, com configurações salvas automaticamente.

## 🛠️ Guia de Instalação:
### Versão compilada:
- Se você não deseja instalar o Python e compilar, você pode baixar a versão final [**clicando aqui**](https://github.com/mtzdev/auto-clicker/releases).
### Versão com compilação manual:
- Para compilar o projeto, é necessário ter **Python 3 instalado** (recomendado versão 3.7 ou superior).
1. **Clone o projeto**: Use o comando abaixo para clonar o projeto:
```
git clone https://github.com/mtzdev/auto-clicker.git
```
2. **Instalar as dependências**: Use o seguinte comando na pasta do projeto:
```
pip install -r requirements.txt
```
3. **Compilação do projeto**: Após instalar todas as dependências, utilize o comando abaixo para compilar:
```
pyinstaller --onefile --noconsole main.py
```
4. **Acessar o executável**: Após compilar, o arquivo executável estará na pasta `dist/`
5. **Executar o programa**: Agora você pode abrir o programa sem precisar do Python e dos outros arquivos!

## 📜 Licença
Este projeto está licenciado sob a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/)
É proibido o uso para fins comerciais sem minha permissão explícita.

## 🤝Contribuições
Sinta-se a vontade para contribuir com atualizações! Se você encontrar bugs ou tiver sugestões, abra uma issue ou faça um pull request!

