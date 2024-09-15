import requests

class TestRailClient:
    def __init__(self, base_url, username, api_key):
        self.base_url = 'https://devexhub.testrail.io',
        self.username = ' ujjvalpandita@devexhub.in',
        self.api_key = 'NqmWX1IrBLe2Fi7Wf.4r-fgi.S5pCcqRpWQaHUpC4'         

    def send_post(self, endpoint, data):
        url = f"{self.base_url}/index.php?/api/v2/{endpoint}"
        response = requests.post(url, auth=(self.username, self.api_key), json=data)
        response.raise_for_status()
        return response.json()

    def add_result_for_case(self, run_id, case_id, status_id, comment=''):
        data = {
            'status_id': status_id,
            'comment': comment
        }
        return self.send_post(f'add_result_for_case/{run_id}/{case_id}', data)
    

