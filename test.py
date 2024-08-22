import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import ImageTk

#cores--------------------------------------------------------------------------------------------------------------
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"
co12 =  '#FF0000' #vermelho
#-------------------------------------------------------------------------------------------------------------------

# Função para mesclar PDFs------------------------------------------------------------------------------------------------
def merge_pdfs():
    merger = PyPDF2.PdfMerger()
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    
    if not files:
        messagebox.showwarning("Nenhum arquivo selecionado", "Por favor, selecione pelo menos dois arquivos PDF.")
        return
    
    for file in files:
        merger.append(file)
    
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    
    if output_path:
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Sucesso", f"Arquivos PDF foram mesclados com sucesso em {output_path}")



# Configuração da janela principal-------------------------------------------------------------------------------
janela = tk.Tk()
janela.title("Mesclador de PDFs")
janela.geometry("400x400")
janela.configure(background=co0)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')
#--------------------------------------------------------------------------------------------------------------------------------------------



#barra de cima----------------------------------------------------------------------------------------------------------------------------- 
barra_de_cima = tk.Frame(janela, width=400, height=50, bg=co12,)
barra_de_cima.grid(row=0 , column=0, columnspan=2)
#-----------------------------------------------------------------------------------------------------------------------------------------------



#nome do programa-----------------------------------------------------------------------------------------------------------
nome = tk.Label(barra_de_cima, text="Mesclador de PDFs", width=20, compound=tk.LEFT, anchor=tk.NW, font=("IVY 12 bold " ), bg=co12, fg=co1)
nome.pack(pady=10 , padx=120)
#-----------------------------------------------------------------------------------------------------------------------------------

#botão para selecionar e mesclar PDFs------------------------------------------------------------------------------------------------
botao_mesclar = tk.Button(janela, text="Selecionar e Mesclar PDFs", command=merge_pdfs, bg=co12, fg=co1, font=("Arial 12 bold"))
botao_mesclar.grid(pady=100, padx=20)
#-----------------------------------------------------------------------------------------------------------------------------------

#Preciso adicionar a logo.png na janela principal
#logo---------------------------------------------------------------------------------------------------------------
from PIL import Image, ImageTk
app_logo = Image.open("icone.png")
app_img = app_logo.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

logo_label = tk.Label(barra_de_cima, image=app_img, width=50, height=50, compound=tk.CENTER, anchor=tk.NW, bg=co0)
logo_label.image = app_img  # Manter uma referência da imagem
logo_label.grid( row=0, column=0, columnspan=1)






# Iniciar a interface gráfica
janela.mainloop()