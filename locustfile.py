from locust import HttpUser, task, between
import random
import json

class CalculatorUser(HttpUser):
    wait_time = between(2, 4)
    
    @task(2)  
    def add(self):
        self._calculate("add", 1, 1, expected_result=2)
        
    @task(1)
    def subtract(self):
        self._calculate("subtract", 5, 3, expected_result=2)
        
    @task(1)
    def multiply(self):
        self._calculate("multiply", 2, 3, expected_result=6)
        
    @task(1)
    def divide(self):
        self._calculate("divide", 10, 2, expected_result=5)

    def _calculate(self, operation, op1, op2, expected_result):
        payload = {"operation": operation, "operand1": op1, "operand2": op2}
        with self.client.post("/calculate", json=payload, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"HTTP {response.status_code}")
                return
            try:
                data = response.json()
            except Exception as e:
                response.failure(f"Invalid JSON response: {e}")
                return
            if data.get("result") != expected_result:
                response.failure(f"Incorrect result for {operation}: {data.get('result')}")
