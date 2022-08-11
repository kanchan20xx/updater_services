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
        for package_key in recipes.keys():
            package = updater_recipe_service_pb2.Package(
                package_name=package_key,
                files=self.__GetFileInPackage(pkg_name=package_key))
            dst_packages.append(package)
        return updater_recipe_service_pb2.GetPackagesReply(packages=dst_packages)
    def __GetFileInPackage(self, pkg_name):
        return recipes.get(pkg_name)

def RegisterGrpcServer(grpc_server):
    updater_recipe_service_pb2_grpc.add_UpdaterRecipeServiceServicer_to_server(UpdaterRecipeService(), server=grpc_server)
    return