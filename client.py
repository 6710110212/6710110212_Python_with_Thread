import socket

def start_client():
    host = "127.0.0.1"
    port = 25000       

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server. Type 'exit' to quit.")

        while True:
            operation = input("Enter operation (add, sub, mul, div): ")
            if operation.lower() == "exit":
                break

            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            
            message = f"{operation} {num1} {num2}"
            s.sendall(message.encode())
            
            data = s.recv(1024)
            print("Server response:", data.decode())

if __name__ == "__main__":
    start_client()