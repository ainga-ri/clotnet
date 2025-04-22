from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from schemas.invoice import Invoice

class PDFCreator:
    # Create a PDF with A4 page size
    def __init__(self, filename: str):
        self.pdf = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4

    # Helper function to draw a line
    def draw_line(self, x1, y1, x2, y2):
        self.pdf.line(x1, y1, x2, y2)

    # Helper function to draw a rectangle (for tables or sections)
    def draw_rect(self, x, y, w, h):
        self.pdf.rect(x, y, w, h)

def company_details(pdf_creator):
    # Company details
    # Add company logo
    pdf_creator.draw_rect(50, pdf_creator.height - 275, 220, 175)
    # Draw white background rectangle first
    pdf_creator.pdf.setFillColor(colors.white)
    pdf_creator.pdf.rect(50, pdf_creator.height - 275, 220, 175, fill=True)
    # Then draw the image on top
    pdf_creator.pdf.drawImage("services/company_name.png", 50, pdf_creator.height - 230, width=210, height=155, preserveAspectRatio=True, mask='auto')
    pdf_creator.pdf.setFillColor(colors.black)  # Reset fill color back to black

    pdf_creator.pdf.setFont("Helvetica", 11)
    pdf_creator.pdf.drawString(60, pdf_creator.height - 210, "CARRER DEL CLOT 123-123")
    pdf_creator.pdf.drawString(60, pdf_creator.height - 230, "08027 BARCELONA")
    pdf_creator.pdf.drawString(60, pdf_creator.height - 250, "TEL: XXXXXXXXXX")
    pdf_creator.pdf.drawString(60, pdf_creator.height - 270, "EMAIL: <email_value>")

def customer_details(pdf_creator):
    # Customer details
    pdf_creator.draw_rect(350, pdf_creator.height - 275, 200, 110)
    pdf_creator.pdf.setFont("Helvetica", 15)
    pdf_creator.pdf.drawString(370, pdf_creator.height - 125, "SERVEIS INTEGRALS")
    pdf_creator.pdf.drawString(410, pdf_creator.height - 145, "DE NETEJA")
    pdf_creator.pdf.setFont("Helvetica", 10)
    pdf_creator.pdf.drawString(355, pdf_creator.height - 185, "COMUNIDAD DE PROPIETARIOS")
    pdf_creator.pdf.drawString(355, pdf_creator.height - 205, "CALLE MOSCU # 8")
    pdf_creator.pdf.drawString(355, pdf_creator.height - 225, "08005 – BARCELONA")
    pdf_creator.pdf.drawString(355, pdf_creator.height - 245, "<CIF VALUE>")
    pdf_creator.pdf.drawString(355, pdf_creator.height - 265, "<CIF VALUE>")

def invoice_number_and_date(pdf_creator, invoice_data: Invoice):    
    pdf_creator.draw_rect(50, pdf_creator.height - 360, 120, 20)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 315, "Nº FACTURA")
    pdf_creator.draw_rect(170, pdf_creator.height - 360, 100, 20)
    pdf_creator.pdf.drawString(245, pdf_creator.height - 315, str(invoice_data.number))
    
    pdf_creator.draw_rect(50, pdf_creator.height - 340, 120, 20)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 335, "FECHA FACTURA")
    pdf_creator.draw_rect(170, pdf_creator.height - 340, 100, 20)
    pdf_creator.pdf.drawString(217, pdf_creator.height - 335, invoice_data.invoice_date)
    
    pdf_creator.draw_rect(50, pdf_creator.height - 320, 120, 20)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 355, "ALBARÁN")
    pdf_creator.draw_rect(170, pdf_creator.height - 320, 100, 20)

def fill_concept_table_details(pdf_creator, invoice_data: Invoice):
    # Table headers
    pdf_creator.pdf.setFont("Helvetica-Bold", 10)
    pdf_creator.draw_rect(50, pdf_creator.height - 420, 300, 40)  # concepte row
    pdf_creator.pdf.drawString(170, pdf_creator.height - 400, "CONCEPTE")
    pdf_creator.draw_rect(50, pdf_creator.height - 560, 300, 140)  # concepte box
    
    pdf_creator.draw_rect(350, pdf_creator.height - 420, 100, 40)  # p/h row
    pdf_creator.pdf.drawString(390, pdf_creator.height - 400, "P/H")
    pdf_creator.draw_rect(350, pdf_creator.height - 560, 100, 140)  # concepte box
    
    pdf_creator.draw_rect(450, pdf_creator.height - 420, 100, 40)  # p/total row
    pdf_creator.pdf.drawString(480, pdf_creator.height - 400, "P/TOTAL")
    pdf_creator.draw_rect(450, pdf_creator.height - 560, 100, 140)  # concepte box

    # Table content
    create_description(pdf_creator, invoice_data)

