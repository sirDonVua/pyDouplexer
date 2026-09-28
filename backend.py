import pymupdf as pd
import os
from pathlib import Path

home = Path.home()
path = f"{home}/pyDouplexer/" 
if os.path.exists(path) is False :
    os.mkdir(path)


def NUp(filename: str, rtl: bool):

    srcFile = pd.open(filename)  # opens the pdf file
    output = pd.open()

    h, w = pd.paper_size("a4")
    leftRect = pd.Rect(0, 0, w / 2, h)  # creating the top rectangle
    rightRect = pd.Rect(w / 2, 0, w, h)  # creating the bottom rectangle

    if rtl == True:
        rect = [rightRect, leftRect]
    else:
        rect = [leftRect, rightRect]

    for spage in srcFile:
        if spage.number % 2 == 0:
            page = output.new_page(-1, width=w, height=h)
        page.show_pdf_page(rect[spage.number % 2], srcFile, spage.number)

    output.save(f"{path}output.pdf", garbage=3, deflate=True)
    print("Finished")


def split(srcFile):

    srcFile = pd.open(srcFile)
    h, w = pd.paper_size("a4")
    if srcFile.page_count % 2 != 0:
        srcFile.new_page(-1, width=w, height=h)

    evenDoc = pd.open()
    evenDoc.insert_pdf(srcFile)

    oddDoc = pd.open()
    oddDoc.insert_pdf(srcFile)

    p_even = []
    p_odd = []

    for page in range(srcFile.page_count):
        if page % 2 == 0:
            p_even.append(page)
        elif page % 2 == 1:
            p_odd.append(page)

    oddDoc.select(p_odd)
    oddDoc.save(f"{path}odd.pdf")
    oddDoc.close()
    evenDoc.select(p_even)
    evenDoc.save(f"{path}even.pdf")
    print("Finished")
