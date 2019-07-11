import os
import subprocess
import sys

image = sys.stdin.buffer.read()
sys.stdout.buffer.write(image)
