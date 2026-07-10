
@echo off
IF EXIST ".env" (
    echo ".env exists, assuming setup is complete"
    .\.venv\Scripts\activate
    python src/main.py
) ELSE (
    echo File is missing.
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r .\scripts\requirements.txt
    type nul > .env
    echo GOOGLE_MAPS_API_KEY= >> .env
    echo ROBOFLOW_API_KEY=uyDjfwt8tTfLrodSYAxP >> .env
    python src/main.py
)
pause

