current_version = input().split('.')
current_version_int = int(''.join(current_version))
next_version_str = str(current_version_int + 1)
print('.'.join(next_version_str))

