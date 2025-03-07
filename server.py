import socket
import threading
import simple_calculator

def handle_client(client_socket, addr):
    print(f"Client {addr} connected.")
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            operation, num1, num2 = data.split()
            num1, num2 = float(num1), float(num2)

            if operation == "add":
                result = simple_calculator.add(num1, num2)
            elif operation == "sub":
                result = simple_calculator.subtract(num1, num2)
            elif operation == "mul":
                result = simple_calculator.multiply(num1, num2)
            elif operation == "div":
                result = simple_calculator.divide(num1, num2)
            else:
                result = "The command is incorrect."

            client_socket.send(str(result).encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            break

    print(f"Client {addr} disconnected.")
    client_socket.close()

def server_main():
    host = ""        
    port = 25000     

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Prevent port binding issues
        s.bind((host, port))
        s.listen()
        print(f"Server listening on port {port}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            print(f"Active connections with clients: {threading.active_count() - 1}")

if __name__ == "__main__":
    server_main()
