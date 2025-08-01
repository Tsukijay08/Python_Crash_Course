import signal
import time

def handle_signal(signum, frame):
   print(f"Signal {signum} received")

# Setting the handler for SIGINT
signal.signal(signal.SIGINT, handle_signal)

print("Press Ctrl+C to trigger SIGINT")
while True:
   time.sleep(1)