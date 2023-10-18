import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook, ImageOrPrintOptions, PdfSaveOptions, ImageSaveOptions, ImageFormat, SaveFormat

workbook = Workbook("input.ods")

# options = ImageOrPrintOptions()
# options.setHorizontalResolution(300)
# options.setVerticalResolution(300)


# saveOptions = ImageSaveOptions(SaveFormat.JPG)
# saveOptions.setOnePagePerSheet(True)
# Create an instance of ImageSaveOptions with the desired image format (JPEG)
# image_options = ImageSaveOptions(SaveFileFormat.PNG)

# # # Set image-related options
# saveOptions.scale =5  # Set image quality (0-100, 100 being the best)
# saveOptions.setMergeAreas(0)
# workbook.save("Output.jpg", saveOptions)

saveOptions = PdfSaveOptions()
saveOptions.setOnePagePerSheet(True)
workbook.save("Output.pdf", saveOptions)

jpype.shutdownJVM()