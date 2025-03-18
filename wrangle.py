'''
*------------------*
|                  |
|     WRANGLE!     |
|                  |
*------------------*
'''

#------------------------------------------------------------- IMPORTS  -------------------------------------------------------------


import os
import pandas as pd


#------------------------------------------------------------- ACQUIRE --------------------------------------------------------------

def check_file_exists(csv_fn):
    """
    Ensures the dataset is available locally.

    - If the CSV file is found, it reads the file.
    - If the local file is missing, prints a warning.
    """

    original_df = None

    if os.path.isfile(csv_fn):
        print(f"✅ CSV file '{csv_fn}' found locally.")
        original_df = pd.read_csv(csv_fn)
    else:
        print(f"⚠️ CSV file '{csv_fn}' not found locally.")
        print("   Please clone the repository or download the file from GitHub so it is available locally.")

    return original_df

# ------------------------------------------------Extra-----------------------------------------------------------------------------------

def check_file_exists_V2(csv_fn):
    """
    Ensures a dataset is available locally.

    - If the CSV file is found, it reads the file (assuming UTF-8 or system default encoding).
    - If the local file is missing, it will print a warning message.
    - The data is no longer uploaded anywhere; each collaborator should clone this repo and work locally.
    """

    original_df = None  # We'll store the DataFrame here

    if os.path.isfile(csv_fn):
        print(f"✅ CSV file '{csv_fn}' found locally.")

        # Read the CSV with default encoding
        original_df = pd.read_csv(csv_fn)

        # Check if data needs cleaning
        if needs_cleaning(original_df):
            print("🔹 Data requires cleaning...")
            clean_df = clean_data(data_df)
            print("✅ Data has been cleaned.")
        else:
            print("✅ Data is already clean; no further action needed.")

    else:
        print(f"⚠️ CSV file '{csv_fn}' not found locally.")
        print("   Please clone the repository or download the file from GitHub so it is available locally.")

    return clean_df

def needs_cleaning(df):
    """Placeholder for logic to check if data requires cleaning."""
    # Implement real checks here; for now, assume no cleaning needed.
    return False

def clean_data(df):
    """Placeholder function to clean data. Replace with actual cleaning steps."""
    return df