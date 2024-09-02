from init import *
from datetime import datetime
import pandas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register DejaVuSans font
pdfmetrics.registerFont(TTFont('DejaVuSans', 'dejavu-fonts/ttf/DejaVuSans.ttf'))

# Load Excel or ODS file
def load_data(file_path):
    if file_path.endswith('.xlsx'):
        df = pandas.read_excel(file_path)
    elif file_path.endswith('.ods'):
        df = pandas.read_excel(file_path, engine='odf')
    else:
        raise ValueError("Formát súboru nie je podporovaný. Podporované súbory sú Excel (.xlsx) alebo ODS (.ods).")
    return df

# Function to format date columns
def format_dates(df, date_columns):
    for col in date_columns:
        if col in df.columns:
            df.loc[:, col] = pandas.to_datetime(df[col], errors='coerce').dt.strftime('%d.%m.%Y')
    return df

def replace_nan_with_empty(df):
    return df.fillna('')

# Create a PDF from the DataFrame
def create_pdf(df, output_pdf_path, columns):
    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Chýbajú Vám tieto stĺpce: {', '.join(missing_columns)}.")

    # Initialize PDF document
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter, topMargin=50, bottomMargin=30)
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=13,
        alignment=1,  # Center alignment
    )
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontName='DejaVuSans',
        fontSize=10,
        alignment=1,  # Center alignment
    )

    # Add titles to elements
    elements.append(Paragraph(title1, title_style))
    elements.append(Spacer(1, 5))
    elements.append(Paragraph(title2, subtitle_style))
    elements.append(Paragraph(title3, subtitle_style))
    elements.append(Spacer(1, 8))

    filtered_df = df[columns]
    date_columns = ['Dátum narodenia']  # List of columns that need date formatting
    filtered_df = format_dates(filtered_df, date_columns)

    # Replace NaN values with empty strings
    filtered_df = replace_nan_with_empty(filtered_df)

    data = [filtered_df.columns.tolist()] + filtered_df.values.tolist()

    # Create table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#d5d5d5'),
        ('GRID', (0, 0), (-1, -1), 1, 'black'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))

    elements.append(table)

    # Build PDF
    doc.build(elements)
    print(f"PDF súbor s názvom {output_pdf_path} vytvorený.")


def get_user_input():
    available_columns = [
        'Izba', 'Škola', 'Trieda', 'Bydlisko', 'Dátum narodenia', 'Telefónne číslo', 'Matka', 'Otec', 'Triedny', 'Triedny telefón', 'Tréner', 'Tréner telefón', 'Aktivita',
    ]
    print("Prosím vyberte maximum 4 stĺpce s daného listu: (P.č. a Priezvisko a meno sú vybrané automaticky)")

    for i, column in enumerate(available_columns, start=1):
        print(f"{i}. {column}")

    selected_indices = input("Vložte Váš výber oddelený čiarkou (e.g., 1,3,5): ").strip().split(',')
    selected_indices = [int(index) for index in selected_indices if index.isdigit()]

    if len(set(selected_indices)) > 4:
        print("Môžete vybrať maximálne 3 stĺpce. Skúste to znova.")
        return 0

    selected_columns = ['P.č.', 'Priezvisko a meno',]
    for i in selected_indices:
        if 1 <= i <= len(available_columns) and available_columns[i - 1] not in selected_columns:
            selected_columns.append(available_columns[i - 1])
        if i > len(available_columns):
            print(f"Stĺpec s číslom {i} nebol na výber. Skúste to znova.")
            return 0

    return selected_columns

def generate_unique_filename(base_name, extension='pdf'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_filename = f"{base_name}_{timestamp}.{extension}"
    return unique_filename

# Main function
def excel_to_pdf(input_file):
    base_output_name = 'generated'
    while True:
        try:
            columns = get_user_input()
            if columns == 0:
                continue
            if len(columns) == 2:
                print("Nevybrali ste žiadne stĺpce. Skúste to znova.")
                continue

            df = load_data(input_file)

            output_pdf = generate_unique_filename(base_output_name)
            create_pdf(df, output_pdf, columns)

            continue_choice = input(
                "Chcete si vytvoriť ďalšie pdf? (a/n): ").strip().lower()
            if continue_choice != 'a':
                print("Koniec programu.")
                break
        except Exception as e:
            print(f"Error pri vykonávaní kódu: {e}")

excel_to_pdf(input_file)
