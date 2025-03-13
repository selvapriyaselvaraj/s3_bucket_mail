import psutil

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')  # Root directory for Ubuntu
    print(f"Total Disk Space: {disk_usage.total / (1024**3):.2f} GB")
    print(f"Used Disk Space: {disk_usage.used / (1024**3):.2f} GB")
    print(f"Free Disk Space: {disk_usage.free / (1024**3):.2f} GB")
    print(f"Percentage Used: {disk_usage.percent}%")

if __name__ == "__main__":
    get_disk_usage()
