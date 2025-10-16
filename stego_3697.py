#!/usr/bin/env python3
"""
███████╗████████╗███████╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ ███████╗██████╗ ███╗   ██╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝ ██╔════╝ ██╔════╝██╔══██╗████╗  ██║
███████╗   ██║   █████╗  ███████║██╔██╗ ██║██║  ███╗██║  ███╗█████╗  ██████╔╝██╔██╗ ██║
╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║██║   ██║██╔══╝  ██╔══██╗██║╚██╗██║
███████║   ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║  ██║██║ ╚████║
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                      
██████╗ ██╗   ██╗████████╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗████████╗ ██████╗██╗  ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔════╝ ██╔════╝██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║  ██║
██████╔╝██║   ██║   ██║   ██║  ███╗█████╗  ██║   ██║██╔██╗ ██║█████╗     ██║   ██║     ███████║
██╔══██╗██║   ██║   ██║   ██║   ██║██╔══╝  ██║   ██║██║╚██╗██║██╔══╝     ██║   ██║     ██╔══██║
██████╔╝╚██████╔╝   ██║   ╚██████╔╝███████╗╚██████╔╝██║ ╚████║███████╗   ██║   ╚██████╗██║  ██║
╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
"""

import os
import sys
import argparse
from PIL import Image
import numpy as np
import time

# ANSI Color Codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ENDC = '\033[0m'

def print_banner():
    banner = f"""
{RED}╔════════════════════════════════════════════════════════════════════════════════════════════╗
{RED}║{WHITE}  ██████╗██╗   ██╗███████╗████████╗ █████╗  ██████╗ ███████╗██████╗  ██████╗  ██████╗      {RED}║
{RED}║{WHITE} ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗██╔═══██╗██╔════╝      {RED}║
{RED}║{WHITE} ██║     ██║   ██║█████╗     ██║   ███████║██║  ███╗█████╗  ██████╔╝██║   ██║██║  ███╗     {RED}║
{RED}║{WHITE} ██║     ██║   ██║██╔══╝     ██║   ██╔══██║██║   ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║     {RED}║
{RED}║{WHITE} ╚██████╗╚██████╔╝███████╗   ██║   ██║  ██║╚██████╔╝███████╗██║  ██║╚██████╔╝╚██████╔╝     {RED}║
{RED}║{WHITE}  ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝      {RED}║
{RED}╚════════════════════════════════════════════════════════════════════════════════════════════╝
{YELLOW}                    Tool: Steganographer_3697                                            
{YELLOW}                    Author: Umar Ruman                                                   
{YELLOW}                    Version: 1.0                                                          
{RED}╔════════════════════════════════════════════════════════════════════════════════════════════╗
{RED}║{CYAN}  This tool is designed for authorized penetration testing and educational purposes only  {RED}║
{RED}║{CYAN}  Unauthorized use of this tool is strictly prohibited and may violate applicable laws    {RED}║
{RED}╚════════════════════════════════════════════════════════════════════════════════════════════╝
{ENDC}"""
    print(banner)

def print_disclaimer():
    disclaimer = f"""
{RED}[!] {YELLOW}DISCLAIMER:
{RED}═══════════════════════════════════════════════════════════════════════════════════════════════
{WHITE}This tool is intended for educational and authorized security testing purposes only.
By using this tool, you agree to the following terms:

1. You have explicit written permission from the device/system owner
2. You will only use this tool on systems you are authorized to test
3. You will comply with all applicable laws and regulations
4. You will report any findings through proper channels
5. You will not use this tool for malicious or unauthorized activities

{RED}[!] {YELLOW}Legal compliance is your responsibility. This tool is provided for legitimate security 
    testing and research purposes only. Misuse of this tool may result in criminal charges.
{ENDC}"""
    print(disclaimer)

def confirm_authorization():
    print(f"\n{RED}[?] {YELLOW}Are you using this tool for AUTHORIZED work? {WHITE}(y/n): {ENDC}", end="")
    response = input().strip().lower()
    
    if response not in ['y', 'yes']:
        print(f"\n{GREEN}[+] {CYAN}OK, try next time babe! {WHITE}Exiting...\n{ENDC}")
        sys.exit(0)
    else:
        print(f"\n{GREEN}[+] {WHITE}Great! Starting the authorized tool...\n{ENDC}")
        time.sleep(1)

