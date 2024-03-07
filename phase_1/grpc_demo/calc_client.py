import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    num1, num2 = 71539, 17593
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.MathServiceStub(channel)
        #print("Asking server to add [ {} ] and [ {} ]".format(num1, num2))
        #response_add = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
        print("Asking server to subtract [ {} ] and [ {} ]".format(num1, num2))
        response_subtract = stub.Subtract(calculator_pb2.SubtractRequest(num1=num1, num2=num2))
    #print("Addition Result: {}".format(response_add.result))
    print("Subtraction Result: {}".format(response_subtract.result))

if __name__ == "__main__":
    run()
