run_server:
	uvicorn main:app --reload

run_stress_test:
	ab -n 800 -c 10 http://127.0.0.1:8000/ping/

.PHONY: run_server
.PHONY: run_stress_test