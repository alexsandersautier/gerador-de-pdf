import library as pdf
import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [
    [sg.Text('Digite o que gostaria de transformar em PDF: ')],
    [sg.Input(key='texto')],
    [sg.Button(button_text='Adicionar texto ao PDF', key='add')],
    [sg.Text('Titulo do cabeçalho: ')],
    [sg.Input(key='title')],
    [sg.Text('Titulo do Texto: ')],
    [sg.Input(key='text_title')],
    [sg.Text('Digite o caminho para salvar o PDF:')],
    [sg.Input(key='caminho_pdf'), sg.FileSaveAs(button_text='Salvar em...')],    
    # [sg.Input(key='imagem'),sg.FileBrowse(button_text='Escolher Imagem')],
    [sg.Button(button_text='Gerar PDF')]
]

window = sg.Window('Gerador de PDF', layout=layout)
text = ''
while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'add':
       text += values['texto'] + '\n' 
    elif event == 'Gerar PDF':
        title = values['title']
        text_title = values['text_title']
        file_name = values['caminho_pdf']
        pdf.criar_pdf(text,title,text_title,file_name=file_name)
        break


