# coding=utf-8
import grpc
from proto import updater_recipe_service_pb2
from proto import updater_recipe_service_pb2_grpc

recipes = {
    'x64' : ['a', 'b', 'c'],
    'x86' : ['d', 'e', 'f']}

class UpdaterRecipeService(updater_recipe_service_pb2_grpc.UpdaterRecipeServiceServicer):
    def GetPackages(self, request, context):
        dst_packages = []
        for package in recipes.keys():
            dst_packages.append(updater_recipe_service_pb2.GetPackagesReply(package_name=package))
        return updater_recipe_service_pb2.GetPackagesReply(packages=dst_packages)
    def GetFileInPackage(self, request, context):
        tag = request.package_name
        file_paths = recipes.get(tag)
        if file_paths is None:
            return updater_recipe_service_pb2.GetFileInPackageReply([])
        return updater_recipe_service_pb2.GetFileInPackageReply(file_paths)

def RegisterGrpcServer(grpc_server):
    updater_recipe_service_pb2.add_EnvRepoServiceServicer_to_server(UpdaterRecipeService(), server=grpc_server)
    return