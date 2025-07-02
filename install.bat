@echo off
SETLOCAL ENABLEEXTENSIONS

REM === Comprobación de permisos de administrador ===
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Debes ejecutar este script como administrador.
    pause
    exit /b 1
)

REM === Variables ===
SET "CURRENT_DIR=%~dp0"
SET "INSTALL_DIR=C:\Program Files\imageToPdf"
SET "REG_KEY=HKEY_CLASSES_ROOT\Directory\Background\shell\Convert images to PDF"
SET "EXE_NAME=imageToPdf.exe"

REM === Crear directorio de instalación si no existe ===
IF NOT EXIST "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%" || (
        echo [ERROR] No se pudo crear el directorio %INSTALL_DIR%.
        pause
        exit /b 1
    )
)

REM === Copiar ejecutable ===
copy /Y "%CURRENT_DIR%%EXE_NAME%" "%INSTALL_DIR%\" >nul
IF NOT EXIST "%INSTALL_DIR%\%EXE_NAME%" (
    echo [ERROR] No se pudo copiar %EXE_NAME% a %INSTALL_DIR%.
    pause
    exit /b 1
)

REM === Agregar entrada al menú contextual ===
reg add "%REG_KEY%" /ve /d "Convert images to PDF" /f >nul
reg add "%REG_KEY%\command" /ve /d "\"%INSTALL_DIR%\%EXE_NAME%\" \"%%V\"" /f >nul

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] No se pudo agregar la clave al registro.
    pause
    exit /b 1
)

echo [OK] Instalación completa.
echo Ahora podes hacer clic derecho sobre fondo de una carpeta para convertir imágenes a PDF.
pause
ENDLOCAL
