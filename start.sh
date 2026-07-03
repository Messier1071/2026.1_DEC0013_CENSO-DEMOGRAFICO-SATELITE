FILE=".env"

if [ -f "$FILE" ]; then
    echo ".env exists, assuming setup is complete"
    source .venv/bin/activate
    python src/main.py
else
    echo ".env missing, starting setup"
    python3.11 -m venv .venv
    source .venv/bin/activate
    echo venv active
    pip install -r "./scripts/requirements.txt"
    touch .env

    read -sp "Enter your GOOGLE_MAPS_API_KEY: (press enter to leave empty)" googlekey
    echo ""
    echo "GOOGLE_MAPS_API_KEY=$googlekey" >> .env

    read -sp "Enter your ROBOFLOW_API_KEY: (press enter to leave empty)" robokey
    echo ""
    echo "ROBOFLOW_API_KEY=$robokey" >> .env

    python src/main.py


fi
