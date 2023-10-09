from datetime import datetime

def calculate_file_id_based_on_date():
    date_str = datetime.now().strftime('%d %b %Y')
    date_mapping = {
        '04 Oct 2023': '5521',
        '05 Oct 2023': '5522',
        '06 Oct 2023': '5523',
    }
    return date_mapping.get(date_str, 'unknown')
