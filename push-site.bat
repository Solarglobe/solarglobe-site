@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ========================================
echo   Envoi du site vers Git
echo ========================================
echo.

echo [1/3] Ajout des fichiers...
git add .
if errorlevel 1 (
  echo.
  echo Erreur lors de git add.
  goto fin
)

echo [2/3] Verification puis commit si necessaire...
git diff --cached --quiet
if %errorlevel% equ 0 (
  echo    Aucun changement a committer - rien de nouveau a enregistrer.
  echo.
  goto push
)

for /f "delims=" %%i in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"') do (
  git commit -m "Update site %%i"
)
if errorlevel 1 (
  echo.
  echo Erreur lors du commit.
  goto fin
)

:push
echo [3/3] Push vers le depot distant...
git push
if errorlevel 1 (
  echo.
  echo Erreur lors du push  ^(branche, reseau ou authentification^).
  goto fin
)

echo.
echo Termine.

:fin
echo.
pause
