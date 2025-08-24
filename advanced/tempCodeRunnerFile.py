    
import tempfile

# --- FILE I/O WITH GZIP & EXCEL ---
with tempfile.NamedTemporaryFile(suffix='.gz', delete=False) as tmp_gz:
    gz_path = tmp_gz.name
with gzip.open(gz_path, 'wt') as f:
    f.write('hello gzip')
with gzip.open(gz_path, 'rt') as f:
    print("gzip read:", f.read())
os.remove(gz_path)

with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_xlsx:
    xlsx_path = tmp_xlsx.name
df.to_excel(xlsx_path)
print("Excel read:\n", pd.read_excel(xlsx_path))
os.remove(xlsx_path)