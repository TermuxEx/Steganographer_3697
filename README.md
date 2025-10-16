# Steganographer_3697

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)

## 🛡️ Professional Steganography Tool

**Steganographer_3697** is a professional-grade steganography tool designed for embedding files (APKs, scripts, documents, etc.) into images. This tool is built for **authorized penetration testing**, **ethical hacking research**, and **educational purposes**.

Created by **Umar Ruman**, this tool incorporates advanced LSB (Least Significant Bit) steganography techniques to securely conceal data within image files.

## ⚠️ DISCLAIMER

This tool is intended for **authorized security testing and educational purposes only**. By using this tool, you agree that:
1. You have explicit written permission to test the systems involved
2. You will only use this tool on systems you are authorized to access
3. You will comply with all applicable local, state, and federal laws
4. You will not use this tool for any malicious or unauthorized activities

**Unauthorized use is strictly prohibited and may result in criminal charges.**

## 🌟 Features

- **Universal File Support**: Embed any file type (APK, scripts, documents, binaries)
- **Advanced Steganography**: Uses LSB technique for secure data concealment
- **Format Preservation**: Maintains original file extensions for proper reconstruction
- **Interactive Interface**: User-friendly guided process
- **Authorization Check**: Built-in compliance verification
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Error Handling**: Comprehensive validation and error reporting

## 📋 Requirements

- Python 3.6 or higher
- Pillow (PIL) library
- NumPy library

## 🔧 Installation

### Method 1: Direct Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Steganographer_3697.git
cd Steganographer_3697

# Install required packages
pip install -r requirements.txt
```

### Method 2: Manual Installation
```bash
# Install dependencies
pip install Pillow numpy

# Download the script
wget https://raw.githubusercontent.com/yourusername/Steganographer_3697/main/steganographer_3697.py
```

### Requirements File (requirements.txt)
```txt
Pillow>=8.0.0
numpy>=1.19.0
```

## 🚀 Usage

### Interactive Mode (Recommended)
```bash
python steganographer_3697.py
```

### Command Line Mode
```bash
# Embed a file into an image
python steganographer_3697.py -f /path/to/file.apk -i /path/to/image.jpg -o output.png

# Extract a file from a stego image
python steganographer_3697.py -e -s /path/to/stego_image.png
```

### Command Line Arguments
```bash
-h, --help            show this help message and exit
-f FILE, --file FILE  Path to file to embed (APK, script, etc.)
-i IMAGE, --image IMAGE
                      Path to cover image
-o OUTPUT, --output OUTPUT
                      Output image path (optional)
-e, --extract         Extract file from stego image
-s STEGO, --stego STEGO
                      Path to stego image for extraction
```

## 📖 How It Works

### Embedding Process:
1. Validates input file and image paths
2. Reads the file to be embedded
3. Encodes file metadata (extension) for reconstruction
4. Converts file data to binary format
5. Embeds data into image using LSB steganography
6. Saves the steganographic image

### Extraction Process:
1. Reads stego image pixel data
2. Extracts embedded bits from LSBs
3. Reconstructs original file data
4. Recreates original file with preserved extension

### Security Features:
- **LSB Technique**: Modifies only the least significant bits to minimize visual distortion
- **Metadata Preservation**: Maintains file extension for proper reconstruction
- **Capacity Checking**: Verifies image can hold the embedded file
- **Error Handling**: Validates all inputs and provides clear error messages

## ⚙️ Technical Details

### Steganography Method
The tool uses **Least Significant Bit (LSB)** steganography:
- Each bit of the file data is embedded in the LSB of image pixel values
- Minimal visual distortion to the cover image
- Robust against casual inspection

### File Format Support
- **Images**: JPEG, PNG, BMP, TIFF (saved as PNG to preserve quality)
- **Files**: Any file type (APK, EXE, DOC, PDF, scripts, etc.)

### Capacity Considerations
- Image must have sufficient pixels to hold the embedded data
- As a rule of thumb: 1 pixel can hold 1 bit of data
- For large files, use high-resolution cover images

## 📚 Usage Examples

### Example 1: Embed an APK file
```bash
python steganographer_3697.py -f malware.apk -i cat_photo.jpg -o hidden_cat.png
```

### Example 2: Extract embedded file
```bash
python steganographer_3697.py -e -s hidden_cat.png
```

### Example 3: Interactive mode
```bash
python steganographer_3697.py
# Follow the interactive prompts
```

## 🔒 Security Considerations

### Detection Resistance
- LSB steganography can be detected by statistical analysis
- For serious applications, consider more advanced techniques
- This tool is intended for educational and authorized testing

### Best Practices
1. Use high-quality, complex images as covers
2. Keep embedded files small relative to image size
3. Store stego images in common formats (PNG recommended)
4. Document all testing activities thoroughly

## 🛠️ Troubleshooting

### Common Issues:
1. **"Image too small to hold the file"**:
   - Use a higher resolution image or smaller file
   
2. **"Invalid image file"**:
   - Ensure the cover image is not corrupted
   - Try converting to PNG format

3. **"File not found"**:
   - Check file paths for typos
   - Ensure proper file permissions

### Performance Tips:
- Larger images take longer to process
- PNG format recommended for lossless embedding
- Keep original cover images for comparison

## 📄 Legal and Ethical Usage

**This tool is for LEGITIMATE SECURITY RESEARCH ONLY!**

Before using this tool, ensure you have:
1. Written authorization from system owners
2. Defined scope of testing activities
3. Proper documentation of all actions
4. Clear understanding of applicable laws

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### Areas for Improvement:
- Enhanced steganography algorithms
- GUI interface
- Batch processing capabilities
- Additional file format support

## 📞 Contact

For questions about legitimate security research usage:
- YouTube: [Cyber Ex Study](https://youtube.com/@UmarRumanCyber)
- Instagram: [@cyber_ex_3697](https://instagram.com/UmarRumanCyber)
- Website: [cyber3697.syrge.sh](https://UmarRumanCyber.com)

## ⚠️ Final Note

This tool is provided for educational and authorized security testing purposes. The creator assumes no liability for misuse. Always follow ethical guidelines and legal requirements in your security research activities.

---
**Remember**: With great power comes great responsibility. Use this tool ethically and legally!
