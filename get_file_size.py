import urllib
import urllib.request
import time
import math

def spacer(String : str,Space : int,Char_Fill : str = None) : # String Spacer
    if Char_Fill == None :
        Char_Fill = " "

    name_len = len(str(String))        # Count how many letter
    #  v------------------------------- Total available space
    if Space - name_len < Space :        # If blank space is greater than space
        space = Space - name_len         # Find a space
        box = f"{String}"
        for j in range(space) :
            box = f"{box}{Char_Fill}" # Add a space
    else :
        box = f"{String}{Char_Fill}"
    return box

def byte(value:float) : # Byte conversion
    value = float(value)
    if value / 1 > 0 and value / 1 < 1000 :
        return spacer(f"{value / 1:.4}",5,0) + " By"

    if value / 1000 > 0 and value / 1000 < 1000 :
        # return f"{value / 1000:.4} KB"
        return spacer(f"{value / 1000:.4}",5,0) + " KB"
    
    if value / 1000000 > 0 and value / 1000000 < 1000 :
        # return f"{value / 1000000:.4} MB"
        return spacer(f"{value / 1000000:.4}",5,0) + " MB"
    
    if value / 1000000000 > 0 and value / 1000000000 < 1000 : #1,000,000,000
        # return f"{value / 1000000000:.4} GB"
        return spacer(f"{value / 1000000000:.4}",5,0) + " GB"
    
    if value / 1000000000000 > 0 and value / 1000000000000 < 1000 :
        # return f"{value / 1000000000000:.4} TB"
        return spacer(f"{value / 1000000000000:.4}",5,0) + " TB"
    
def time_count(Second : float) :
    Second = float(Second)
    Minute = 0
    Hour = 0

    Minute_Text = ""
    Hour_Text = ""

    while Second - 60 >= 0 :
        Minute += 1
        Second -= 60

    while Minute - 60 >= 0 :
        Hour += 1
        Minute -= 60

    if Hour == 0 :
        None
    else :
        Hour_Text = f"{Hour}h "
    
    if Minute == 0 and Hour == 0 :
        None
    else :
        Minute_Text = f"{Minute}m "

    return f"{Hour_Text}{Minute_Text}{int(Second)}s"

def col(text : str ,fg : str = None ,bg : str = None) : # Color Display

    fg_text = ""
    bg_text = ""
    try :
        fg_arg = fg.split(" ")
    except Exception:
        None
    try :
        bg_arg = bg.split(" ")
    except Exception:
        None

    # Background
    try :
        if bg_arg[0] == "rgb" :
            bg_text = f"\N{ESC}[48;2;{str(bg_arg[1])}m"
        elif bg_arg[0] == "256" :
            bg_text = f"\N{ESC}[48;5;{str(bg_arg[1])}m"
    except Exception :
        None
    # Foreground
    try :
        if fg_arg[0] == "rgb" :
            fg_text = f"\N{ESC}[38;2;{str(fg_arg[1])}m"
        elif fg_arg[0] == "256" :
            fg_text = f"\N{ESC}[38;5;{str(fg_arg[1])}m"
    except Exception :
        None

    return f"{fg_text}{bg_text}{text}\N{ESC}[0m"

col_red = "256 196"
col_orange = "256 208"
col_yellow = "256 226"
col_lime = "256 46"
col_green = "256 28"
col_skyblue = "256 51"
col_midblue = "256 33"
col_blue = "256 21"
col_purple = "256 129"
col_pink = "256 207"
col_grey = "256 8"
col_white = "256 15"

def bar(left,total,length) : # A Bar Genarator
    length = int(length)
    left = float(left)
    total = float(total)
    bar_box = ""
    bar_box = "["
    for i in range(length) :
        exp_bar = left / total * 100
        exp_bar = exp_bar / 100 * length
        if i >= math.floor(exp_bar) :
            bar_box = f"{bar_box}{col(" ",fg=col_grey)}"
        elif i >= math.floor(exp_bar) - 1 :
            bar_box = f"{bar_box}{col("%",fg=col_white)}"
        else :
            bar_box = f"{bar_box}{col("=",fg=col_white)}"
    bar_box = f"{bar_box}]"
    return bar_box

# req = urllib.request.Request("")
# 
# f = urllib.request.urlopen(req)
# print(f.headers['Content-Length'])



URL = "https://archive.org/download/WindowsVistaBeta1Build5112x86DVD/en_longhorn_beta1_dvd.iso"

URL = input("Insert Download Link : ")

UP = "\x1B[3A"
CLR = "\x1B[0K"

# r = requests.get(URL)
# headers = r.headers
# file_size = headers.get('Content-Length')
# print(file_size)
print("Wait to response")

ping_s = time.perf_counter()
response = urllib.request.urlopen(URL)

file_size = response.headers['Content-Length']
ping_f = time.perf_counter()

total_ping = (ping_f - ping_s)


print(f"Start Downloading... {URL.split("/")[-1]} | {total_ping:.2f}s")
print("")
print("\n\n")
CHUNK = 16 * 1024

data = 0
with open(URL.split("/")[-1], 'wb') as f:
    while True:
        time_start = time.perf_counter()
        chunk = response.read(CHUNK)
        if not chunk:
            break
        time_end = time.perf_counter()
        total_time = time_end - time_start

        data += len(chunk)

        persentage = f"{(int(data) / int(file_size)) * 100:.2f}"
        # if float(persentage) < 1 :
        #     persentage = f"{(int(data) / int(file_size)) * 100:.3}"

        data_rate = len(chunk) / total_time

        eta_time = f"{(float(file_size) - data) / data_rate}"
        # if float(eta_time) < 1 :
        #     eta_time = f"{(float(file_size) - data) / data_rate:.3}"

        print(f"{UP}{bar(data,file_size,50)} {persentage}%           {CLR}\n{byte(data)} / {byte(file_size)} | {byte(data_rate)}/s{CLR}\n")


        f.write(chunk)

print("")
print("Download Successfully.")
