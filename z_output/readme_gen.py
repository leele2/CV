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
    readme_dir = "\\".join(cwd.split("\\")[:-1])  # -1 represents up 1 directory

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)
    txt_out = []

    # Create folder to store images if not already created
    if not exists(output_dir):
        mkdir(output_dir)

    # Convert pdf to images
    for i in range(len(images)):
        # Save pdf pages as .png images
        images[i].save(output_dir + f"{text}page" + str(i) + ".png", "PNG")
        # String for README.md
        txt_out.append(f"![{text} Page {i + 1}](z_output/Images/{text}page{i}.png)")
        txt_out.append("")  # Empty line for spacing

    # Copy pdf to main directory
    shutil.copy(pdf_file, readme_dir + f"/{text}.pdf")
    return txt_out


def get_comprehensive_readme():
    """Return the comprehensive README content"""
    return """# Professional LaTeX CV Template

A sophisticated, data-driven LaTeX CV template originally forked from [latex-ninja/simple-hipstercv](https://github.com/latex-ninja/simple-hipstercv), significantly enhanced with a modular data architecture, advanced styling, and comprehensive customization options.

## 📋 CV Preview

The following images show the current version of the CV. The PDF version is automatically updated and available for download.

"""


def get_readme_footer():
    """Return the footer content explaining the automation"""
    return """

---

## 🤖 Automated README Generation

This README is automatically generated using a Python script that:
- Converts PDF files to images for preview
- Combines CV previews with comprehensive documentation
- Maintains up-to-date visual representation of the CV

### Script Features
- **PDF to Image Conversion**: Uses `pdf2image` to create PNG previews
- **Automatic File Management**: Organizes images and copies PDFs to appropriate directories  
- **Dynamic Content**: Generates image links and maintains file structure
- **Selective Processing**: Filters out working files and focuses on final outputs

To regenerate this README:
```bash
cd z_output
python readme_generator.py
```

## 🌟 Key Features

### Data-Driven Architecture
- **Complete separation of content and presentation** - All personal information, projects, skills, and work experience are stored in `data_file.sty`
- **Modular design** - Easy to update content without touching the layout code
- **Dynamic rendering** - Content is automatically formatted using custom LaTeX commands

### Advanced Layout & Design
- **Two-page professional layout** with sidebar and main content areas
- **Custom TikZ graphics** for skill bars, contact icons, and visual elements
- **Responsive typography** with automatic spacing adjustment using microtype
- **Professional color scheme** with customizable theme colors
- **QR code integration** for easy CV sharing

### Enhanced Functionality
- **Automated skill visualization** with progress bars for programming languages
- **Project showcase** with GitHub links and technology tags
- **Professional certifications section**
- **Technical expertise with real-world applications**
- **Age calculation** from date of birth
- **Multiple icon libraries** (FontAwesome, Academicons)

## 📁 Repository Structure

```
CV/
├── CV.tex                 # Main CV document
├── preamble.sty          # Core styling and formatting commands
├── data_file.sty         # All personal data and content
├── CoverLetterTemplate.tex # Cover letter template (optional)
├── cover_preamble.sty    # Cover letter styling
├── z_output/             # Build output directory
│   ├── readme_generator.py # Automated README generation script
│   └── Images/           # Generated CV preview images
├── PIC/                  # Images directory
│   ├── Portrait.jpg      # Profile picture
│   ├── ExeterLogo.png   # University logos
│   ├── harvard.jpg      # Certificate logos
│   └── ...              # Flag icons and other graphics
└── CV.pdf               # Generated output
```

## 🚀 Quick Start

### Prerequisites
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Python with `pdf2image` package (for README generation)
- Required LaTeX packages (automatically handled by most distributions):
  - `tcolorbox`, `tikz`, `fontawesome5`, `academicons`
  - `geometry`, `microtype`, `hyperref`, `xcolor`
  - `graphicx`, `adjustbox`, `multicol`, `qrcode`

### Compilation
```bash
# Standard compilation
pdflatex CV.tex
pdflatex CV.tex  # Second pass for references

# Or using latexmk for automatic compilation
latexmk -pdf CV.tex

# Update README with new CV preview
cd z_output
python readme_generator.py
```

### VS Code Integration (Recommended)
For the best experience, use VS Code with LaTeX Workshop extension. Add this configuration to your `settings.json`:

```json
{
    "latex-workshop.latex.outDir": "./z_output/",
    "latex-workshop.latex.autoClean.run": "never",
    "latex-workshop.latex.recipes": [
        {
            "name": "lualatex + README",
            "tools": ["lualatex", "Py README.md Generator"]
        },
        {
            "name": "latexmk + README",
            "tools": ["latexmk", "Py README.md Generator"]
        },
        {
            "name": "README Generator Only",
            "tools": ["Py README.md Generator"]
        }
    ],
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-aux-directory=z_output",
                "-output-directory=z_output",
                "%DOC%"
            ]
        },
        {
            "name": "lualatex",
            "command": "latexmk",
            "args": [
                "-pdflatex=lualatex",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-aux-directory=z_output",
                "-output-directory=z_output",
                "%DOC%"
            ]
        },
        {
            "name": "Py README.md Generator",
            "command": "python",
            "args": ["%OUTDIR%readme_gen.py"],
            "env": {}
        }
    ]
}
```

This setup automatically:
- Compiles your CV to the `z_output` directory
- Runs the README generator after compilation
- Keeps auxiliary files organized
- Updates the repository documentation with fresh CV previews

## ✏️ Customization Guide

### 1. Personal Information
All content is stored in `data_file.sty`. Simply modify the relevant commands:

```latex
% Update contact information by modifying the contact matrix in CV.tex
% Update about me section by changing the \aboutMe{} content
```

### 2. Projects
Add or modify projects in the `\\projectList` command:
```latex
\\newcommand{\\projectList}{%
{Project Type}/{Year}/{Title}/{Description}/{GitHub URL}/{Link Text}/{Technologies},
% Add more projects here...
}
```

### 3. Skills
Update skill lists by modifying these commands in `data_file.sty`:
```latex
\\newcommand{\\professionalSkillsList}{%
    {Python}, {R}, {SQL}, {Web Scraping}, ... }

\\newcommand{\\softSkillsList}{%
    {Problem Solving}, {Collaboration}, ... }
```

### 4. Programming Languages with Skill Bars
Modify the `\\skills{}` command in `CV.tex`:
```latex
\\skills{{\\flag{C.png} C\\slash C++/2},{\\faPython Python/5.5}, ...}
```
Numbers represent skill level (1-6 scale).

### 5. Work Experience
Add experience using the `\\MySectionB{}` command:
```latex
\\MySectionB{Date Range}{logo.png}{Position}{Company}{Location}
{Description and achievements}
```

### 6. Technical Expertise
Define detailed technical sections in `\\techExpertiseApplicationList`:
```latex
{Skill Category}/{%
{Technology}/{Detailed application description},
{Another Technology}/{Another application}, ... },
```

## 🎨 Styling Customization

### Colors
Modify colors in `preamble.sty`:
```latex
\\definecolor{titleBackColor}{rgb}{0.25,0.25,0.25}  # Header background
\\definecolor{sideBarColor}{rgb}{0.6,0.6,0.6}       # Sidebar background
```

### Layout Dimensions
Adjust layout in `preamble.sty`:
```latex
\\geometry{
    a4paper,
    left=0.1cm,    # Adjust margins
    right=0.6cm,
    top=0.1cm,
    bottom=0.1cm
}
```

### Fonts
The template uses Fourier-OTF with Adobe Utopia math design. To change fonts, modify the font loading section in `preamble.sty`.

## 🖼️ Adding Images

### Profile Picture
- Add your photo as `PIC/Portrait.jpg`
- Uncomment `\\profilePicture{}` in `CV.tex`

### Company/University Logos
- Add logos to the `PIC/` directory
- Reference them in `\\MySection{}` or `\\MySectionB{}` commands

### Flag Icons
- Add country/technology flags to `PIC/` directory
- Use with `\\flag{filename.png}` command

## 🔧 Advanced Features

### QR Code Integration
The template automatically generates a QR code linking to your CV. Update the link in `data_file.sty`:
```latex
\\newcommand{\\linkToCV}{%
    https://github.com/yourusername/CV/blob/master/CV.pdf}
```

### Skills Visualization
The `\\listskills{}` command creates professional skill tags, while `\\skills{}` creates progress bars for programming languages.

### Project Management
Projects are rendered with GitHub integration, technology tags, and automatic formatting for consistent presentation.

## 📊 Key Improvements Over Original Template

1. **Complete data separation** - Content stored independently from presentation
2. **Enhanced modularity** - Easy to maintain and update
3. **Professional project showcase** - Integrated GitHub links and technology tags  
4. **Advanced skill visualization** - Progress bars and professional tags
5. **Technical expertise section** - Detailed applications and examples
6. **Improved typography** - Better spacing and microtype integration
7. **QR code integration** - Modern sharing capabilities
8. **Comprehensive icon support** - FontAwesome5 and Academicons
9. **Flexible layout system** - Easy to modify sections and styling
10. **Automated documentation** - Python script for README generation and CV previews

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements. Some areas for potential enhancement:

- Additional section types
- More color themes
- Alternative layout options
- Extended icon support
- Multi-language support
- Enhanced automation scripts

## 📄 License

This project maintains the same license as the original [latex-ninja/simple-hipstercv](https://github.com/latex-ninja/simple-hipstercv) repository.

## 🙏 Acknowledgments

- Original template by [latex-ninja](https://github.com/latex-ninja)
- Enhanced and modified by [leele2](https://github.com/leele2)
- Icons by FontAwesome and Academicons projects
- Automated README generation using Python and pdf2image

---

## 🚧 Work in Progress

**Note**: This template is currently undergoing migration to fully separate content from presentation. The core data separation system is implemented and working well - projects, skills, technical expertise, and interests are already managed through the `data_file.sty` system. 

**Still being migrated**: Contact information, work experience, education sections, and personal achievements are in the process of being moved from CV.tex to the data file system.

The template is designed for technical professionals and includes specialized sections for programming skills, projects, and technical expertise. It's particularly well-suited for software engineers, data scientists, and mathematicians."""


# Main execution
pdf_files = [str(pdf_file).split("\\")[-1] for pdf_file in Path("./").glob("*.pdf")]
txt_out = []

# Add header content
txt_out.append(get_comprehensive_readme())

# Process PDF files for images
for pdf_file in reversed(pdf_files):
    if "WorkingCoverLetter" in pdf_file:
        # Don't add working files to ReadMe
        continue

    result = readme(pdf_file, pdf_file.split(".")[0])
    txt_out.extend(result)
    txt_out.append("")  # Add spacing between documents

# Add comprehensive README content
txt_out.append(get_readme_footer())

# Create README.md
with open(readme_dir + "/README.md", "w", encoding="utf-8") as output:
    output.write("\n".join(txt_out))
