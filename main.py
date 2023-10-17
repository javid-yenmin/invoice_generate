import ezodf
import shutil

# Specify the path to the ODS file you want to open and edit
org_ods_file_path = 'templates_ods/invoice_template_1.ods'
ods_value_path = 'templates_ods/values.ods'

data_doc = ezodf.opendoc(ods_value_path)
# for sheet in doc.sheets:
#    print(sheet.name)
data_sheet = data_doc.sheets[0]
# print(sheet.nrows())
# print(sheet.ncols())

for i_row in range(data_sheet.nrows()-2):
    ods_file_path = 'invoice_ods_output/invoice_template_1_out_' + str(i_row + 1) + '.ods'
    shutil.copy(org_ods_file_path, ods_file_path)

    # Open the ODS document
    update_doc = ezodf.opendoc(ods_file_path)

    # Select a specific sheet from the ODS document
    update_sheet = update_doc.sheets[0]  # Change the index to select a different sheet

    print(ods_file_path)
    for i_col in range(data_sheet.ncols()-2):
        if data_sheet[i_row+1, i_col].value:
            # # Make changes to the sheet
            # # For example, change the value of a specific cell
            update_sheet[data_sheet[0, i_col].value].set_value(data_sheet[i_row+1, i_col].value)
            # print(data_sheet[0, i_col].value, data_sheet[i_row+1, i_col].value)
    # Save the modified ODS file
    update_doc.save()
    # Close the ODS document
    # update_doc.close()
    print("=========================")
