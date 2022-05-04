
import pdfplumber

# TODO: Get this table extraction to work!

table_params = {
    "vertical_strategy": "text",
    "horizontal_strategy": "lines",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    "snap_tolerance": 3,
    "snap_x_tolerance": 3,
    "snap_y_tolerance": 3,
    "join_tolerance": 3,
    # "join_x_tolerance": 3,
    # "join_y_tolerance": 3,
    "edge_min_length": 3,
    "min_words_vertical": 3,
    "min_words_horizontal": 1,
    "keep_blank_chars": False,
    "text_tolerance": 3, # was 3
    # "text_x_tolerance": 3,
    # "text_y_tolerance": 3,
    "intersection_tolerance": 3,
    "intersection_x_tolerance": 3,
    "intersection_y_tolerance": 3,
}

with pdfplumber.open("../files/anglian-water-climate-change-adaptation-report-2020.pdf") as pdf:
    # for page in pdf.pages:
    for i, page in enumerate(pdf.pages):

        tables = page.extract_tables(table_params)
        # if tables
        if i == 22:
            break
tables



import fitz

doc_text = []
with fitz.open("../files/anglian-water-climate-change-adaptation-report-2020.pdf") as doc:
    for i, page in enumerate(doc):
        text = page.get_text()
        # if i == 2:
            # break
        doc_text.append(text)

