import shutil

def get_disk_usage(drive):
    # Get disk usage statistics
    usage = shutil.disk_usage(drive)
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)
    percent_used = (usage.used / usage.total) * 100

    print(f"Drive: {drive}")
    print(f"Total Space: {total_gb:.2f} GB")
    print(f"Used Space: {used_gb:.2f} GB")
    print(f"Free Space: {free_gb:.2f} GB")
    print(f"Percentage Used: {percent_used:.2f}%")

# Example usage
get_disk_usage("C:\\")
