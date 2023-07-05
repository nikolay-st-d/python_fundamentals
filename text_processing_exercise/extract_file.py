data = input()
path, extension = data.split('.')
sliced_path = path.split('\\')
file_name = sliced_path[-1]
print(f'File name: {file_name}')
print(f'File extension: {extension}')