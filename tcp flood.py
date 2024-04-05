import socket
import threading
import time


connection_duration = 15                   # in seconds
delay_between_data_transmissions = 0.05       # amount of time to wait between resending data (in seconds)
target_host = "127.0.0.1"
target_port = 135
num_connections = 15


def connect_to_port():
    try:
        # Create a TCP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the target host and port
        client.connect((target_host, target_port))

        print(f"Connected to {target_host}:{target_port}")

        for i in range(0, int((connection_duration/delay_between_data_transmissions)), 1):
            # Send some data (optional)
            client.send(b"Eat my data!\r\n")
            time.sleep(delay_between_data_transmissions)

        # Close the connection
        # client.close()
    except Exception as e:
        print(f"Error: {e}")

# Create threads for each connection
threads = []
for _ in range(num_connections):
    t = threading.Thread(target=connect_to_port)
    threads.append(t)
    t.start()

# Wait for all threads indefinitely to complete
for t in threads:
    t.join()

print("All connections closed...")