def create_description(pdf_creator, invoice_data: Invoice):
    pdf_creator.pdf.setFont("Helvetica", 10)
    line_spacing = 15

    # variable
    if len(invoice_data.client_info.description) >= 50:
        pdf_creator.pdf.drawString(55, pdf_creator.height - 445, invoice_data.client_info.description[:50]) # analize last word to avoid cut
        pdf_creator.pdf.drawString(55, pdf_creator.height - 460, invoice_data.client_info.description[51:])
    else:
        pdf_creator.pdf.drawString(55, pdf_creator.height - 445, invoice_data.client_info.description[:50])
    
    # variable
    if len(invoice_data.client_info.description_street) >= 50:
        pdf_creator.pdf.drawString(55, pdf_creator.height - 485, invoice_data.client_info.description_street[:50])
        pdf_creator.pdf.drawString(55, pdf_creator.height - 500, invoice_data.client_info.description_street[51:])    
    else:
        pdf_creator.pdf.drawString(55, pdf_creator.height - 485, invoice_data.client_info.description_street[:50])
    
    # fixed
    pdf_creator.pdf.drawString(55, pdf_creator.height - 525, f"MES DE {invoice_data.month}")

    # pdf_creator.pdf.drawString(400, pdf_creator.height - 510, str(invoice_data.client_info.price_per_hour)) # not implemented yet
    pdf_creator.pdf.drawString(475, pdf_creator.height - 510, f"{invoice_data.client_info.total_price_description:.2f}")

def payment_details(pdf_creator, invoice_data: Invoice):
    # Payment and totals
    pdf_creator.pdf.setFont("Helvetica", 10)
    pdf_creator.draw_rect(350, pdf_creator.height - 600, 100, 25)  # net import box 
    pdf_creator.pdf.drawString(360, pdf_creator.height - 590, "IMPORTE NETO")
    
    pdf_creator.draw_rect(450, pdf_creator.height - 600, 95, 25)  # net import amount box 
    pdf_creator.pdf.drawString(475, pdf_creator.height - 590, f"{invoice_data.client_info.net_price:.2f} €")
    
    pdf_creator.draw_rect(350, pdf_creator.height - 625, 100, 25)  # iva box 
    pdf_creator.pdf.drawString(360, pdf_creator.height - 615, "IVA 21%")
    
    pdf_creator.draw_rect(450, pdf_creator.height - 625, 95, 25)  # iva value box 
    pdf_creator.pdf.drawString(475, pdf_creator.height - 615, f"{invoice_data.client_info.vat21:.2f} €")
    
    pdf_creator.draw_rect(350, pdf_creator.height - 650, 100, 25)  # import box  
    pdf_creator.pdf.drawString(360, pdf_creator.height - 640, "IMPORTE TOTAL")
    
    pdf_creator.draw_rect(450, pdf_creator.height - 650, 95, 25)  # import value
    pdf_creator.pdf.drawString(475, pdf_creator.height - 640, f"{invoice_data.client_info.total_price:.2f} €")

def bank_details(pdf_creator, invoice_data: Invoice):
    # Bank details
    pdf_creator.pdf.drawString(55, pdf_creator.height - 580, "CONDICIONES:")
    pdf_creator.pdf.drawString(200, pdf_creator.height - 580, invoice_data.client_info.condition)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 615, "VENCIMIENTO:")
    pdf_creator.pdf.drawString(200, pdf_creator.height - 615, invoice_data.deadline)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 650, "FORMA DE PAGO:")
    pdf_creator.pdf.drawString(200, pdf_creator.height - 650, invoice_data.client_info.payment_method)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 685, "CTA. CTE:")
    pdf_creator.pdf.drawString(200, pdf_creator.height - 685, invoice_data.client_info.account_number)
    pdf_creator.pdf.drawString(55, pdf_creator.height - 720, "IBAN:")
    pdf_creator.pdf.drawString(200, pdf_creator.height - 720, invoice_data.client_info.iban)

def footer(pdf_creator):
    margin = 50
    footer_box_length = 495
    footer_box_height = pdf_creator.height - 775
    width_box = 15
    pdf_creator.draw_rect(margin, footer_box_height, footer_box_length, width_box)  # Footer box
    
    pdf_creator.pdf.drawString(55, pdf_creator.height - 770, "ALFRED INGA RIOS")
    pdf_creator.pdf.drawString(485, pdf_creator.height - 770, "12345678-N")

class InvoiceData:
    
    def create_invoice(self, invoice_data: Invoice):
        pdf_creator = PDFCreator(filename=f"{invoice_data.number}.pdf")
        
        print("writting company details")
        company_details(pdf_creator)
        
        print("writting customer details")
        customer_details(pdf_creator)

        print("writting invoice number and date")
        invoice_number_and_date(pdf_creator, invoice_data)

        print("writting concept table details")
        fill_concept_table_details(pdf_creator, invoice_data)
        
        print("writting payment details")
        payment_details(pdf_creator, invoice_data)
        
        print("writting bank details")
        bank_details(pdf_creator, invoice_data)

        print("writting footer")
        footer(pdf_creator)
        
        # Save the PDF
        pdf_creator.pdf.save()
