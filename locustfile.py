from locust import HttpUser, task, between

class CalcUser(HttpUser):
    wait_time = between(2, 4)

    def on_start(self):
        pass

    @task(2)
    def add(self):
        self.run_calc("add", 1, 1, 2)

    @task(1)
    def sub(self):
        self.run_calc("subtract", 2, 1, 1)

    @task(1)
    def mul(self):
        self.run_calc("multiply", 2, 2, 4)

    @task(1)
    def div(self):
        self.run_calc("divide", 4, 2, 2)

    def run_calc(self, op, a, b, expected):
        data = {"operation": op, "operand1": a, "operand2": b}
        with self.client.post("/calculate", json=data, name=op, catch_response=True) as res:
            if res.status_code != 200:
                res.failure(f"HTTP {res.status_code}")
                return
            try:
                result = res.json().get("result")
            except Exception as e:
                res.failure(f"Invalid JSON: {e}")
                return
            if result != expected:
                res.failure(f"Wrong {op} result: {result} (expected {expected})")

if __name__ == "__main__":
    from locust import run_single_user
    CalcUser.host = "http://127.0.0.1:5000"
    run_single_user(CalcUser)


