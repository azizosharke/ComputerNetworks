# https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
import socket

# initializes the socket obj, hostname and port and binds it to the server
socketVar = socket.socket()
hostName = socket.gethostname()
port = 8090
socketVar.bind((hostName, port))
socketVar.listen(1)  # wait for 1 incoming connection

print(hostName)

# loops to accept the incoming connection and file being sent from the client
while True:
    print("Waiting for connection...")
    connection, address = socketVar.accept()

    print(address, "Has connected to the server")

    # receives the fileName and number of packets from the client
    fileName = connection.recv(1024)
    fileName = fileName.decode()
    numOfPackets = connection.recv(1024)
    decodedNumOfPackets = numOfPackets.decode()
    numOfPackets = int(decodedNumOfPackets)

    # open the file in write-binary
    file = open(fileName, 'wb')

    # loops to keep receiving packets and prints the packets being received from the client
    for x in range(1, numOfPackets + 1):
        numOfPacketsRecv_String = f"Receiving packet #{x} from server..."
        print(numOfPacketsRecv_String)
        data = connection.recv(1024)
        file.write(data)
    connection.close()
    file.close()

    print("\nData has been transmitted successfully!\n")
