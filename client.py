
import grpc
from proto import service_pb2
from proto import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.SampleServiceStub(channel)
        response = stub.SayHello(service_pb2.HelloRequest(name='Yamada'))
    print('RECV : %s' % response.message)

if __name__ == '__main__':
    run()