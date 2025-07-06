import os
import requests
from PyQt6.QtGui import QPixmap

# Simple image cache - create this once in your app
def download_image(url):
    """Download image and return QPixmap"""
    try:
        # Create cache folder
        if not os.path.exists("images"):
            os.makedirs("images")
        
        # Get filename from URL
        filename = url.split('/')[-1].split('?')[0]
        if not filename.endswith(('.jpg', '.jpeg', '.png')):
            filename += '.jpg'
        
        cache_path = f"images/{filename}"
        
        # Check if already cached
        if os.path.exists(cache_path):
            return QPixmap(cache_path)
        
        # Download and save
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            with open(cache_path, 'wb') as f:
                f.write(response.content)
            return QPixmap(cache_path)
        
    except Exception as e:
        print(f"Error loading image: {e}")
    
    return None