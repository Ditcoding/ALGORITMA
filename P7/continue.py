st = 'Programming'# fungsi akan dieksekusi selama huruf adalah konsonan
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue #skip eksekusi kode dibawah jika vokal
    print(ch)
print('The end')