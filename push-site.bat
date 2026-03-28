@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ============================================================
echo   Deploiement du site SolarGlobe  ^(Git^)
echo ============================================================
echo.

REM --- Git disponible ? ---
where git >nul 2>&1
if errorlevel 1 (
  echo [X] Git n'est pas installe ou absent du PATH.
  set "RESUME=Echec - Git introuvable"
  goto fin
)

REM --- Depot Git ? ---
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo [X] Ce dossier n'est pas un depot Git ^(pas de .git^).
  set "RESUME=Echec - pas un depot Git"
  goto fin
)

echo [1/3] Ajout des fichiers...
git add .
if errorlevel 1 (
  echo [X] Erreur lors de git add.
  set "RESUME=Echec - git add"
  goto fin
)

echo [2/3] Verification des changements...
git diff --cached --quiet
if errorlevel 1 (
  for /f "delims=" %%t in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH-mm'"') do set "TS=%%t"
  echo     Creation du commit : Update site - !TS!
  git commit -m "Update site - !TS!"
  if errorlevel 1 (
    echo [X] Erreur lors du commit.
    set "RESUME=Echec - commit"
    goto fin
  )
  set "DIDCOMMIT=1"
  goto dopush
)

REM --- Rien a committer : fichiers deja enregistres localement ---
echo     Rien de nouveau a committer ^(aucun fichier modifie a enregistrer^).

git rev-parse @{u} >nul 2>&1
if errorlevel 1 (
  echo.
  echo [OK] Aucun changement a envoyer.
  echo      Branche sans suivi distant ^(upstream^).
  echo      Si besoin : git push -u origin NOM_DE_BRANCHE
  set "RESUME=Aucun changement - pas d'amont Git"
  goto fin
)

set "AHEAD=0"
set "AHEADFILE=%TEMP%\sg_ahead_%RANDOM%.txt"
git rev-list --count @{u}..HEAD 2>nul > "!AHEADFILE!"
if exist "!AHEADFILE!" (
  for /f "usebackq delims=" %%n in ("!AHEADFILE!") do set "AHEAD=%%n"
)
del "!AHEADFILE!" 2>nul
if not defined AHEAD set "AHEAD=0"

if "!AHEAD!"=="0" (
  echo.
  echo [OK] Aucun changement detecte - tout est deja synchronise avec le distant.
  set "RESUME=Aucun changement - deja synchronise"
  goto fin
)

echo     !AHEAD! commit^(s^) local^(aux^) en attente sur le distant - envoi...
set "DIDCOMMIT=0"
set "AHEADNUM=!AHEAD!"

:dopush
echo [3/3] Push vers le depot distant...
git push
if errorlevel 1 (
  echo [X] Erreur lors du push ^(reseau, droits, conflit ou depot^).
  set "RESUME=Echec - push"
  goto fin
)

if "!DIDCOMMIT!"=="1" (
  set "RESUME=Commit cree puis push reussi"
) else (
  set "RESUME=Push reussi ^(!AHEADNUM! commit^(s^) en attente^)"
)
goto fin

:fin
echo.
echo ------------------------------------------------------------
if defined RESUME echo   Resume : !RESUME!
echo ------------------------------------------------------------
echo.
pause
