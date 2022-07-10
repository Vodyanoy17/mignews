REM EXCUTE FROM THE DOS WINDOWS promt and not in the Windows POwerSher  
rmdir .venv /q
python -m venv .venv
.venv\Scripts\activate



set HTTP_PROXY=http://proxy02.iil.intel.com:911/
set HTTPS_PROXY=http://proxy02.iil.intel.com:911/


REM pip-compile
REM pip install -r requirements_dev.txt
python -m ipykernel install --user --name=venv

