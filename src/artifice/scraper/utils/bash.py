# all functions can either return the raw terminal command
# or by passing the exec flag as an argument, will run the command and return the output

def sh_disk_usage(exec=False):
    cmd = "df -hl | grep '/' | awk '{print $5}' | sed -n '3 p'"
    return cmd
