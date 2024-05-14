import csv
import datetime

def generate_report(log_file, report_file):
    with open(log_file, 'r') as infile, open(report_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["Timestamp", "Event", "Details"])
        for row in reader:
            timestamp = datetime.datetime.now().isoformat()
            writer.writerow([timestamp, row[0], row[1]])

if __name__ == "__main__":
    log_file_path = input("Enter the log file path: ")
    report_file_path = input("Enter the report file path: ")
    generate_report(log_file_path, report_file_path)
    print(f"Report generated: {report_file_path}")
