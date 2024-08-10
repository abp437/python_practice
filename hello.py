# You can go to the definition of the library itself. Awesome!
import os, platform

print("Hello, World!")
print(os.name) # Why does it print `posix`?
# POSIX indicates a Unix-like operating system (including Linux, macOS, and other Unix variants).

# Detailed OS info
print("platform.system:", platform.system())

if os.name == 'posix':
  print("Detailed OS info:", os.uname())
