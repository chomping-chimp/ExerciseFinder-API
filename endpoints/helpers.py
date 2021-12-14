
class RequestHelper:
    
    def __init__(self):
        self.default_methods = 'GET'

    def create_request_headers(self, response, methods=None):
        """Method that returns a template for the headers of a response

        Args:
            methods (str, optional): Methods of the request. Defaults to None.

        Returns:
            [dict]: A dictionary of the headers
                {
                    "Access-Control-Allow-Credentials": "GET",
                    "Access-Control-Allow-Headers": "Origin, Content-Type, Accept",
                    "Access-Control-Allow-Origin": "*",
                    "Content-Type": "application/json",
                }
        """
        # More to be done on this, this has more potential
        # Create headers
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
        # Check if methods are specified, if not, default to 'GET'
        if not methods:
            response.headers['Access-Control-Allow-Credentials'] = self.default_methods
        else: 
            response.headers['Access-Control-Allow-Credentials'] = methods
        # Return headers
        return response
    
    def create_response_meta(self, data, status):
        """
        Method that creates metadata information for the response

        Args:
            data (list): Data to be returned from endpoint
            status (int): Status of operation

        Returns:
            (dict): Collection of metadata information
        """
        total_count = 0

        if data:
            total_count = len(data)

        return {
            "Total Results": total_count,
            "Status": status

