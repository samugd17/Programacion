samba_full_path = "//1.1.1.1./eoi/python"
samba_path = samba_full_path[2:]
slash_index = samba_path.index("/")
host = samba_path[:slash_index]
path = samba_path[slash_index:]
print(f"host = {host}, path = {path}")