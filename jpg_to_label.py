import xml.etree.ElementTree as ET
import glob
import os
# filename.text = 'Template-' + str(n_file+1) + '_' + str(n_dup) + '.jpg'
# for n_file in range(25):

jpg_path = 'invoice_jpg_output/1698249175'
system_path = 'C:\\Users\\Yenmin\\Documents\\Project\\AIInvoice\\invoice_jpg_output\\1698249175\\'
template_name = 'invoice_template_1'

path = os.path.join(os.getcwd(), (jpg_path))
jpg_count = int(len(glob.glob(path + '/*.jpg')))
for n_dup in range(jpg_count):
    mytree = ET.parse('invoice_sample_label/Output_1.xml')
    myroot = mytree.getroot()
    filename = myroot.find(".//filename")
    filename.text = template_name + '_output_' + str(n_dup + 1) + '.jpg'
    path = myroot.find(".//path")
    path.text = system_path + filename.text
    mytree.write(jpg_path + '/' + template_name + '_output_' + str(n_dup + 1) + '.xml')