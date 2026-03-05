import requests
import time
import os

# Create a folder to store images
save_dir = "/content/mosdac_images"
os.makedirs(save_dir, exist_ok=True)

# List of image URLs
urls = ["https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0600_L1B_STD_WV_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0600_L1B_STD_WV_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0630_L1B_STD_IR1_TEMP_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0530_L1B_STD_IR2_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0530_L1B_STD_IR2_TEMP_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0500_L1B_STD_MIR_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0630_L1B_STD_MIR_TEMP_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0530_L1B_STD_SWIR_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0600_L1B_STD_VIS_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0600_L1B_STD_WV_V01R00.jpg",
      "https://mosdac.gov.in/look/3S_IMG/preview/2025/06JUL/3SIMG_06JUL2025_0530_L1B_STD_WV_TEMP_V01R00.jpg"
]
# Loop to download
for url in urls:
    filename = os.path.join(save_dir, url.split("/")[-1])
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f" Downloaded: {filename}")
    else:
        print(f" Failed: {url}")

    time.sleep(0.5)  # <---  delay between requests
