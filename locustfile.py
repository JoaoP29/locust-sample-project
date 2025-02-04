from locust import HttpUser, task, between
import random

class ReqResUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def list_users(self):
        self.client.get("/api/users")

    @task(2)
    def create_user(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.client.post("/api/users", json=payload)
        if response.status_code == 201:
            user_id = response.json().get("id")
            self.update_user(user_id)

    def update_user(self, user_id):
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        self.client.put(f"/api/users/{user_id}", json=payload)

    @task(1)
    def delete_user(self):
        user_id = random.randint(1, 12)
        self.client.delete(f"/api/users/{user_id}")
