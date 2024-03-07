# gRPC Demo

## Overview

In this demo, we will take a look at a very basic example of `gRPC`

## Requirements

Confirm the following packages are installed, if not, install them using `pip`

```shell
python3 -m pip freeze | egrep "grpcio|grpcio-tools"
```

## gRPC Service

The gRPC service is defined in the `calculator.proto` file, with the RPC method parameters and return types.

```proto
syntax = "proto3";
package calculator;

// Math service definition
service MathService {
  rpc Add (AddRequest) returns (AddResponse) {}
  rpc Subtract (SubtractRequest) returns (SubtractResponse) {}
}

// The request message containing two numbers.
message AddRequest {
  int32 num1 = 1;
  int32 num2 = 2;
}

// The response message containing the result.
message AddResponse {
  int32 result = 1;
}

// The request message containing two numbers.
message SubtractRequest {
  int32 num1 = 1;
  int32 num2 = 2;
}

// The response message containing the result.
message SubtractResponse {
  int32 result = 1;
}
```

gRPC uses `protoc` with a special gRPC plugin to generate code from your proto file: you get generated gRPC client and server code, as well as the regular protocol buffer code for populating, serializing, and retrieving your message types

In this example, the following files have already been generated:

- `calculator_pb2.py`: Contains the generated request and response classes
- `calculator_pb2_grpc.py`: Contains the generated client and server classes

If making any changes to the service definition file such as adding a new service, the gRPC code can be regenerated using the below command:

```shell
python3 -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. calculator.proto
```

## Running the application

### Start the server

```shell
$ python3 calc_server.py 
Server started, listening on port: 50051
```

### Start the client

```shell
$ python3 calc_client.py 
Asking server to add [ 71539 ] and [ 17593 ]
Asking server to subtract [ 71539 ] and [ 17593 ]
Addition Result: 89132
Subtraction Result: 53946
```

### Analyzing gRPC messages in Wireshark

With the .proto files available Wireshark can be used to analyze **plain text** gRPC messages that are transferred over the network. More details can be found [here](https://grpc.io/blog/wireshark/).

Sample parsed capture,

#### Request

```shell
Frame 16: 78 bytes on wire (624 bits), 78 bytes captured (624 bits)
Linux cooked capture v1
Internet Protocol Version 4, Src: 192.168.40.96, Dst: 192.168.129.170
Transmission Control Protocol, Src Port: 53289, Dst Port: 50051, Seq: 319, Ack: 62, Len: 22
HyperText Transfer Protocol 2
GRPC Message: /calculator.MathService/Add, Request
    0... .... = Frame Type: Data (0)
    .... ...0 = Compressed Flag: Not Compressed (0)
    Message Length: 8
    Message Data: 8 bytes
Protocol Buffers: /calculator.MathService/Add,request
    Message: calculator.AddRequest
        Field(1): num1 = 71539 (int32)
        Field(2): num2 = 17593 (int32)
```

#### Response

```shell
Frame 19: 225 bytes on wire (1800 bits), 225 bytes captured (1800 bits)
Linux cooked capture v1
Internet Protocol Version 4, Src: 192.168.129.170, Dst: 192.168.40.96
Transmission Control Protocol, Src Port: 50051, Dst Port: 53289, Seq: 79, Ack: 341, Len: 157
HyperText Transfer Protocol 2
HyperText Transfer Protocol 2
GRPC Message: /calculator.MathService/Add, Response
    0... .... = Frame Type: Data (0)
    .... ...0 = Compressed Flag: Not Compressed (0)
    Message Length: 4
    Message Data: 4 bytes
Protocol Buffers: /calculator.MathService/Add,response
    Message: calculator.AddResponse
        Field(1): result = 89132 (int32)
HyperText Transfer Protocol 2
HyperText Transfer Protocol 2
```