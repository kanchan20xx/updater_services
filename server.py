#coding at utf-8
from concurrent import futures

import grpc
import sample_service
import env_repo_service

def serve():
    # Create grpc server.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add handler.
    sample_service.RegisterGrpcServer(server)
    env_repo_service.RegisterGrpcServer(server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()