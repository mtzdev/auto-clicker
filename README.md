# AutoClicker
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

## 💻 Como usar:
O AutoClick possui duas seções principais: Mouse e Teclado. Abaixo, a explicação para cada uma:
### 🖱 Mouse: Efetua cliques de mouse automaticamente
1. Defina a quantidade de cliques por segundo que o AutoClick deverá realizar.
2. Clique no botão para definir uma key-bind (tecla de ativação), e essa tecla será responsável por ligar/desligar o AutoClick.
3. Se quiser, pode mudar o lado do mouse que será efetuado os cliques (Esquerda/Direita)
4. Após a configuração, basta clicar na tecla escolhida que os cliques serão efetuados, e para desativar, basta pressiona-la novamente.

### ⌨ Teclado: Efetua cliques em uma tecla automaticamente
1. Configure quantos cliques por segundo o autoclick deverá realizar.
2. Clique no botão para definir uma key-bind que será a tecla responsável por ativar/desativar o Autoclick.
3. Escolha a tecla a ser pressionada automaticamente pelo Autoclick.
4. Agora basta clicar na tecla de key-bind que os cliques serão efetuados. Para desativar, clique na mesma tecla.

**OBS¹**: Você não pode usar a mesma tecla de ativação para o Mouse e Teclado.
<br>
**OBS²**: Caso você deseje desabilitar ou parar de usar uma das seções (Mouse ou Teclado), basta clicar no botão de escolher uma key-bind, e clicar em "Resetar/Desabilitar", assim você removerá a key-bind de ativação e essa seção não será mais ativada sem que você queira.
  

## 📜 Licença
Este projeto está licenciado sob a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/)
É proibido o uso para fins comerciais sem minha permissão explícita.

## 🤝Contribuições
Sinta-se a vontade para contribuir com atualizações! Se você encontrar bugs ou tiver sugestões, abra uma issue ou faça um pull request!

