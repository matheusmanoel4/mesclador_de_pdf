import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir('arquivos')
lista_arquivos.sort()


for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'arquivos/{arquivo}')
        
merger.write('arquivos/resultado.pdf')


#botao
merge_button = tk.Button(janela, text="Selecionar e Mesclar PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

