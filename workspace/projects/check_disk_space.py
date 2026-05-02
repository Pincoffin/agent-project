import shutil

def check_disk_space(path):
    total, used, free = shutil.disk_usage(path)
    print(f'Total: {total // (2**30):.1f} GB, Used: {used // (2**30):.1f} GB, Free: {free // (2**30):.1f} GB')

check_disk_space('/')