#!/usr/bin/env python3
"""
Quick launcher for the Sasiran Markdown Viewer
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Launch the markdown viewer"""
    print("📚 Sasiran Markdown Viewer Launcher")
    print("=" * 40)

    # Check if we're in the right directory
    if not Path("server.py").exists():
        print("❌ Please run this script from the viewer directory!")
        sys.exit(1)

    # Get port number
    port = 8001
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"❌ Invalid port number: {sys.argv[1]}")
            sys.exit(1)

    print(f"🚀 Starting markdown viewer on port {port}...")
    print("")

    try:
        subprocess.run([sys.executable, "server.py", str(port)])
    except KeyboardInterrupt:
        print("\n🛑 Viewer stopped.")
    except Exception as e:
        print(f"❌ Error starting viewer: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
