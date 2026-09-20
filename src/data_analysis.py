import os
import glob
import pandas as pd


# --------------------------------------------------
# Configuration
# --------------------------------------------------

DATASET_DIRECTORY = "dataset/Daily"
OUTPUT_DIRECTORY = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIRECTORY, "soil_moisture_analysis.csv")


# --------------------------------------------------
# Dataset Loading
# --------------------------------------------------

def find_sensor_files():
    """Find all sensor text files in the dataset directory."""
    pattern = os.path.join(DATASET_DIRECTORY, "*.txt")
    files = glob.glob(pattern)

    if not files:
        raise FileNotFoundError(
            f"No sensor files found in: {DATASET_DIRECTORY}"
        )

    return sorted(files)


def load_sensor_file(file_path):
    """Load a single sensor data file."""
    try:
        data = pd.read_csv(
            file_path,
            sep=None,
            engine="python"
        )

        location = os.path.splitext(
            os.path.basename(file_path)
        )[0]

        data["Location"] = location

        return data

    except Exception as error:
        print(f"Could not read {file_path}: {error}")
        return pd.DataFrame()


def load_dataset():
    """Load and combine all available sensor files."""
    sensor_files = find_sensor_files()

    data_frames = []

    for file_path in sensor_files:
        data = load_sensor_file(file_path)

        if not data.empty:
            data_frames.append(data)

    if not data_frames:
        raise ValueError("No valid sensor data could be loaded.")

    return pd.concat(
        data_frames,
        ignore_index=True
    )


# --------------------------------------------------
# Data Cleaning
# --------------------------------------------------

def clean_dataset(data):
    """Clean and prepare the combined sensor data."""

    data = data.copy()

    # Remove completely empty rows and columns
    data.dropna(
        axis=0,
        how="all",
        inplace=True
    )

    data.dropna(
        axis=1,
        how="all",
        inplace=True
    )

    # Remove duplicate records
    data.drop_duplicates(
        inplace=True
    )

    # Standardize column names
    data.columns = [
        column.strip()
        for column in data.columns
    ]

    return data


# --------------------------------------------------
# Analysis
# --------------------------------------------------

def display_summary(data):
    """Display a basic summary of the dataset."""

    print("\n" + "=" * 60)
    print("SOIL MOISTURE DATASET SUMMARY")
    print("=" * 60)

    print(f"Total records : {len(data):,}")
    print(f"Total columns : {len(data.columns)}")

    if "Location" in data.columns:
        print(
            f"Locations     : "
            f"{data['Location'].nunique()}"
        )

    print("\nColumns:")
    for column in data.columns:
        print(f"  - {column}")


def calculate_statistics(data):
    """Calculate statistics for numeric measurements."""

    numeric_data = data.select_dtypes(
        include="number"
    )

    if numeric_data.empty:
        print("\nNo numeric measurements available.")
        return

    statistics = numeric_data.describe().transpose()

    print("\n" + "=" * 60)
    print("NUMERIC MEASUREMENT STATISTICS")
    print("=" * 60)

    print(
        statistics[
            ["count", "mean", "min", "max"]
        ].round(4)
    )


# --------------------------------------------------
# Output
# --------------------------------------------------

def save_analysis(data):
    """Save the cleaned dataset for further analysis."""

    os.makedirs(
        OUTPUT_DIRECTORY,
        exist_ok=True
    )

    data.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nAnalysis file saved to: {OUTPUT_FILE}"
    )


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():
    """Run the complete data analysis workflow."""

    print("Loading soil moisture sensor data...")

    try:
        data = load_dataset()

        data = clean_dataset(data)

        display_summary(data)

        calculate_statistics(data)

        save_analysis(data)

        print("\nData analysis completed successfully.")

    except (FileNotFoundError, ValueError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()