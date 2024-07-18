import socket

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enable reuse address/port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the address and port
    server_socket.bind(("localhost", 6379))
    
    # Listen for incoming connections
    server_socket.listen()

    print("Server is listening on localhost:6379")
    
    # Accept a client connection (this will block until a client connects)
    client_socket, client_address = server_socket.accept()
    
    print(f"Connection accepted from {client_address}")
    client_socket.close()

if __name__ == "__main__":
    main()
