# Image to PDF Converter

This project allows users to convert images to PDF files easily using a context menu option in Windows Explorer.

## Prerequisites

- Python 3.12 or later

### Package and install

```commandline
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate  # On Windows
```

```commandline
pip install -r requirements.txt
```

```commandline
pyinstaller --onefile imageToPdf.py
```
