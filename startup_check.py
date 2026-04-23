"""
Startup verification script for Exam Result System
Ensures all dependencies and modules are properly installed
"""

import sys
import os

def check_dependencies():
    """Check if all required packages are installed"""
    print("=" * 60)
    print("📋 DEPENDENCY CHECK")
    print("=" * 60)
    
    required_packages = {
        'streamlit': 'Streamlit Web Framework',
        'pandas': 'Data Processing',
        'numpy': 'Numerical Computing',
        'matplotlib': 'Visualization',
        'openpyxl': 'Excel File Handling',
        'reportlab': 'PDF Generation',
        'PIL': 'Image Processing'
    }
    
    missing = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"✓ {package:15} - {description}")
        except ImportError:
            print(f"✗ {package:15} - {description}")
            missing.append(package)
    
    if missing:
        print("\n⚠️  Missing packages detected!")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n✓ All dependencies installed!")
    return True


def check_modules():
    """Check if all project modules are accessible"""
    print("\n" + "=" * 60)
    print("📁 MODULE CHECK")
    print("=" * 60)
    
    sys.path.insert(0, 'src')
    
    modules = {
        'data_processor': 'Data Processing Module',
        'analyzer': 'Analytics Module',
        'report_generator': 'PDF Report Generator'
    }
    
    missing = []
    
    for module, description in modules.items():
        try:
            __import__(module)
            print(f"✓ {module:20} - {description}")
        except ImportError as e:
            print(f"✗ {module:20} - {description}")
            print(f"  Error: {e}")
            missing.append(module)
    
    if missing:
        print("\n⚠️  Missing modules detected!")
        return False
    
    print("\n✓ All modules loaded successfully!")
    return True


def check_directories():
    """Check if required directories exist"""
    print("\n" + "=" * 60)
    print("📂 DIRECTORY CHECK")
    print("=" * 60)
    
    directories = {
        'src': 'Source Code',
        'data': 'Input Data',
        'outputs': 'Output Results',
        'outputs/reports': 'PDF Reports',
        'outputs/charts': 'Chart Images'
    }
    
    missing = []
    
    for dir_path, description in directories.items():
        if os.path.isdir(dir_path):
            print(f"✓ {dir_path:20} - {description}")
        else:
            print(f"✗ {dir_path:20} - {description}")
            missing.append(dir_path)
    
    if missing:
        print("\n⚠️  Missing directories. Creating them...")
        for dir_path in missing:
            os.makedirs(dir_path, exist_ok=True)
            print(f"  Created: {dir_path}")
        return True
    
    print("\n✓ All directories present!")
    return True


def check_files():
    """Check if required files exist"""
    print("\n" + "=" * 60)
    print("📄 FILE CHECK")
    print("=" * 60)
    
    files = {
        'app.py': 'Main Application',
        'requirements.txt': 'Dependencies List',
        'README.md': 'Documentation',
        'src/data_processor.py': 'Data Processing Module',
        'src/analyzer.py': 'Analytics Module',
        'src/report_generator.py': 'Report Generator Module',
        'src/__init__.py': 'Package Initializer'
    }
    
    missing = []
    
    for file_path, description in files.items():
        if os.path.isfile(file_path):
            print(f"✓ {file_path:30} - {description}")
        else:
            print(f"✗ {file_path:30} - {description}")
            missing.append(file_path)
    
    if missing:
        print("\n⚠️  Missing files detected!")
        return False
    
    print("\n✓ All required files present!")
    return True


def main():
    """Run all checks"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║  EXAM RESULT SYSTEM - STARTUP VERIFICATION                ║")
    print("║  Automated Exam Result Processing & Analytics             ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    results = {
        'Dependencies': check_dependencies(),
        'Modules': check_modules(),
        'Directories': check_directories(),
        'Files': check_files()
    }
    
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    
    for check, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{check:20} ... {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ ALL CHECKS PASSED - Ready to run!")
        print("\nTo start the application, run:")
        print("  streamlit run app.py")
        print("\nThen open your browser to: http://localhost:8501")
    else:
        print("✗ SOME CHECKS FAILED - Please fix errors above")
        print("\nTroubleshooting:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Verify Python version: python --version (3.7+)")
        print("3. Check file permissions")
        print("4. Ensure all files are in correct locations")
    print("=" * 60)
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
