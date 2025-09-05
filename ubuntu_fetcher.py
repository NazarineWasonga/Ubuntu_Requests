"""
Ubuntu-Inspired Image Fetcher
--------------------------------
"I am because we are" - Ubuntu Philosophy

This script fetches images from the web and stores them locally
in a 'Fetched_Images' folder, embracing Ubuntu principles:
- Community: connects to the global web
- Respect: handles errors gracefully
- Sharing: organizes images for later appreciation
- Practicality: serves a real-world need
"""

import requests
import os
from urllib.parse import urlparse
import hashlib


def fetch_image(url):
    """Fetch and save an image from the given URL."""

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image with a timeout
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check Content-Type header to ensure it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped: {url} (Not an image)")
            return

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # Fallback filename
            filename = "downloaded_image.jpg"

        # Prevent duplicate downloads (by hashing content)
        file_hash = hashlib.md5(response.content).hexdigest()
        filename = f"{file_hash[:8]}_{filename}"

        filepath = os.path.join("Fetched_Images", filename)

        if os.path.exists(filepath):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs separated by spaces
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()

    for url in urls:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
