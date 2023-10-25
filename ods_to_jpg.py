import ezodf
import  jpype     
import  asposecells 
import os    
jpype.startJVM() 
from asposecells.api import Workbook, ImageOrPrintOptions, PdfSaveOptions, ImageSaveOptions, ImageFormat, SaveFormat
from PIL import Image, ImageDraw 
import time

org_ods_file_path = 'templates_ods/invoice_template_1.ods'
ods_value_path = 'templates_ods/values.ods'
template_name = 'invoice_template_1'

def check_create_folder(path):
    mode = 0o666
    if not os.path.exists(path):  
        os.mkdir(path, mode)

data_doc = ezodf.opendoc(ods_value_path)
# for sheet in doc.sheets:
#    print(sheet.name)
data_sheet = data_doc.sheets[0]
# print(sheet.nrows())
# print(sheet.ncols())
print("Total Invoice Data:", (data_sheet.nrows() - 2))

timestamp = int(time.time())
invoice_path = 'invoice_jpg_output/' + str(timestamp)
check_create_folder(os.path.join(invoice_path))

for i_row in range(data_sheet.nrows()-2):
    
    workbook = Workbook(org_ods_file_path)
    # worksheet = workbook.worksheets[0]
    # cells = worksheet.cells
    for i_col in range(data_sheet.ncols()-2):
        if data_sheet[i_row+1, i_col].value:
            workbook.getWorksheets().get(0).getCells().get(data_sheet[0, i_col].value).putValue(str(data_sheet[i_row+1, i_col].value))
    # print(cells.get("A2"))
    # print(cells.get("B2"))
    # saveOptions = ImageSaveOptions(SaveFormat.JPG)
    # # Set image-related options
    # saveOptions.setMergeAreas(0)
    # workbook.save("Output.jpg", saveOptions)

    workbook.save(invoice_path + "/" + template_name + "_output_" + str(i_row + 1) + ".jpg")

    # saveOptions = PdfSaveOptions()
    # saveOptions.setOnePagePerSheet(True)
    # workbook.save("Output.pdf", saveOptions)
jpype.shutdownJVM()
print("PATH: ", invoice_path)
print("DONE")

