from Resources.resource import RegisterApi,LoginApi,BirdsAPI,BirdCRUDAPI


def initialize_routes(api):
    api.add_resource(RegisterApi, "/api/signup")
    api.add_resource(LoginApi, "/api/login")
    api.add_resource(BirdsAPI, '/api/bird')
    api.add_resource(BirdCRUDAPI, "/api/bird/update")
