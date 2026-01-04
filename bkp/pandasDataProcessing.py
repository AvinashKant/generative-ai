import pandas as pd
import os

def read_users_csv(file_path):
    """
    Reads a CSV file into a pandas DataFrame and prints the contents.
    Includes error handling for file not found.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' was not found.")
            # Create a sample file for demonstration
            create_sample_csv(file_path)
            print(f"\nI've created a sample file named '{file_path}' for you.")
            print("Please run the script again to see the output.")
            return

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Print the DataFrame's contents
        print(f"Successfully read the file '{file_path}'.")
        print("\nDataFrame contents:")
        print(df)

        # You can now perform operations on the DataFrame, for example:
        # print("\nFirst 3 rows:")
        # print(df.head(3))
        # print("\nColumn names:")
        # print(df.columns)
        # print("\nDataFrame information:")
        # df.info()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def create_sample_csv(file_path):
    """
    Creates a simple sample users.csv file for demonstration.
    """
    sample_data = {
        'user_id': [1, 2, 3, 4],
        'username': ['alice', 'bob', 'charlie', 'diana'],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'diana@example.com']
    }
    sample_df = pd.DataFrame(sample_data)
    sample_df.to_csv(file_path, index=False)


if __name__ == "__main__":
    csv_file_path = 'users.csv'
    read_users_csv(csv_file_path)
