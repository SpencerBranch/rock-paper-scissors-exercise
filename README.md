# rock-paper-scissors-exercise

# Enter your player name by updating the .env file
# Replace "Your_Name" with desired user name
# Note .gitignore file already contain .env file type**
PLAYER_NAME="Your_Name"

# Create a new environment
conda create -n my-game-env python=3.8 

# Activate newly created environment
conda activate my-game-env

# Install required third party packages by running:
pip install -r requirements.txt

# Once you have entered your name, created and activated environnment and installed third party packages, run the game:
python game.py

