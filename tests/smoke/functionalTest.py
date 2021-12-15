

def routing(app, request):
    routes = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        print(rule)
        # routes.append(str(rule))
        with app.test_client() as client:
            route = client.get(str(rule))
            
            # the contexts are not popped even though the request ended
            print(route)
    
    return "ok"
    # testing(app, request, routes)
        
def testing(app, request, routes):
    
    with app.test_client() as client:
        route = client.get('/home')
        
        # the contexts are not popped even though the request ended
        return request.path . route.status_code
 
    # app.testing = True
    # # with app.test_client() as c:
    # #     response = c.get('/some/path/that/exists')
    # #     self.assertEquals(response.status_code, 200)
    # with app.test_client() as client:
    #     route = client.get('/pa')
        
    #     # the contexts are not popped even though the request ended
    #     print(request.path, route.status_code)