def validate_paths(file_path, image_path):
    """Validate if both paths exist and are accessible"""
    print(f"{YELLOW}[...] {WHITE}Validating file paths...{ENDC}")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Check if image is valid
    try:
        img = Image.open(image_path)
        img.verify()
        print(f"{GREEN}[✓] {WHITE}Paths validated successfully!{ENDC}")
        return True
    except Exception:
        raise ValueError(f"Invalid image file: {image_path}")

def embed_file_in_image(file_path, image_path, output_path=None):
    """Embed a file into an image using LSB steganography"""
    
    print(f"{YELLOW}[...] {WHITE}Preparing to embed file...{ENDC}")
    
    # Validate input paths
    validate_paths(file_path, image_path)
    
    # Open the original image
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Read the file to embed
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    print(f"{YELLOW}[...] {WHITE}Reading file: {os.path.basename(file_path)} ({len(file_data)} bytes){ENDC}")
    
    # Add file extension identifier
    file_extension = os.path.splitext(file_path)[1].encode()
    extension_length = len(file_extension)
    
    # Prepare data with header (extension info + data)
    data_to_hide = (
        extension_length.to_bytes(2, byteorder='big') +
        file_extension +
        file_data
    )
    
    # Convert data to bits
    data_bits = ''.join(format(byte, '08b') for byte in data_to_hide)
    
    # Get image pixels
    pixels = np.array(img)
    flat_pixels = pixels.flatten()
    
    # Check capacity
    if len(data_bits) > len(flat_pixels):
        raise ValueError("Image too small to hold the file")
    
    print(f"{YELLOW}[...] {WHITE}Embedding data using LSB technique...{ENDC}")
    
    # Embed data using LSB
    for i, bit in enumerate(data_bits):
        # Modify LSB of each color channel
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(bit)
    
    # Reshape and save
    modified_pixels = flat_pixels.reshape(pixels.shape)
    result_img = Image.fromarray(modified_pixels.astype('uint8'), 'RGB')
    
    # Save output
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = f"{base_name}_stego.png"
    
    result_img.save(output_path, 'PNG')
    
    print(f"{GREEN}[✓] {WHITE}Embedding completed successfully!{ENDC}")
    
    return output_path

def extract_file_from_image(stego_image_path, output_dir="."):
    """Extract embedded file from steganographic image"""
    
    if not os.path.exists(stego_image_path):
        raise FileNotFoundError(f"Stego image not found: {stego_image_path}")
    
    print(f"{YELLOW}[...] {WHITE}Extracting file from stego image...{ENDC}")
    
    # Open stego image
    img = Image.open(stego_image_path)
    pixels = np.array(img)
    flat_pixels = pixels.flatten()
    
    # Extract bits
    extracted_bits = ""
    for pixel_value in flat_pixels[:100000]:  # Limit extraction
        extracted_bits += str(pixel_value & 1)
    
    # Convert bits to bytes
    extracted_bytes = bytearray()
    for i in range(0, len(extracted_bits)-7, 8):
        byte = extracted_bits[i:i+8]
        if len(byte) == 8:
            extracted_bytes.append(int(byte, 2))
    
    # Extract header info
    if len(extracted_bytes) < 2:
        raise ValueError("No valid data found")
    
    ext_len = int.from_bytes(extracted_bytes[:2], byteorder='big')
    
    if len(extracted_bytes) < 2 + ext_len:
        raise ValueError("Corrupted data")
    
    file_ext = extracted_bytes[2:2+ext_len].decode('utf-8', errors='ignore')
    file_data = extracted_bytes[2+ext_len:]
    
    # Save extracted file
    output_filename = f"extracted_file{file_ext}"
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'wb') as f:
        f.write(file_data)
    
    print(f"{GREEN}[✓] {WHITE}File extracted successfully!{ENDC}")
    
    return output_path

