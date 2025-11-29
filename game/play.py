#!/usr/bin/env python3
"""
Sasiran Language Game - Simple Launcher
Quick way to start the game server
"""

import subprocess
import sys
from pathlib import Path


def check_dependencies():
    """Check if required Python packages are installed."""
    required_packages = ["markdown"]
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(f"📦 Installing required packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install"] + missing_packages
            )
            print("✅ Packages installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please install manually:")
            print(f"   pip install {' '.join(missing_packages)}")
            return False

    return True


def main():
    """Main launcher function."""
    print("🏛️  Sasiran Language Game Launcher")
    print("=" * 40)

    # Check if we're in the right directory
    if not Path("server.py").exists():
        print("❌ Please run this script from the game directory!")
        print("   The game directory should contain server.py")
        sys.exit(1)

    # Check dependencies
    if not check_dependencies():
        sys.exit(1)

    # Get port number
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"❌ Invalid port number: {sys.argv[1]}")
            sys.exit(1)

    print(f"🚀 Starting Sasiran game server on port {port}...")
    print(f"🌐 Open your browser to: http://localhost:{port}")
    print("⏹️  Press Ctrl+C to stop the server")
    print("")

    try:
        # Start the server
        subprocess.run([sys.executable, "server.py", str(port)])
    except KeyboardInterrupt:
        print("\n🛑 Game server stopped. Thanks for playing!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
