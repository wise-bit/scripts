@echo off
:: Prompt for the file name
set /p filename=Enter the file name to decrypt: 

:: Prompt for the password with invisible input
for /f "tokens=*" %%p in ('powershell -Command "Read-Host -AsSecureString | ConvertFrom-SecureString"') do set password=%%p

:: Call the Python script to decrypt
python script.py decrypt "%filename%" "%password%"

:: Clear the password variable from memory
set password=

