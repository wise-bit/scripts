@echo off
:: Prompt for the file name
set /p filename=Enter the file name to encrypt: 

:: Prompt for the password with invisible input
for /f "tokens=*" %%p in ('powershell -Command "Read-Host -AsSecureString | ConvertFrom-SecureString"') do set password=%%p

:: Call the Python script to encrypt
python script.py encrypt "%filename%" "%password%"

:: Clear the password variable from memory
set password=

