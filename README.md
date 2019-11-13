# LabProjectReport

To create each PDF, make sure that MikTex is installed.
Use Tex Console to install all required packages as seen in the preamble of each `.tex` file.

To merge the PDFs together to the condition it was submitted in, make sure Python (3.7.4 was used at the time of writing).
Next, install the `PyPDF2` package using Power Shell, CMD, or Git Bash:

`pip install PyPDF2`

To merge the PDFs, run `merge.py` from the root (LabProjectReport) directory:

`python merge.py`