def get_file_path():
    """Get file path from user with validation"""
    while True:
        print(f"\n{RED}[>] {CYAN}Enter the path of the file to embed {WHITE}(APK, script, etc.): {ENDC}", end="")
        file_path = input().strip()
        
        if os.path.exists(file_path):
            print(f"{GREEN}[✓] {WHITE}File found: {file_path}{ENDC}")
            return file_path
        else:
            print(f"{RED}[!] {YELLOW}File not found. Please check the path and try again.{ENDC}")

def get_image_path():
    """Get image path from user with validation"""
    while True:
        print(f"\n{RED}[>] {CYAN}Enter the path of the cover image: {ENDC}", end="")
        image_path = input().strip()
        
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img.verify()
                print(f"{GREEN}[✓] {WHITE}Valid image found: {image_path}{ENDC}")
                return image_path
            except Exception:
                print(f"{RED}[!] {YELLOW}Invalid image file. Please select a valid image.{ENDC}")
        else:
            print(f"{RED}[!] {YELLOW}Image not found. Please check the path and try again.{ENDC}")

def show_completion(output_path):
    """Show completion message with output path"""
    print(f"\n{GREEN}[★] {WHITE}PROCESS COMPLETED SUCCESSFULLY!{ENDC}")
    print(f"{RED}[>] {CYAN}Embedded image saved at: {WHITE}{output_path}{ENDC}")
    print(f"\n{YELLOW}[!] {WHITE}IMPORTANT NOTE:")
    print(f"{WHITE}   When someone clicks on this image, the embedded content will NOT")
    print(f"{WHITE}   automatically execute. Additional social engineering or exploitation")
    print(f"{WHITE}   techniques would be required for automatic execution, which is beyond")
    print(f"{WHITE}   the scope of this educational tool.")
    print(f"\n{GREEN}[✓] {WHITE}For extraction, use the -e flag with this tool.{ENDC}")

def show_links():
    """Show social media and website links"""
    print(f"\n{RED}╔══════════════════════════════════════════════════════════════════════════════╗")
    print(f"{RED}║{YELLOW}                           CONNECT WITH US                                   {RED}║")
    print(f"{RED}╠══════════════════════════════════════════════════════════════════════════════╣")
    print(f"{RED}║{WHITE}  YouTube: {CYAN}https://youtube.com/@UmarRumanCyber                            {RED}║")
    print(f"{RED}║{WHITE}  Instagram: {CYAN}https://instagram.com/UmarRumanCyber                        {RED}║")
    print(f"{RED}║{WHITE}  Website: {CYAN}https://UmarRumanCyber.com                                 {RED}║")
    print(f"{RED}╚══════════════════════════════════════════════════════════════════════════════╝")
    print(f"\n{GREEN}[>] {CYAN}For more Cyber Security & Ethical Hacking tutorials, check these links!{ENDC}\n")

def main():
    # Print banner and disclaimer
    print_banner()
    print_disclaimer()
    
    # Confirm authorization
    confirm_authorization()
    
    parser = argparse.ArgumentParser(description="Steganographer_3697 - Professional Steganography Tool")
    parser.add_argument("-f", "--file", help="Path to file to embed (APK, script, etc.)")
    parser.add_argument("-i", "--image", help="Path to cover image")
    parser.add_argument("-o", "--output", help="Output image path (optional)")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract file from stego image")
    parser.add_argument("-s", "--stego", help="Path to stego image for extraction")
    
    args = parser.parse_args()
    
    try:
        if args.extract and args.stego:
            print(f"{YELLOW}[...] {WHITE}Extracting file from stego image...{ENDC}")
            extracted_path = extract_file_from_image(args.stego)
            print(f"{GREEN}[+] {WHITE}File extracted successfully: {extracted_path}{ENDC}")
            
        elif args.file and args.image:
            output_path = embed_file_in_image(
                args.file, 
                args.image, 
                args.output
            )
            show_completion(output_path)
            
        else:
            # Interactive mode
            file_path = get_file_path()
            image_path = get_image_path()
            
            print(f"\n{YELLOW}[...] {WHITE}Starting embedding process...{ENDC}")
            output_path = embed_file_in_image(file_path, image_path)
            show_completion(output_path)
        
        show_links()
            
    except Exception as e:
        print(f"\n{RED}[!] {YELLOW}Error: {str(e)}{ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
