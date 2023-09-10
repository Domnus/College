import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        
        request = helloworld_pb2.HelloRequest(name='you')
        response = stub.SayHello(request)
        print("SayHello response:", response.message)
        
        request = helloworld_pb2.HelloRequest(num1=10, num2=5)
        response = stub.Soma(request)
        print("Soma response:", response.message)
        
        request = helloworld_pb2.HelloRequest(num1=10, num2=2)
        response = stub.Divisao(request)
        print("Divisao response:", response.message)

if __name__ == '__main__':
    run()
