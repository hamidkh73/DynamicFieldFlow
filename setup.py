from setuptools import setup, find_packages
import sysconfig
import sys

platform = sysconfig.get_platform()
python_version = sys.version_info

# Check for M1/M2 Mac (Apple Silicon)
is_apple_silicon = (
    platform.startswith("mac") and 
    ("arm64" in platform or "universal" in platform)
)

# Check for Colab (usually Linux with specific characteristics)
is_colab = (
    "google.colab" in sys.modules or
    platform.startswith("linux") and "x86_64" in platform
)

if is_apple_silicon:
    # M1/M2 Mac dependencies with updated versions
    install_requires = [
        'DynamicFieldPy',
        'tensorflow-macos>=2.12.0',  # Updated to available version
        'matplotlib>=3.6.0',         # Updated for compatibility
        'numpy>=1.23.0',             # Updated for M1/M2 compatibility
        'scipy>=1.10.0',             # Updated version
        'tensorflow-probability>=0.19.0',  # Updated to match TF version
        'protobuf>=3.20.0,<4.0.0'   # Flexible protobuf version
    ]
elif is_colab or platform.startswith("linux"):
    # Colab/Linux dependencies with current versions
    install_requires = [
        'DynamicFieldPy',
        'tensorflow>=2.12.0',        # Use current TF version
        'matplotlib>=3.6.0',
        'numpy>=1.23.0',
        'scipy>=1.10.0',
        'tensorflow-probability>=0.19.0',
        'protobuf>=3.20.0,<4.0.0'
    ]
else:
    # Default for other platforms (Windows, older systems)
    install_requires = [
        'DynamicFieldPy',
        'tensorflow>=2.12.0',        # Updated from 2.9.0
        'matplotlib>=3.6.0',         # More flexible version
        'numpy>=1.22.0',             # Minimum compatible version
        'scipy>=1.9.0',              # Minimum compatible version
        'tensorflow-probability>=0.19.0',  # Updated version
        'protobuf>=3.20.0,<4.0.0'   # Avoid protobuf 4.x issues
    ]

setup(
    name='DynamicFieldFlow',
    version='0.1',
    description='A library for simulating Dynamic Field architectures with TensorFlow',
    url='https://github.com/danielsabinasz/DynamicFieldFlow',
    author='Daniel Sabinasz',
    author_email='daniel@sabinasz.net',
    license='CC-BY-ND 3.0',
    packages=find_packages(include=['dff', 'dff.*']),
    install_requires=install_requires,
    python_requires='>=3.8',  # Added Python version requirement
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
