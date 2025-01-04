from tkinter import *;
from tkinter import ttk;
from tkinter.ttk import Progressbar;
from tkinter import messagebox;
from PIL import Image, ImageTk;
from random import *;
from paises import *;

# Paleta de Cores
co0 = "#444466";
co1 = "#feffff";
co2 = "#6f9fbd";
co3 = "#38576b";
co4 = "#403d3d";
fundo_cima = "#2aa6a8";
fundo = co1;
cor1 = "#f0ba4f";

# Global variables
global pontos, vida, nome_do_pais, img_bandeira;
pontos = 0;
vida = 3;

janela = Tk();
janela.title("Advinhe o País");
janela.geometry("350x310");
janela.configure(bg=co1)

# Separator entre Frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, padx=172);

# Frames

frame_cima = Frame(janela, width=350, height=60, bg=fundo_cima, pady=0, padx=0, relief=FLAT);
frame_cima.grid(column=0, row=1);

frame_baixo = Frame(janela, width=350, height=300, bg=co1, pady=0, padx=0, relief=FLAT);
frame_baixo.grid(column=0, row=2, sticky=NW);

app_nome = Label(frame_cima, text="QUAL O PAÍS?", relief=FLAT, anchor=CENTER, font=("Fixedsys 20"), bg=fundo_cima, fg=co1);
app_nome.place(x=15, y=15)

# Styles
style = ttk.Style(janela);
style.theme_use('default');
style.configure("black.Horizontal.TProgressbar", background="#fcc058");
style.configure("TProgressbar", thickness=5);

# Progress Bar
bar = Progressbar(frame_baixo, length=293, style="black.Horizontal.TProgressbar");
bar.place(x=27, y=58);
bar['value'] = pontos;

# Label de Pontuação
l_score = Label(frame_baixo, text="Pontuação: "+str(pontos), font=('System 17'), bg=fundo, fg=co0);
l_score.place(x=27, y=10)

# Imagens de Vida
img_0 = Image.open('vida-perdida.png');
img_0 = img_0.resize((30, 30));
img_0 = ImageTk.PhotoImage(img_0);

img_1 = Image.open('vida-cheia.png');
img_1 = img_1.resize((30, 30));
img_1 = ImageTk.PhotoImage(img_1);

# Icones de Vida
l_icon_1 = Label(frame_baixo, image=img_1, bg=fundo);
l_icon_1.place(x=229, y=10);

l_icon_2 = Label(frame_baixo, image=img_1, bg=fundo);
l_icon_2.place(x=259, y=10);

l_icon_3 = Label(frame_baixo, image=img_1, bg=fundo);
l_icon_3.place(x=289, y=10);

# Label de perguntas
l_pergunta = Label(frame_baixo, text="Qual país pertence essa bandeira?", pady=0, padx=0, relief=FLAT, anchor=CENTER, font=('Iby 10 bold'), bg=co1, fg=co4);
l_pergunta.place(x=30, y=70);

# Input de Resposta
input_resposta = Entry(frame_baixo, width=15, justify=CENTER, font=("", 12), highlightthickness=1, relief=SOLID);
input_resposta.place(x=178, y=100);

def IniciarJogo():
    # Dados do Jogo
    global pontos, vida, nome_do_pais, l_icon_bandeira, img_bandeira
    dados = DadosPais();
    nome_do_pais = dados[1];
    imagem = dados[0];

    # Imagem bandeira
    img_bandeira = Image.open(imagem);
    img_bandeira = img_bandeira.resize((140, 100));
    img_bandeira = ImageTk.PhotoImage(img_bandeira);

    l_icon_bandeira = Label(frame_baixo, image=img_bandeira, bg=fundo, relief=SOLID)
    l_icon_bandeira.place(x=30, y=100);

def ReiniciarJogo():
    global pontos, nome_do_pais, vida, img_0, img_1;

    # Resetar dados do jogo
    pontos = 0;
    vida = 3;
    bar['value'] = pontos;
    l_score.configure(text="Pontuação: "+str(pontos));
    l_icon_1['image'] = img_1;
    l_icon_2['image'] = img_1;
    l_icon_3['image'] = img_1;

    IniciarJogo();

def GameOver():
    global pontos, nome_do_pais, vida, img_0, img_1;

    pontos = 0;
    vida= 3;
    bar['value'] = pontos
    l_score.configure(text="Pontuação: "+str(pontos));
    l_icon_1['image'] = img_1;
    l_icon_2['image'] = img_1;
    l_icon_3['image'] = img_1;

    IniciarJogo()

def Verificar():
    global pontos, vida;

    # Validar Resposta
    resposta = input_resposta.get();
    if resposta == nome_do_pais:
        pontos += 10;
        l_score.configure(text="Pontuação: " + str(pontos));
        bar["value"] = pontos;
    else:
        messagebox.showerror("Erro", "Resposta está Incorreta!");
        vida -= 1
        if vida == 2:
            l_icon_1['image'] = img_0;
        if vida == 1:
            l_icon_2['image'] = img_0;
        if vida == 0:
            l_icon_3['image'] = img_0;
        if vida == -1:
            messagebox("Game Over", "Fim de jogo!");
            GameOver();
    
    # Resetar Input
    input_resposta.delete(0, END);

    # Verificar se Venceu
    if bar["value"] == 100:
        messagebox.showinfo("Parabéns", "Parabens você venceu o jogo");
        ReiniciarJogo()
    else:
        IniciarJogo()

# Botão Iniciar
b_resposta = Button(frame_baixo, text="Confirmar", width=10, height=1, bg=co1, fg=co4, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=Verificar);
b_resposta.place(x=210, y=150);

IniciarJogo()
janela.mainloop();