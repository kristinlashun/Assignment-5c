# Author: Kristin Towns
# GitHub: kristinlashun
# Date: 2/7/2024
# Description: This class reads SAT data from a JSON file and writes selected data to a CSV file.

import json

class SatData:
    def __init__(self, json_file='sat.json'):
        """Initialize the SatData object, reading the SAT data from a JSON file."""
        self.__data = self.__read_json(json_file)

    def __read_json(self, file_path):
        """Read JSON data from a file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def __sanitize_data(self, data):
        """Enclose data in quotes if it contains a comma."""
        return f'"{data}"' if ',' in data or '"' in data else data

    def save_as_csv(self, dbns):
        """Save data as CSV for the provided DBNs."""
        with open('output.csv', 'w') as file:
            # Write column headers
            file.write('DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean\n')
            
            # Filter and sort the data by DBN
            filtered_data = [entry for entry in self.__data if entry['dbn'] in dbns]
            sorted_data = sorted(filtered_data, key=lambda x: x['dbn'])

            # Write the sorted data to the CSV file
            for entry in sorted_data:
                dbn = entry['dbn']
                school_name = self.__sanitize_data(entry['school_name'])
                num_of_test_takers = entry['num_of_test_takers']
                critical_reading_mean = entry['sat_critical_reading_avg_score']
                math_mean = entry['sat_math_avg_score']
                writing_mean = entry['sat_writing_avg_score']

                line = f'{dbn},{school_name},{num_of_test_takers},{critical_reading_mean},{math_mean},{writing_mean}\n'
                file.write(line)



