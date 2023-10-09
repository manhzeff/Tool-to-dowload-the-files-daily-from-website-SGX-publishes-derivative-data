import argparse
from file_handling import read_recovery_file, write_recovery_file
from download import downloads
from date_handling import calculate_file_id_based_on_date

def get_today_files(file_id):
    return [
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/WEBPXTICK_DT-{file_id}.zip',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TickData_structure.dat',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TC_{file_id}.txt',
        f'https://links.sgx.com/1.0.0/derivatives-historical/{file_id}/TC_structure.dat'
    ]


def main(id=None):
    if id:
        file_id = id
    else:
        file_id = calculate_file_id_based_on_date()

    recovery_urls = read_recovery_file('recover.txt')
    if recovery_urls:
        failed_urls = downloads(recovery_urls)
        write_recovery_file('recover.txt', failed_urls)

    today_urls = get_today_files(file_id)
    failed_urls = downloads(today_urls)
    write_recovery_file('recover.txt', failed_urls)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download files from the specified website.')
    parser.add_argument('--id', help='File ID corresponding to the date', required=False, type=str)
    args = parser.parse_args()
    main(args.id)
