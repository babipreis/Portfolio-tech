# log_analyzer.py
# Simple Log Analyzer Script by Bárbara dos Reis

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        error_count = 0
        warning_count = 0

        for line in lines:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

        print("📊 Log Analysis Summary:")
        print(f"Errors found: {error_count}")
        print(f"Warnings found: {warning_count}")
        print("✅ Analysis completed successfully.")

    except FileNotFoundError:
        print("⚠️ Log file not found. Please check the file path.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    log_path = input("Enter the path to your log file: ")
    analyze_log(log_path)
