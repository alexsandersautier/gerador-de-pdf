from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, title):
        super().__init__()  
        self.title = title
        self.unit = 'cm'
        # self.imagem = image  

    def set_unit(self, unit):
        self.unit = unit

    def header(self):
        self.image('C:\\Users\\Alexsander\\Documents\\mestre-pythonista\\pdf-projects\\project2\\paganismo-nordico.png', x=1.2, h=0.8)
        self.ln(0.1)
        self.set_font("helvetica", "B", 12)
        self.cell(w=0, h=1, txt=self.title, align="l", new_x="LMARGIN", new_y="NEXT")
        self.ln(0.1)

    def footer(self):
        self.set_y(-1.5)
        self.set_font("helvetica", "i", 8)
        self.cell(w=0, h=1, txt=f"Page {self.page_no()}/{{nb}}", align="C")

def criar_pdf(texto, title,text_title,file_name):
    pdf = PDF(title=title)
    pdf.set_unit("cm")  # Define a unidade de medida para centímetros
    pdf.add_page()
    pdf.set_font("Times", "B", size=17)
    pdf.cell(w=0, h=5, txt=text_title, align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font("Times", size=12)

    pdf.multi_cell(w=0, h=10, txt=texto, align='j', new_x='LMARGIN', new_y='NEXT')
    pdf.output(file_name)
