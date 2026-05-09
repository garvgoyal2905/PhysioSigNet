import os
import requests

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Download CSV
csv_url = 'https://physionet.org/files/ptb-xl/1.0.3/ptbxl_database.csv'
try:
    response = requests.get(csv_url)
    response.raise_for_status()
    with open(os.path.join(data_dir, 'ptbxl_database.csv'), 'wb') as f:
        f.write(response.content)
    print("CSV downloaded.")
except Exception as e:
    print(f"Failed to download CSV: {e}")

# Download records100
records_dir = os.path.join(data_dir, 'records100')
os.makedirs(records_dir, exist_ok=True)

for i in range(1, 101):
    record = f'{i:05d}'
    record_dir = os.path.join(records_dir, record)
    os.makedirs(record_dir, exist_ok=True)

    # Download .hea
    hea_url = f'https://physionet.org/files/ptb-xl/1.0.3/records100/{record}/{record}.hea'
    try:
        response = requests.get(hea_url)
        response.raise_for_status()
        with open(os.path.join(record_dir, f'{record}.hea'), 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {record}.hea: {e}")
        continue

    # Download .dat
    dat_url = f'https://physionet.org/files/ptb-xl/1.0.3/records100/{record}/{record}_lr.dat'
    try:
        response = requests.get(dat_url)
        response.raise_for_status()
        with open(os.path.join(record_dir, f'{record}_lr.dat'), 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Failed to download {record}_lr.dat: {e}")
        continue

print("Download complete.")