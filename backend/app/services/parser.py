import gzip, csv, io

def parse_gzip_tsv(content:bytes):
    text=gzip.decompress(content).decode("utf-8")
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))