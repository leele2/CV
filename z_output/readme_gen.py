# import module
from pdf2image import convert_from_path
from pathlib import Path
from os.path import exists
from os import mkdir
import shutil

def readme(pdf, text):
    global readme_dir
    # Directories
    cwd = str(Path(__file__).parent.absolute())
    pdf_file = cwd + f"\\{pdf}"
    output_dir = cwd + "\\Images\\"
    readme_dir = "\\".join(cwd.split("\\")[:-1]) # -3 represents up 4 directories
    
    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)
    txt_out = []
    # Add Title (root folder of repositry)
    # txt_out.append("# " + cwd.split("\\")[-2] + "\n")
    txt_out.append("# " + text+ "\n")

    # Create folder to store images if not already created
    if not exists(output_dir):
        mkdir(output_dir)
    # Convert pdf to images
    for i in range(len(images)):
        #Save pdf pages as .png images
        images[i].save(output_dir + f'{text}page'+ str(i) +'.png', 'PNG')
        #String for README.md
        txt_out.append(f"![{text}page" + str(i) + f"](z_output/Images/{text}page" + str(i) + ".png)")
        # txt_out.append("![page" + str(i) + "](" + "/".join(output_dir.split("\\")[-5:]) + "page" + str(i) + ".png)")
        txt_out.append("***")
    # Copy pdf to main directory
    shutil.copy(pdf_file, readme_dir + f"/{text}.pdf")
    return txt_out

pdf_files = [str(pdf_file).split('\\')[-1] for pdf_file in Path('./z_output/').glob("*.pdf")]
txt_out = []
for pdf_file in reversed(pdf_files):
    result = readme(pdf_file, pdf_file.split('.')[0])
    if "WorkingCoverLetter" in pdf_file:
        # Dont add to ReadMe
        continue
    txt_out.extend(result)
    txt_out.append("\n")

# Create README.md
with open(readme_dir + "/README.md", "w") as output:
    output.write("\n".join(txt_out))