start_chr = int(input())
end_chr = int(input())

for char in range(start_chr, end_chr + 1):
    print(f'{chr(char)}', end=' ')
