
import grpc
from proto import service_pb2
from proto import service_pb2_grpc
from proto import env_repo_service_pb2
from proto import env_repo_service_pb2_grpc
from proto import updater_recipe_service_pb2
from proto import updater_recipe_service_pb2_grpc

def run():
    # with grpc.insecure_channel('localhost:50051') as channel:
        # stub = service_pb2_grpc.SampleServiceStub(channel)
        # response = stub.SayHello(service_pb2.HelloRequest(name='Yamada'))
    # print('RECV : %s' % response.message)
    # print("%d" % len(response.ids))
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = env_repo_service_pb2_grpc.EnvRepoServiceStub(channel=channel)
        #response = stub.GetEnvInfo(env_repo_service_pb2.GetEnvInfoReply())
        response = stub.GetDiffFiles(env_repo_service_pb2.GetDiffFilesRequest(target_tag='V6.16.0'))
        print(len(response.diff_files))
        response = stub.GetTargetableTags(env_repo_service_pb2.Empty())
        print(response.tags[0].tag_name)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = updater_recipe_service_pb2_grpc.UpdaterRecipeServiceStub(channel=channel)
        response = stub.GetPackages(updater_recipe_service_pb2.Empty())
        for responsed_pkg in response.packages:
            print(responsed_pkg.package_name)

if __name__ == '__main__':
    run()