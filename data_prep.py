import pandas as pd
import re

# Convert the bytes into a number
def byte_to_num(byte_string):
    byte_string = str(byte_string).strip().upper()

    match = re.match(r'([0-9\.]+)\s*([KMG])?', byte_string)

    if not match:
        return byte_string
    
    value, unit = match.groups()
    value = float(value)

    if unit == 'K':
        return int(value * 1024)
    if unit == 'M':
        return int(value * 1024**2)
    if unit == 'G':
        return int(value * 1024**3)
    
    return int(value)

def parse_csv(path_to_csv, output_path):

    # creating a dataframe
    df = pd.read_csv(path_to_csv)
    df.columns = df.columns.str.strip()

    sentences = []

    for index, row in df.iterrows():
        try:
            proto = str(row['Proto']).strip()
            duration = float(row['Duration'])
            src_ip = str(row['Src IP Addr']).strip()
            src_port = str(row['Src Pt']).strip()
            dst_ip = str(row['Dst IP Addr']).strip()
            dst_port = str(row['Dst Pt']).strip()
            packets = int(row['Packets'])

            bytes_cleaned = byte_to_num(row['Bytes'])
            flags = str(row['Flags']).strip()

            sentence = (
                f"A {proto} connection between {src_ip} on port {src_port} and "
                f"{dst_ip} on port {dst_port} lasted for {duration:.2f} seconds. "
                f"It involved {packets} packets and {bytes_cleaned} bytes. "
                f"The TCP flags were '{flags}'."
            )

            sentences.append(sentence)
        except (KeyError, ValueError) as e:
            print(f"[-] Warning: Skipping row {index + 2} due to error: {e}")
            continue

    print(f"[+] Saving the processed sentences of length {len(sentences)} to {output_path}")
    with open(output_path, 'w') as f:
        for sentence in sentences:
            f.write(sentence + '\n')
        
    print("[+] Processing complete")

if __name__ == "__main__":
    INPUT_FILE = './CIDDS-001-external-week1.csv'
    OUTPUT_FILE = './output.txt'
    parse_csv(INPUT_FILE, OUTPUT_FILE)

