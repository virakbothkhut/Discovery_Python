#!/usr/bin/env python3
import sys

param = sys.argv[1:]

if not param:
    print("none")
    exit(0)
print(f"Parameters:{len(sys.argv)-1}")
for p in param:
    print(f"{p}: {len(p)}")










# #!/usr/bin/env python3

# import sys

# # Exclude the script name and check if arguments exist
# params = sys.argv[1:]

# if not params:
#     print("none")
#     exit(0)

# # Print the number of parameters
# print(f"parameters: {len(params)}")

# # Print each parameter with its length
# for param in params:
#     print(f"{param}: {len(param)}")
